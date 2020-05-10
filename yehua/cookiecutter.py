import os
from copy import deepcopy

import yehua.utils as utils
from yehua.utils import dump_yaml
from yehua.project import Project

from jinja2 import Environment
import logging


MOBAN_FILE_FOR_COOKIE_CUTTER = """
configuration:
  template_dir:
  - ""
  configuration: project.json
  force_template_type: cookiecutter
  template_types:
    cookiecutter:
      base_type: jinja2
      file_extensions:
        - cookiecutter
      options:
        trim_blocks: false
        lstrip_blocks: false
        extensions:
          - cookiecutter.extensions.JsonifyExtension
          - jinja2_time.TimeExtension
"""
LOG = logging.getLogger(__name__)


class CookieCutter(Project):
    def __init__(self, project_content, base_dir):
        self.source_dir = base_dir
        self.template_dir = base_dir
        self.project_content = project_content
        self.project_name = None
        self.answers = None
        self.name = None
        self.directives = None
        self.cookie_cutter_dir = utils.find_project_name(self.source_dir)
        self._ask_questions()
        self._append_magic_variables()
        self._template_yehua_file()

    def _create_jj2_environment(self, _):
        return Environment(
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
            block_start_string="<cookiecutter%",
            block_end_string="%cookiecutter>",
            variable_start_string="<cookiecutter<",
            variable_end_string=">cookiecutter>",
        )

    def _template_yehua_file(self):
        template = self.jj2_environment.from_string(self.project_content)
        renderred_content = template.render(**self.answers)
        self.directives = utils.load_yaml(renderred_content)

    def _ask_questions(self):
        first_stage = utils.load_yaml(self.project_content)
        self.answers = get_user_inputs(first_stage["questions"])

        my_dict = {"cookiecutter": deepcopy(self.answers)}
        my_dict["project_name"] = self.cookie_cutter_dir

        tmp_env = Environment(
            keep_trailing_newline=True, trim_blocks=True, lstrip_blocks=True
        )

        template = tmp_env.from_string(my_dict["project_name"])

        renderred_content = template.render(**my_dict)
        my_dict["project_name"] = renderred_content
        self.answers = my_dict

    def templating(self):
        path = os.path.join(
            self.answers["project_name"], self.answers["project_name"] + ".yml"
        )
        with open(path, "w") as f:
            project_yaml = deepcopy(self.answers)
            project_yaml.pop("now")  # is not required
            dump_yaml(project_yaml, f)

        moban_file = utils.load_yaml(MOBAN_FILE_FOR_COOKIE_CUTTER)
        moban_file["configuration"]["configuration"] = (
            self.answers["project_name"] + ".yml"
        )
        moban_file["targets"] = self.directives["moban"]

        if "://" in self.template_dir:
            moban_file["configuration"]["template_dir"][0] = (
                self.template_dir + "!/" + self.cookie_cutter_dir
            )
        else:
            moban_file["configuration"]["template_dir"][0] = (
                os.path.abspath(self.template_dir)
                + "/"
                + self.cookie_cutter_dir
            )
        with open(
            os.path.join(self.answers["project_name"], ".moban.yml"), "w"
        ) as f:
            dump_yaml(moban_file, f)


def get_user_inputs(questions):  # refactor this later
    LOG.debug(questions)
    answers = {}
    for q in questions:
        for key, question in q.items():
            if isinstance(question, list):
                q, additional = raise_complex_question(question)
                answers[key] = q
                if additional:
                    answers.update(additional)
            else:
                a = utils.yehua_input(question + " ")
                answers[key] = a
    LOG.debug(answers)
    return answers


def raise_complex_question(question):
    additional_answers = None
    for subq in question:
        subquestion = subq.pop("question")
        suggested_answers = sorted(subq.keys())
        long_question = [subquestion] + suggested_answers
        choice = "(%s): " % (
            ",".join([str(x) for x in range(1, len(long_question))])
        )
        long_question.append(choice)
        a = utils.yehua_input("\n".join(long_question))
        for key in suggested_answers:
            if key.startswith(a):
                string_answer = key.split(".")[1].strip()
                if subq[key] != "N/A":
                    additional_answers = get_user_inputs(subq[key])
        break
    return string_answer, additional_answers
