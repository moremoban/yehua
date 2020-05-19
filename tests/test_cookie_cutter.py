import os
import sys
import shutil

from yehua.main import main
from moban.externals.file_system import is_dir, url_join, read_unicode

import fs
from mock import patch
from nose.tools import eq_


@patch("yehua.cookiecutter.get_user_inputs")
def test_local_cookie_cutter_package(fake_inputs):
    project_name = "my_test"
    file_name = "yehua_test"
    fake_inputs.return_value = {
        "directory_name": project_name,
        "file_name": file_name,
        "greeting_recipient": "yehua",
    }

    path = os.path.join("docs", "source", "hello_cookie_cutter")
    with patch.object(sys, "argv", ["yh", path]):
        main()

    with open(os.path.join(project_name, f"{file_name}.py")) as f:
        content = f.read()

    assert content == 'print("Hello, yehua!")\n'
    os.unlink(os.path.join(project_name, f"{file_name}.py"))
    os.unlink(os.path.join(project_name, f"{project_name}.yml"))
    os.unlink(os.path.join(project_name, ".moban.yml"))
    os.unlink(os.path.join(project_name, ".moban.hashes"))
    shutil.rmtree(project_name)


@patch("yehua.cookiecutter.get_user_inputs")
def test_github_package(fake_inputs):
    project_name = "git_package_test"
    file_name = "yehua_test"
    fake_inputs.return_value = {
        "directory_name": project_name,
        "file_name": file_name,
        "greeting_recipient": "yehua",
    }

    path = "git://github.com/moremoban/cookiecutter-helloworld.git"
    with patch.object(sys, "argv", ["yh", path]):
        main()

    with open(os.path.join(project_name, f"{file_name}.py")) as f:
        content = f.read()

    assert content == 'print("Hello, yehua!")\n'
    os.unlink(os.path.join(project_name, f"{file_name}.py"))
    os.unlink(os.path.join(project_name, f"{project_name}.yml"))
    os.unlink(os.path.join(project_name, ".moban.yml"))
    os.unlink(os.path.join(project_name, ".moban.hashes"))
    shutil.rmtree(project_name)


@patch("yehua.cookiecutter.get_user_inputs")
def test_reference_pypi_package(fake_inputs):
    project_name = "project_s"
    fake_inputs.return_value = {
        "full_name": "full_n",
        "email": "email_",
        "github_username": "github_u",
        "project_name": "project_n",
        "project_slug": "project_s",
        "project_short_description": "project_sd",
        "pypi_username": "pypi_u",
        "version": "1.0",
        "use_pytest": "y",
        "use_pypi_deployment_with_travis": "y",
        "add_pyup_badge": "y",
        "command_line_interface": "Click",
        "create_author_file": "y",
        "open_source_license": "MIT license",
    }
    path = "git://github.com/moremoban/cookiecutter-pypackage.git"
    with patch.object(sys, "argv", ["yh", path]):
        main()

    assert os.path.exists(os.path.join("project_s", ".git"))

    for a_file in find_files("project_s"):
        reference = url_join("tests/fixtures", a_file)
        if ".git" in a_file:
            continue
        if fs.path.basename(a_file) in [
            ".moban.yml",
            "HISTORY.rst",
            ".moban.hashes",
        ]:
            # no way to compare them
            continue
        r = read_unicode(reference)
        a = read_unicode(a_file)
        eq_(r, a, f"{a_file} differs")
        os.unlink(a_file)

    shutil.rmtree(project_name)


def find_files(dir):
    with fs.open_fs(dir) as the_fs:
        for a_file in the_fs.listdir("."):
            relative_path = url_join(dir, a_file)
            if is_dir(relative_path):
                a_list = find_files(relative_path)
                yield from a_list
            else:
                yield relative_path
