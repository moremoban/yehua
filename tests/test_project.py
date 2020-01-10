import os
import re
import codecs
import unittest

from yehua.main import get_yehua_file
from yehua.project import Project

from mock import patch
from nose.tools import eq_, raises


@patch("yehua.utils.mkdir")
@patch("yehua.project.get_user_inputs")
def test_project(inputs, mkdir):
    mkdir.return_value = 0
    inputs.return_value = dict(project_name="test-me")
    yehua_file = get_yehua_file()
    project = Project(yehua_file)
    project.create_all_directories()
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


@raises(Exception)
@patch("yehua.utils.mkdir")
@patch("yehua.project.get_user_inputs")
def test_existing_directory(inputs, mkdir):
    mkdir.return_value = 0
    inputs.return_value = dict(project_name="yehua")
    yehua_file = get_yehua_file()
    project = Project(yehua_file)
    project.create_all_directories()


class TestProject(unittest.TestCase):
    def setUp(self):
        self.patcher1 = patch("yehua.utils.copy_file")
        self.copy_file = self.patcher1.start()

        self.patcher2 = patch("yehua.project.get_user_inputs")
        self.inputs = self.patcher2.start()

        self.patcher3 = patch("yehua.utils.save_file")
        self.save_file = self.patcher3.start()

    def tearDown(self):
        self.patcher3.stop()
        self.patcher2.stop()
        self.patcher1.stop()

    def test_project_copy_static(self):
        self.copy_file.return_value = 0
        self.inputs.return_value = dict(project_name="test-me")
        project = Project(get_yehua_file())
        project.copy_static_files()
        calls = self.copy_file.call_args_list
        calls = [split_call_arguments(call) for call in calls]
        expected = [
            ["CUSTOM_README.rst", "test-me/.moban.d/CUSTOM_README.rst.jj2"],
            ["custom_setup.py.jj2", "test-me/.moban.d/custom_setup.py.jj2"],
            [
                "tests/custom_requirements.txt.jj2",
                "test-me/.moban.d/tests/custom_requirements.txt.jj2",
            ],
            ["CHANGELOG.rst", "test-me/CHANGELOG.rst"],
            ["setup.cfg", "test-me/setup.cfg"],
            ["azure-pipelines.yml", "test-me/azure-pipelines.yml"],
            [
                "azure/pipelines-steps-macos.yml",
                "test-me/.azure-pipelines-steps-macos.yml",
            ],
            [
                "azure/pipelines-steps.yml",
                "test-me/.azure-pipelines-steps.yml",
            ],
            [
                "pythonpublish.yml",
                "test-me/.github/workflows/pythonpublish.yml",
            ],
        ]
        basepath = os.path.join(os.getcwd(), "yehua", "resources", "static")
        expected = [
            [os.path.join(basepath, path[0]), path[1]] for path in expected
        ]
        for call, expectee in zip(calls, expected):
            eq_(call, expectee)

    def test_project_templating(self):
        def mock_save_file(filename, filecontent):
            file_to_write = os.path.join(
                "tests", "fixtures", "project_templating", filename
            )
            path = os.path.dirname(file_to_write)
            if not os.path.exists(path):
                print(path)
                os.mkdir(path)
            with open(file_to_write, "w") as f:
                f.write(filecontent)
            file_to_read = os.path.join(
                "tests", "fixtures", "project_templating", filename
            )
            with codecs.open(file_to_read, "r", encoding="utf-8") as f:
                expected = f.read()
                self.assertMultiLineEqual(filecontent, expected)

        self.inputs.return_value = dict(project_name="test-me")
        self.save_file.side_effect = mock_save_file
        project = Project(get_yehua_file())
        project.templating()


def split_call_arguments(mock_call):
    pattern = r"call\('(.*)', '(.*)'\)"
    result = re.match(pattern, str(mock_call))
    return [result.group(1), result.group(2)]


def test_get_simple_user_inputs():
    from yehua.project import get_user_inputs

    simple_questions = [{"hello": "world?"}]

    with patch("yehua.utils.yehua_input") as yehua_input:
        yehua_input.return_value = "hello"
        answers = get_user_inputs(simple_questions)
        assert answers["hello"] == "hello"


def test_get_complex_user_inputs():
    from yehua.project import get_user_inputs

    simple_questions = [
        {
            "hello": [
                {
                    "question": "Multiple choice question?",
                    "1. option 1": "N/A",
                    "2. option 2": [{"option 2": "What is your answer?"}],
                }
            ]
        }
    ]

    with patch("yehua.utils.yehua_input") as yehua_input:
        yehua_input.side_effect = ["2", "hello"]
        answers = get_user_inputs(simple_questions)
        eq_(answers["hello"], "2")
        eq_(answers["option 2"], "hello")
