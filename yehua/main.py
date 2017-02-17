import os
from jinja2 import Environment, FileSystemLoader
import shutil
from collections import OrderedDict

questions = OrderedDict(
    project="What is your project name?",
    description="What is the description?",
    type="What is project type? 1. pyexcel library 2. command line tool"
)

optional = {
    'nickname': "What is the nick name?",
    'cli': "What is the name of cli executable?",
}

padding = " A: "

answers = {
    'project': 'n/a',
    'description': 'n/a',
}

def main():
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
    
    template_loader = FileSystemLoader(get_resource_dir("templates"))
    jj2_environment = Environment(
        loader=template_loader,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True)
    
    project_name = answers['project']
    project_moban = os.path.join(project_name, '.moban.d')
    project_moban_tests = os.path.join(project_name, '.moban.d', 'tests')
    project_tests = os.path.join(project_name, 'tests')
    project_src = os.path.join(project_name, project_name.lower().replace('-', '_'))
    os.mkdir(project_name) # project name
    os.mkdir(project_moban) # project name
    os.mkdir(project_moban_tests) # project name
    os.mkdir(project_tests) # project name
    os.mkdir(project_src)
    
    template = jj2_environment.get_template('project.yml')
    with open(os.path.join(project_name, project_name + '.yml'), 'w') as f:
        rendered_content = template.render(**answers)
        f.write(rendered_content)
    
    template = jj2_environment.get_template('.moban.yml')
    with open(os.path.join(project_name, '.moban.yml'), 'w') as f:
        rendered_content = template.render(**answers)
        f.write(rendered_content)
    
    for f in ['README.rst', 'test.bat', 'test.sh', 'requirements.txt', 'setup.py', os.path.join('tests', 'requirements.txt')]:
        source = os.path.join(get_resource_dir('templates'), f)
        dest = os.path.join(project_moban, f)
        shutil.copy(source, dest)
    
    for f in ['CHANGELOG.rst', 'Makefile']:
        source = os.path.join(get_resource_dir('static'), f)
        dest = os.path.join(project_name, f)
        shutil.copy(source, dest)
    
    for f in ['__init__.py']:
        source = os.path.join(get_resource_dir('static'), f)
        dest = os.path.join(project_src, f)
        shutil.copy(source, dest)


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, '..', folder)
    return resource_path