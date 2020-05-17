import os
import subprocess
from datetime import datetime

import yehua.utils as utils
from yehua.utils import get_user_inputs
from moban.externals.file_system import exists, is_dir, read_unicode

import fs
from jinja2 import Environment
from jinja2_fsloader import FSLoader


class Project:
    def __init__(self, yehua_file):
        if not exists(yehua_file):
            raise Exception("%s does not exist" % yehua_file)
        if is_dir(yehua_file):
            raise Exception("A yehua file is expected. Not a directory")

        self.project_file = yehua_file
        self.project_name = None
        self.answers = None
        self.name = None
        self.directives = None
        self._ask_questions()
        self._append_magic_variables()
        self._template_yehua_file()

    def create_all_directories(self):
        folder_tree = {
            self.answers["project_name"]: self.directives.get("layout", None)
        }
        utils.make_directories(None, folder_tree)

    def templating(self):
        for template in self.directives["templates"]:
            for output, template_file in template.items():
                template = self.jj2_environment.get_template(template_file)
                rendered_content = template.render(**self.answers)
                target = os.path.join(self.project_name, output)
                utils.save_file(target, rendered_content)

    def copy_static_files(self):
        if "static" not in self.directives:
            return
        for static in self.directives["static"]:
            for output, source in static.items():
                source = os.path.abspath(os.path.join(self.static_dir, source))
                dest = os.path.join(self.project_name, output)
                utils.copy_file(source, dest)

    def inflate_all_by_moban(self):
        current = os.getcwd()
        project_name = self.answers["project_name"]
        os.chdir(project_name)
        cmd = "moban"
        _run_command(cmd)
        os.chdir(current)
        utils.color_print(
            f"\u2713 Files are generated under [info]{project_name}[/info]"
        )

    def post_moban(self):
        if "post-moban" not in self.directives:
            return
        for key, value in self.directives["post-moban"].items():
            if key == "git-repo-files":
                self.initialize_git_and_add_all(value)

    def initialize_git_and_add_all(self, project_files):
        project_name = self.answers["project_name"]
        current = os.getcwd()
        os.chdir(project_name)
        cmd = "git init"
        _run_command(cmd)
        for file_name in project_files:
            _run_command(f"git add {file_name}")
        os.chdir(current)
        utils.color_print(
            f"\u2713 Git repo initialized under [info]{project_name}[/info]"
            + " and is ready to commit"
        )

    def end(self):
        utils.color_print(
            "All done!! project [info]%s[/info] is created."
            % self.project_name
        )
        utils.color_print(
            "In the future, "
            + "run [info]moban[/info] to synchronize with the project template"
        )

    def _ask_questions(self):
        content = read_unicode(self.project_file)
        first_stage = utils.load_yaml(content)
        utils.color_print(first_stage["introduction"])
        base_path = fs.path.dirname(self.project_file)
        with fs.open_fs(base_path) as the_fs:
            self.template_dir = os.path.join(
                the_fs._root_path,
                first_stage["configuration"]["template_path"],
            )
            self.static_dir = os.path.join(
                the_fs._root_path, first_stage["configuration"]["static_path"]
            )
        self.answers = get_user_inputs(first_stage["questions"])

    def _append_magic_variables(self):
        self.project_name = self.answers["project_name"]
        self.answers["now"] = datetime.utcnow()

        self.jj2_environment = self._create_jj2_environment(self.template_dir)

    def _template_yehua_file(self):
        base_path = fs.path.dirname(self.project_file)
        with fs.open_fs(base_path) as the_fs:
            base_path = the_fs._root_path
            tmp_env = self._create_jj2_environment(base_path)
            template = tmp_env.get_template(
                os.path.basename(self.project_file)
            )
            renderred_content = template.render(**self.answers)
            self.directives = utils.load_yaml(renderred_content)

    def _create_jj2_environment(self, path):
        template_loader = FSLoader(path)
        default_extensions = [
            "cookiecutter.extensions.JsonifyExtension",
            "jinja2_time.TimeExtension",
        ]
        environment = Environment(
            loader=template_loader,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
            extensions=default_extensions,
        )
        return environment


def _run_command(command):
    subprocess.check_call(
        command.split(" "),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
