# flake8: noqa

import os
from mock import patch
from yehua.project import Project
from nose.tools import eq_
from yehua.main import get_yehua_file


@patch('yehua.project._mkdir')
@patch('yehua.project.get_user_inputs')
def test_project(inputs, mkdir):
    mkdir.return_value = 0
    inputs.return_value = dict(
        project_name='test-me'
    )
    project = Project(get_yehua_file())
    project.digest()
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


@patch('yehua.project.save_file')
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
    project.digest()
    project.templating()


@patch('yehua.project.copy_file')
@patch('yehua.project.get_user_inputs')
def test_project_copy_static(inputs, copy_file):
    copy_file.return_value = 0
    inputs.return_value = dict(
        project_name='test-me'
    )
    project = Project(get_yehua_file())
    project.digest()
    project.copy_static_files()
    calls = copy_file.call_args_list
    calls = [str(call) for call in calls]
    expected = [
        "call('%s/yehua/resources/./static/README.rst', 'test-me/.moban.d/README.rst.jj2')",
        "call('%s/yehua/resources/./static/test.sh', 'test-me/.moban.d/test.sh.jj2')",
        "call('%s/yehua/resources/./static/requirements.txt', 'test-me/.moban.d/requirements.txt.jj2')",
        "call('%s/yehua/resources/./static/setup.py.jj2', 'test-me/.moban.d/setup.py.jj2')",
        "call('%s/yehua/resources/./static/tests/requirements.txt', 'test-me/.moban.d/tests/requirements.txt.jj2')",
        "call('%s/yehua/resources/./static/docs/source/conf.py.jj2', 'test-me/.moban.d/docs/source/conf.py.jj2')",
        "call('%s/yehua/resources/./static/Makefile', 'test-me/Makefile')",
        "call('%s/yehua/resources/./static/CHANGELOG.rst', 'test-me/CHANGELOG.rst')",
        "call('%s/yehua/resources/./static/MANIFEST.in', 'test-me/MANIFEST.in')",
        "call('%s/yehua/resources/./static/travis.yml.jj2', 'test-me/.travis.yml')",
        "call('%s/yehua/resources/./static/gitignore', 'test-me/.gitignore')",
        "call('%s/yehua/resources/./static/__init__.py.jj2', 'test-me/test_me/__init__.py')"]
    expected = [call % os.getcwd() for call in expected]
    eq_(calls, expected)
