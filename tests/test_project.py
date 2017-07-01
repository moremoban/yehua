# flake8: noqa

import os
import re
from mock import patch
from yehua.project import Project
from nose.tools import eq_
from yehua.main import get_yehua_file


@patch('yehua.utils.mkdir')
@patch('yehua.project.get_user_inputs')
def test_project(inputs, mkdir):
    mkdir.return_value = 0
    inputs.return_value = dict(
        project_name='test-me'
    )
    project = Project(get_yehua_file())
    project.create_all_directories()
    calls = mkdir.call_args_list
    calls = [str(call) for call in calls]
    expected = [
        "call('test-me')",
        "call('test-me/tests')",
        "call('test-me/docs')",
        "call('test-me/docs/source')",
        "call('test-me/.moban.d')",
        "call('test-me/.moban.d/tests')",
        "call('test-me/.moban.d/docs')",
        "call('test-me/.moban.d/docs/source')",
        "call('test-me/test_me')"
    ]
    eq_(calls, expected)


@patch('yehua.utils.save_file')
@patch('yehua.project.get_user_inputs')
def test_project_templating(inputs, save_file):

    def mock_save_file(filename, filecontent):
        #file_to_write = os.path.join(
        #    "tests", "fixtures",
        #    "project_templating", filename)
        #path = os.path.dirname(file_to_write)
        #if not os.path.exists(path):
        #    print(path)
        #    os.mkdir(path)
        #with open(file_to_write, 'w') as f:
        #    f.write(filecontent)
        file_to_read = os.path.join(
            "tests",
            "fixtures",
            "project_templating",
            filename)
        with open(file_to_read, 'r') as f:
            expected = f.read()
            eq_(filecontent, expected)

    inputs.return_value = dict(
        project_name='test-me'
    )
    save_file.side_effect = mock_save_file
    project = Project(get_yehua_file())
    project.templating()


@patch('yehua.utils.copy_file')
@patch('yehua.project.get_user_inputs')
def test_project_copy_static(inputs, copy_file):
    copy_file.return_value = 0
    inputs.return_value = dict(
        project_name='test-me'
    )
    project = Project(get_yehua_file())
    project.copy_static_files()
    calls = copy_file.call_args_list
    calls = [split_call_arguments(call) for call in calls]
    expected = [
        ["README.rst", "test-me/.moban.d/README.rst.jj2"],
        ["test.sh", "test-me/.moban.d/test.sh.jj2"],
        ["requirements.txt", "test-me/.moban.d/requirements.txt.jj2"],
        ["setup.py.jj2", "test-me/.moban.d/setup.py.jj2"],
        ["tests/requirements.txt", "test-me/.moban.d/tests/requirements.txt.jj2"],
        ["docs/source/conf.py.jj2", "test-me/.moban.d/docs/source/conf.py.jj2"],
        ["Makefile", "test-me/Makefile"],
        ["CHANGELOG.rst", "test-me/CHANGELOG.rst"],
        ["MANIFEST.in", "test-me/MANIFEST.in"],
        ["travis.yml.jj2", "test-me/.travis.yml"],
        ["gitignore", "test-me/.gitignore"],
        ["__init__.py.jj2", "test-me/test_me/__init__.py"]
    ]
    basepath = os.path.join(os.getcwd(), 'yehua', 'resources', 'static')
    expected = [[ os.path.join(basepath, path[0]), path[1]] for path in expected]
    eq_(calls, expected)


def split_call_arguments(mock_call):
    pattern = "call\('(.*)', '(.*)'\)"
    result = re.match(pattern, str(mock_call))
    return [result.group(1), result.group(2)]


def test_get_simple_user_inputs():
    from yehua.project import get_user_inputs
    
    simple_questions = [
            {
                "hello": "world?"
            }
    ]

    with patch("yehua.utils.yehua_input") as yehua_input:
        yehua_input.return_value = "hello"
        answers = get_user_inputs(simple_questions)
        assert answers["hello"] == "hello"


def test_get_complex_user_inputs():
    from yehua.project import get_user_inputs
    
    simple_questions = [
            {
                "hello": [{
                    "question": "Multiple choice question?",
                    "1. option 1": "N/A",
                    "2. option 2": [{
                        "option 2": "What is your answer?"
                    }]
                }]
            }
    ]

    with patch("yehua.utils.yehua_input") as yehua_input:
        yehua_input.side_effect = [ "2", "hello" ]
        answers = get_user_inputs(simple_questions)
        eq_(answers["hello"], "2")
        eq_(answers["option 2"], "hello")
