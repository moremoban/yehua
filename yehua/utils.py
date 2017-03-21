import os
import shutil


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
        for item in value:
            if isinstance(item, dict):
                make_directories(the_parent, item)
            else:
                mkdir(os.path.join(the_parent, item))


def mkdir(path):
    os.mkdir(path)


def make_project_src(project_name):
    return project_name.lower().replace('-', '_')


def copy_file(source, dest):
    shutil.copy(source, dest)


def save_file(filename, filecontent):
    with open(os.path.join(filename), 'w') as f:
        f.write(filecontent)


