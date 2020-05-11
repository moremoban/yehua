import os
import re
import codecs
import shutil
import logging

import fs
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
                        cookiecutter=answers, yehua=answers
                    )
                a = yehua_input(question)
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
        subquestion = subq.pop("question")
        suggested_answers = sorted(subq.keys())
        long_question = [subquestion] + suggested_answers
        choice = "Choose from %s [1]: " % (
            ",".join([str(x) for x in range(1, len(long_question))])
        )
        long_question.append(choice)
        a = yehua_input("\n".join(long_question))
        if not a:
            a = "1"
        for key in suggested_answers:
            if key.startswith(a):
                string_answer = key.split(".")[1].strip()
                if subq[key] != "N/A":
                    additional_answers = get_user_inputs(subq[key])
                break
    return string_answer, additional_answers
