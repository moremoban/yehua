import os

from yehua.project import Project
from yehua.utils import get_resource_dir


def main():
    yehua_file = get_yehua_file()
    project = Project(yehua_file)
    project.create_all_directories()
    project.templating()
    project.copy_static_files()


def get_yehua_file():
    yehua_file = os.environ.get('YEHUA_FILEx', None)
    if yehua_file is None:
        if os.path.exists("yehua.yml"):
            yehua_file = os.path.abspath("yehua.yml")
        else:
            default = get_resource_dir("resources")
            yehua_file = os.path.join(default, 'yehua.yml')
    return yehua_file
