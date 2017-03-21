import os

from mock import patch
from yehua.main import main, get_yehua_file
from nose.tools import eq_


@patch('yehua.project.get_user_inputs')
@patch('yehua.utils.mkdir')
@patch('yehua.utils.save_file')
@patch('yehua.utils.copy_file')
def test_main(copy, save, mkdir, inputs):
    copy.return_value = 0
    save.return_value = 0
    mkdir.return_value = 0
    inputs.return_value = dict(
        project_name='test-me'
    )
    main()
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


def test_get_yehua_file_1():
    file_name = "testme"
    os.environ['YEHUA_FILE'] = file_name
    yehua_file = get_yehua_file()
    eq_(file_name, yehua_file)
    os.environ.pop('YEHUA_FILE')


def test_get_yehua_file_2():
    with open('yehua.yml', 'w') as f:
        f.write('test')
    yehua_file = get_yehua_file()
    eq_(os.path.abspath('yehua.yml'), yehua_file)
    os.unlink('yehua.yml')


def test_get_yehua_file_3():
    default_yehua_file = os.path.join('yehua', 'resources', 'yehua.yml')
    yehua_file = get_yehua_file()
    eq_(os.path.abspath(default_yehua_file), yehua_file)
