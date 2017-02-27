import os
import yaml
from jinja2 import Environment, FileSystemLoader
import shutil


padding = "A: "


def get_user_inputs(questions):
    answers = {}
    for q in questions:
        for key, question in q.items():
            if isinstance(question, list):
                q, additional = raise_complex_question(question)
                answers[key] = q
                if additional:
                    answers.update(additional)
            else:
                a = raw_input(question + ' ' + padding)
                answers[key] = a
    return answers


def raise_complex_question(question):
    additional_answers = None
    for subq in question:
        subquestion = subq.pop('question')
        suggested_answers = sorted(subq.keys())
        long_question = [subquestion] + suggested_answers + [padding]
        a = raw_input('\n'.join(long_question))
        for key in suggested_answers:
            if key.startswith(a) and subq[key] != 'N/A':
                additional_answers = get_user_inputs(subq[key])
        break
    return a, additional_answers


class Project:
    def __init__(self):
        layout = 'layout.yml'
        layout_file = os.path.join(get_resource_dir("templates"), layout)
        with open(layout_file, "r") as f:
            first_stage = yaml.load(f)
            self.answers = get_user_inputs(first_stage['questions'])
        self.name = self.answers['project_name']
        project_src = self.name.lower().replace('-', '_')
        template_loader = FileSystemLoader(get_resource_dir("templates"))
        self.jj2_environment = Environment(
            loader=template_loader,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True)
        template = self.jj2_environment.get_template(layout)
        renderred_content = template.render(
            project_src=project_src,
            project_name=self.name
        )
        self.directives = yaml.load(renderred_content)
        self.layout = {self.name: self.directives['layout']}
        self.layout[self.name].append(project_src)  # create project src

    def create_all_directories(self):
        make_directories(None, self.layout)

    def templating(self):
        for template in self.directives['templates']:
            for output, template_file in template.items():
                template = self.jj2_environment.get_template(template_file)
                rendered_content = template.render(**self.answers)
                save_file(os.path.join(self.name, output), rendered_content)

    def copy_static_files(self):
        for static in self.directives['static']:
            for output, source in static.items():
                static_path = get_resource_dir('static')
                copy_file(os.path.join(static_path, source),
                          os.path.join(self.name, output))


def copy_file(source, dest):
    shutil.copy(source, dest)


def save_file(filename, filecontent):
    with open(os.path.join(filename), 'w') as f:
        f.write(filecontent)


def make_directories(parent, node_dictionary):
    for key, value in node_dictionary.items():
        if parent:
            the_parent = os.path.join(parent, key)
        else:
            the_parent = key
        _mkdir(the_parent)
        for item in value:
            if isinstance(item, dict):
                make_directories(the_parent, item)
            else:
                _mkdir(os.path.join(the_parent, item))


def _mkdir(path):
    os.mkdir(path)


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path
