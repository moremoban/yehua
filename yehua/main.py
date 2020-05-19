import sys
import signal
import logging
import argparse

from yehua.utils import get_yehua_file
from yehua.project import Project
from yehua._version import __version__
from moban.exceptions import FileNotFound
from yehua.cookiecutter import CookieCutter
from yehua.cookiecutter_to_yehua import cookiecutter_json_to_yehua_file

HELP_TEXT = (
    """
Usage: %s

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
    % __version__
)
DESCRIPTION = (
    "Make an installable, github ready, travis-ci capable "
    + "python package in 1 minute"
)
LOG = logging.getLogger(__name__)
LOG_LEVEL = [logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]


def main():
    signal.signal(signal.SIGINT, control_c_quit)
    parser = create_parser()
    options = vars(parser.parse_args())
    handle_verbose(options["verbose"])

    yehua_file = options.get("url")
    if yehua_file is None:
        yehua_file = get_yehua_file()
    try:
        if yehua_file.endswith("git") and yehua_file.startswith("https"):
            yehua_file = yehua_file.replace("https://", "git://")

        yehua = cookiecutter_json_to_yehua_file(yehua_file)
        project = CookieCutter(yehua, yehua_file)
    except FileNotFound:
        # then it is yehua file
        project = Project(yehua_file)
    project.create_all_directories()
    project.templating()
    project.copy_static_files()
    project.inflate_all_by_moban()
    project.post_moban()
    project.end()


def usage():
    print(HELP_TEXT)
    sys.exit(0)


def control_c_quit(_, __):
    print("\n")
    sys.exit(0)


def create_parser():
    parser = argparse.ArgumentParser(prog="yh", description=DESCRIPTION)
    parser.add_argument(
        "url",
        metavar="url",
        type=str,
        nargs="?",
        help="a url to yehua file or cookie_cutter",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"yehua {__version__}"
    )
    parser.add_argument(
        "-v",
        action="count",
        dest="verbose",
        default=0,
        help="show verbose, try -v, -vv, -vvv",
    )
    return parser


def handle_verbose(verbose_level):
    if verbose_level > len(LOG_LEVEL):
        verbose_level = len(LOG_LEVEL) - 1
    level = LOG_LEVEL[verbose_level]
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=level,
    )
