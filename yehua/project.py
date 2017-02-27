import os
import yaml
from jinja2 import Environment, FileSystemLoader
import shutil


class Project:
    def __init__(self, name):
        self.name = name
        project_src = name.lower().replace('-', '_')
        layout = 'layout.yml'
        template_loader = FileSystemLoader(get_resource_dir("templates"))
        self.jj2_environment = Environment(
            loader=template_loader,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True)
        template = self.jj2_environment.get_template(layout)
        renderred_content = template.render(
            project_src=project_src,
            project_name=name
        )
        self.directives = yaml.load(renderred_content)
        print self.directives
        self.layout = {name: self.directives['layout']}
        self.layout[name].append(project_src) # create project src

    def create_all_directories(self):
        make_directories(None, self.layout)

    def templating(self, data):
        for template  in self.directives['templates']:
            for output, template_file in template.items():
                template = self.jj2_environment.get_template(template_file)
                with open(os.path.join(self.name, output), 'w') as f:
                    rendered_content = template.render(**data)
                    f.write(rendered_content)

    def copy_static_files(self):
        for static in self.directives['static']:
            for output, source in static.items():
                static_path = get_resource_dir('static')
                shutil.copy(os.path.join(static_path, source),
                            os.path.join(self.name, output))


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