import os
import sys
import codecs
import shutil

DEFAULT_FILE = "yehua.yml"
ENVIRONMENT_KEY = "YEHUA_FILE"
PY2 = sys.version_info[0] == 2


if PY2:
    yehua_input = raw_input  # noqa: F821
else:
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
