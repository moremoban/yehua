import os
from collections import OrderedDict
from yehua.project import Project


questions = OrderedDict(
    project_name="What is your project name?",
    description="What is the description?",
    type="What is project type? 1. pyexcel library 2. command line tool"
)

optional = {
    'nickname': "What is the nick name?",
    'cli': "What is the name of cli executable?",
}

padding = " A: "


def main():
    answers = get_user_inputs()
    project_name = answers['project_name']
    project = Project(project_name)
    project.create_all_directories()
    project.templating(answers)
    project.copy_static_files()


def get_user_inputs():
    answers = {}
    for q in questions.keys():
        a = raw_input(questions[q] + padding)
        answers[q] = a

    if answers['type'] == '2':
        for q in ['cli']:
            a = raw_input(optional[q] + padding)
            answers[q] = a
    else:
        a = raw_input(optional['nickname'])
        answers['nickname'] = a
    return answers


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path