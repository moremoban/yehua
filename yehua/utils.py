import os
import re
import codecs
import shutil
import logging

from yehua.theme import THEME
from yehua.thirdparty import cutie

import fs
import colorful
from jinja2 import Environment
from ruamel.yaml import YAML

DEFAULT_FILE = "yehua.yml"
ENVIRONMENT_KEY = "YEHUA_FILE"
LOG = logging.getLogger(__name__)

yehua_input = input


def get_yehua_file():
    yehua_file = os.environ.get(ENVIRONMENT_KEY, None)
    if yehua_file is None:
        if os.path.exists(DEFAULT_FILE):
            yehua_file = os.path.abspath(DEFAULT_FILE)
        else:
            default = get_resource_dir("resources")
            yehua_file = os.path.join(default, DEFAULT_FILE)
    return yehua_file


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path


def make_directories(parent, node_dictionary):
    for key, value in node_dictionary.items():
        if parent:
            the_parent = os.path.join(parent, key)
        else:
            the_parent = key
        if os.path.exists(the_parent):
            raise Exception("%s exists. Please remove it." % the_parent)
        mkdir(the_parent)
        if value is None:
            continue
        for item in value:
            if isinstance(item, dict):
                make_directories(the_parent, item)
            else:
                mkdir(os.path.join(the_parent, item))


def make_project_src(project_name):
    return project_name.lower().replace("-", "_")


# The following Python depdencies are trusted to work
def copy_file(source, dest):
    shutil.copy(source, dest)


def mkdir(path):
    os.mkdir(path)


def save_file(filename, filecontent):
    with codecs.open(os.path.join(filename), "w", encoding="utf-8") as f:
        f.write(filecontent)


def load_yaml(content):
    yaml = YAML(typ="rt")
    data = yaml.load(content)
    return data


def dump_yaml(content, file_handle):
    yaml = YAML(typ="rt")
    yaml.dump(content, file_handle)


def find_project_name(parent_directory):
    with fs.open_fs(parent_directory) as the_fs:
        for a_file in the_fs.listdir("."):
            project_name_condition = a_file.startswith("{{")
            if project_name_condition:
                return a_file


def get_user_inputs(questions):  # refactor this later
    LOG.debug(questions)
    answers = {}
    env = Environment()
    colorful.update_palette({"peach": "#f47983"})
    for q in questions:
        for key, question in q.items():
            if isinstance(question, list):
                q, additional = raise_complex_question(question)
                answers[key] = q
                if additional:
                    answers.update(additional)
            else:
                if "{{" in question:
                    # {"foo": "foo [{{yehua.hello}}]"},
                    # {"bar": "bar [{{cookiecutter.hello}}]"}
                    template = env.from_string(question)
                    question = template.render(
                        cookiecutter=answers, **answers
                    )

                match = re.match(r"(.*)\[(.*)\].*", question)
                if match:
                    q, default_answer = match.group(1), match.group(2)
                    decorated_question = (
                        f"{q}[{colorful.peach(default_answer)}]: "
                    )
                    if default_answer in ["y", "n"]:
                        decorated_question = (
                            q + f"[{colorful.peach(default_answer)}]"
                        )
                        a = cutie.prompt_yes_or_no(
                            decorated_question,
                            default_is_yes=default_answer == "y",
                            deselected_prefix="  ",
                            selected_prefix=colorful.bold_peach("\u27a4 "),
                            char_prompt=False,
                        )
                        if a is None:
                            raise Exception()

                    else:
                        a = yehua_input(decorated_question)
                else:
                    decorated_question = question
                    a = yehua_input(decorated_question)
                if not a:
                    match = re.match(r".*\[(.*)\].*", question)
                    if match:
                        a = match.group(1)
                answers[key] = a
    LOG.debug(answers)
    return answers


def raise_complex_question(question):
    additional_answers = None
    for subq in question:
        question = subq.pop("question")
        suggested_answers = sorted(subq.keys())
        full_question = [question] + suggested_answers
        a = cutie.select(
            full_question,
            caption_indices=[0],
            selected_index=1,
            deselected_prefix="[ ] ",
            selected_prefix=(
                colorful.bold_white("[")
                + colorful.bold_peach("\u2713")
                + colorful.bold_white("] ")
            ),
        )
        if a is None:
            raise Exception()
        for key in suggested_answers:
            if key.startswith(str(a)):
                string_answer = key.split(".")[1].strip()
                if subq[key] != "N/A":
                    additional_answers = get_user_inputs(subq[key])
                break
    return string_answer, additional_answers


def color_print(rich_text):
    from rich.theme import Theme
    from rich.console import Console

    theme = Theme(THEME)
    console = Console(theme=theme)
    console.print(rich_text)
