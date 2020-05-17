import os
import logging
from copy import deepcopy

import yehua.utils as utils
from yehua.utils import dump_yaml, get_user_inputs
from yehua.project import Project

from jinja2 import Environment

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
        utils.color_print(first_stage["introduction"])
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
        utils.color_print(
            f"\u2713 Your answers are saved in [info]{path}[/info]!"
        )

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
        moban_file_path = os.path.join(
            self.answers["project_name"], ".moban.yml"
        )
        with open(moban_file_path, "w") as f:
            dump_yaml(moban_file, f)
        utils.color_print(
            f"\u2713 [info]{moban_file_path}[/info]! l"
            + "inks your project with the template."
        )
