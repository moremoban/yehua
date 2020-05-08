import os
import sys

from yehua.main import main

from mock import patch


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
    os.unlink(os.path.join(project_name, "my_test.yml"))
    os.unlink(os.path.join(project_name, ".moban.yml"))
    os.unlink(os.path.join(project_name, ".moban.hashes"))
    os.rmdir(project_name)


@patch("yehua.cookiecutter.get_user_inputs")
def test_github_package(fake_inputs):
    project_name = "my_test"
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
    os.unlink(os.path.join(project_name, "my_test.yml"))
    os.unlink(os.path.join(project_name, ".moban.yml"))
    os.unlink(os.path.join(project_name, ".moban.hashes"))
    os.rmdir(project_name)
