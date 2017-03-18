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
    f = get_yehua_file()
    print(f)
    project = Project(get_yehua_file())
    project.create_all_directories()
    calls = mkdir.call_args_list
    calls = [str(call) for call in calls]
    assert calls == [
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


@patch('yehua.project.save_file')
@patch('yehua.project.get_user_inputs')
def test_project_templating(inputs, save_file):
    save_file.return_value = 0
    inputs.return_value = dict(
        project_name='test-me'
    )
    project = Project(get_yehua_file())
    project.templating()
    calls = save_file.call_args_list
    calls = [str(call) for call in calls]
    assert calls == [
        'call(\'test-me/test-me.yml\', u\'overrides: "pyexcel.yaml"\\nname: ""\\nnick_name: ""\\nversion: "0.0.1"\\nrelease: "0.0.1"\\ndependencies:\\n  - example_lib>=0.4.4\\ndescription: ""\')',
        'call(\'test-me/.moban.yml\', u\'configuration:\\n  configuration_dir: "commons/config"\\n  template_dir:\\n  - "commons/templates"\\n  - ".moban.d"\\n  configuration: test-me.yml\\ntargets:\\n  - README.rst: README.rst\\n  - setup.py: setup.py\\n  - requirements.txt: requirements.txt\\n  - LICENSE: LICENSE.jj2\\n  - MANIFEST.in: MANIFEST.in.jj2\\n  - "tests/requirements.txt": "tests/requirements.txt"\\n  - test.sh: test.sh.jj2\\n  - test.bat: test.sh.jj2\\n  - .travis.yml: travis.yml.jj2\\n  - .gitignore: .gitignore.jj2\\n\')'
    ]


@patch('yehua.project.copy_file')
@patch('yehua.project.get_user_inputs')
def test_project_copy_static(inputs, copy_file):
    copy_file.return_value = 0
    inputs.return_value = dict(
        project_name='test-me'
    )
    project = Project(get_yehua_file())
    project.copy_static_files()
    calls = copy_file.call_args_list
    calls = [str(call) for call in calls]
    expected = [
        "call('%s/yehua/resources/./static/README.rst', 'test-me/.moban.d/README.rst')",
        "call('%s/yehua/resources/./static/test.bat', 'test-me/.moban.d/test.bat')",
        "call('%s/yehua/resources/./static/test.sh', 'test-me/.moban.d/test.sh')",
        "call('%s/yehua/resources/./static/requirements.txt', 'test-me/.moban.d/requirements.txt')",
        "call('%s/yehua/resources/./static/setup.py.jj2', 'test-me/.moban.d/setup.py')",
        "call('%s/yehua/resources/./static/tests/requirements.txt', 'test-me/.moban.d/tests/requirements.txt')",
        "call('%s/yehua/resources/./static/docs/source/conf.py.jj2', 'test-me/.moban.d/docs/source/conf.py')",
        "call('%s/yehua/resources/./static/Makefile', 'test-me/Makefile')",
        "call('%s/yehua/resources/./static/CHANGELOG.rst', 'test-me/CHANGELOG.rst')",
        "call('%s/yehua/resources/./static/__init__.py.jj2', 'test-me/test_me/__init__.py')"
    ]
    expected = [call % os.getcwd() for call in expected]
    eq_(calls, expected)
