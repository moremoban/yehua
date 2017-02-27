from mock import patch
from yehua.main import main


@patch('yehua.project.get_user_inputs')
@patch('yehua.project._mkdir')
@patch('yehua.project.save_file')
@patch('yehua.project.copy_file')
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
