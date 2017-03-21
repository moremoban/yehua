import sys

from yehua.project import Project
from yehua.utils import get_yehua_file


HELP_TEXT = """
Usage:

   yehua [yehua_file/help]

where:

- yehua_file: is an instruction file for yehua to act. See documentation for
              its file specification.
- help: print this text and exit

If no argument is given, the command looks for the instruction file in the
shell environment variable "YEHUA_FILE" first, then for "yehua.yml" at
current working directory, and at last use the default "yehua.yml" in its
own package.
"""


def main():
    argument = None
    yehua_file = None
    if len(sys.argv) == 2:
        argument = sys.argv[1]
        if argument == "help":
            usage()
        else:
            yehua_file = argument
    else:
        yehua_file = get_yehua_file()
    project = Project(yehua_file)
    project.create_all_directories()
    project.templating()
    project.copy_static_files()


def usage():
    print(HELP_TEXT)
    sys.exit(0)
