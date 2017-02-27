from mock import patch
from yehua.project import Project


@patch('yehua.project._mkdir')
def test_project(mkdir):
    mkdir.return_value = 0
    project = Project('test')
    project.create_all_directories()
    calls = mkdir.call_args_list
    calls = [str(call) for call in calls]
    assert calls == [
        "call('test')",
        "call('test/tests')",
        "call('test/docs')",
        "call('test/docs/source')",
        "call('test/.moban.d')",
        "call('test/.moban.d/tests')",
        "call('test/.moban.d/docs')",
        "call('test/.moban.d/docs/source')"]