import sys
import shutil
from filecmp import dircmp

import yehua.project
from yehua.main import main

from mock import patch


@patch.object(yehua.project.Project, "post_moban")
@patch("yehua.project.get_user_inputs")
def test_reference_pypi_package(fake_inputs, fake_post_moban):
    project_name = "project_yehua"
    fake_inputs.return_value = {
        "project_name": project_name,
        "description": "description",
        "license": "mit",
        "author": "author",
        "contact": "contact",
        "organisation": "github",
        "company": "copyright",
        "project_type": "command line interface",
        "cli": "cli",
    }
    with patch.object(sys, "argv", ["yh"]):
        main()

    c = dircmp("project_yehua", "tests/fixtures/project_yehua")
    assert len(c.diff_files) == 0, "\n".join(c.diff_files)
    shutil.rmtree("project_yehua")
