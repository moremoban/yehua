import json
from io import StringIO

from yehua.utils import dump_yaml, find_project_name
from moban.externals.file_system import is_dir, url_join, read_unicode

import fs

INTRODUCTION = """
[info]Yehua /'jɛhwa/[/info] will walk you through cookiecutter template wizard
Press ^C to quit at any time.

"""


def cookiecutter_json_to_yehua_file(path):
    content = read_unicode(url_join(path, "cookiecutter.json"))
    cookie_questions = json.loads(content)

    questions = []
    for key, value in cookie_questions.items():
        if isinstance(value, list):
            complex_question = {"question": f"{key}:"}
            for index, option in enumerate(value, 1):
                complex_question[f"{index}. {option}"] = "N/A"
            questions.append({key: [complex_question]})
        else:
            questions.append({key: f"{key} [{value}]: "})
    project_dir = find_project_name(path)
    dir_list = walk_tree(url_join(path, project_dir))
    better_list = cleanse(dir_list, url_join(path, project_dir))
    layout = find_sub_directories(url_join(path, project_dir))

    git_repo_files = []
    for entry in better_list:
        git_repo_files += list(entry.keys())
    git_repo_files += [".moban.yml", cookiefy(project_dir + ".yml")]
    yehua = {
        "introduction": INTRODUCTION,
        "configuration": {
            "template_path": project_dir,
            "static_path": project_dir,
        },
        "post-moban": {"git-repo-files": git_repo_files},
        "questions": questions,
        "moban": better_list,
        "layout": layout,
    }
    yaml_content = StringIO()
    dump_yaml(yehua, yaml_content)
    return yaml_content.getvalue()


def walk_tree(parent_directory):
    dir_list = []
    p = fs.open_fs(parent_directory)
    for a_file in p.listdir("."):
        relative_path = url_join(parent_directory, a_file)
        if is_dir(relative_path):
            a_list = walk_tree(relative_path)
            dir_list.append(a_list)
        else:
            dir_list.append(relative_path)
    return dir_list


def find_sub_directories(parent_directory):
    dir_list = []
    p = fs.open_fs(parent_directory)
    for a_file in p.listdir("."):
        relative_path = url_join(parent_directory, a_file)
        if is_dir(relative_path):
            a_list = find_sub_directories(relative_path)
            key = cookiefy(a_file)
            if a_list:
                dir_list.append({key: a_list})
            else:
                dir_list.append(key)
    return dir_list


def cleanse(tree, base):
    better = []
    for item in tree:
        if isinstance(item, list):
            a_list = cleanse(item, base)
            if a_list:
                better = better + a_list
        else:
            good = item.replace(base, "")[1:]
            key = cookiefy(good)
            better.append({key: good})
    return better


def cookiefy(item):
    if "{{" in item:
        return item.replace("{{", "<cookiecutter<").replace(
            "}}", ">cookiecutter>"
        )
    else:
        return item
