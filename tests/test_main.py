import os
import sys

from yehua.main import HELP_TEXT, main, control_c_quit, get_yehua_file

from six import StringIO
from mock import patch
from nose.tools import eq_, raises


@patch("os.system")
@patch("yehua.project.get_user_inputs")
@patch("yehua.utils.mkdir")
@patch("yehua.utils.save_file")
@patch("yehua.utils.copy_file")
def test_main(copy, save, mkdir, inputs, os_system):
    copy.return_value = 0
    save.return_value = 0
    mkdir.return_value = 0
    inputs.return_value = dict(project_name="test-me")
    main()
    calls = mkdir.call_args_list
    calls = [str(call) for call in calls]
    expected = [
        "call('test-me')",
        "call('test-me/test_me')",
        "call('test-me/tests')",
        "call('test-me/docs')",
        "call('test-me/docs/source')",
        "call('test-me/.moban.d')",
        "call('test-me/.moban.d/tests')",
        "call('test-me/.moban.d/docs')",
        "call('test-me/.moban.d/docs/source')",
    ]
    eq_(calls, expected)


@raises(SystemExit)
def test_main_help():
    args = ["yehua", "help"]
    with patch("sys.stdout", new_callable=StringIO) as out:
        with patch.object(sys, "argv", args):
            main()
            eq_(out.getvalue(), HELP_TEXT)


@raises(SystemExit)
def test_main_dash_dash_help():
    args = ["yehua", "--help"]
    with patch("sys.stdout", new_callable=StringIO) as out:
        with patch.object(sys, "argv", args):
            main()
            eq_(out.getvalue(), HELP_TEXT)


@raises(SystemExit)
def test_main_dash_h():
    args = ["yehua", "-h"]
    with patch("sys.stdout", new_callable=StringIO) as out:
        with patch.object(sys, "argv", args):
            main()
            eq_(out.getvalue(), HELP_TEXT)


def test_yehua_file_passed_in_command_line():
    args = ["yehua", "/tmp/yehua.yml"]
    with patch("yehua.main.Project") as mocked_project:
        with patch.object(sys, "argv", args):
            main()
            mocked_project.assert_called()


@raises(Exception)
def test_a_directory_is_passed_in_command_line():
    args = ["yehua", "/"]
    with patch.object(sys, "argv", args):
        main()


def test_get_yehua_file_1():
    file_name = "testme"
    os.environ["YEHUA_FILE"] = file_name
    yehua_file = get_yehua_file()
    eq_(file_name, yehua_file)
    os.environ.pop("YEHUA_FILE")


def test_get_yehua_file_2():
    with open("yehua.yml", "w") as f:
        f.write("test")
    yehua_file = get_yehua_file()
    eq_(os.path.abspath("yehua.yml"), yehua_file)
    os.unlink("yehua.yml")


def test_get_yehua_file_3():
    default_yehua_file = os.path.join("yehua", "resources", "yehua.yml")
    yehua_file = get_yehua_file()
    eq_(os.path.abspath(default_yehua_file), yehua_file)


@raises(SystemExit)
def test_contrl_c_quit():
    control_c_quit("not", "used")
