Change log
================================================================================

0.0.8 - 2020
--------------------------------------------------------------------------------

**Added**

#. `#30 <https://github.com/moremoban/yehua/issues/30>`_: 'yh -h' or 'yh --help'
   triggers help text
#. `#32 <https://github.com/moremoban/yehua/issues/32>`_: pypi-moban-pkg as
   installation extras
#. enable auto github auto publishing
#. generate mit license

**Updated**

#. `#35 <https://github.com/moremoban/yehua/issues/35>`_: better error message
   when the project name has been made a directory already
#. updated moban dependency to v0.6.0
#. updated yaml library to ruamel.yaml. PyYAML is out because only one yaml
   library is wanted in the organisation.

0.0.7 - 6/10/2019
--------------------------------------------------------------------------------

**Updated**

#. upgrade yehua to use pypi-mobans-pkg version 0.0.7
#. generated project will have azure build pipeline, moban command stage in
   travis and local flake8 check

0.0.6 - 04/15/2019
--------------------------------------------------------------------------------

**Updated**

#. upgrade yehua to use pypi-mobans-pkg version 0.0.5
#. generated project will have four new files: pipfile, lint.sh, changelog.yml
   and Makefile 

0.0.5 - 08/11/2018
--------------------------------------------------------------------------------

**added**

#. `#6 <https://github.com/moremoban/yehua/issues/6>`_: provide Pipfile for
   pipenv

0.0.4 - 06/07/2018
--------------------------------------------------------------------------------

**Updated**

#. `#11 <https://github.com/moremoban/yehua/issues/11>`_: keep up-to-date with
   pypi-mobans

0.0.3 - 24/02/2018
--------------------------------------------------------------------------------

**Added**

#. To add all files to a git repo is being made optional. The action is
   specified in `git-repo-files` under `post-moban` section. This particular
   need arises when it is used to scaffold other type of projects such as npm.

0.0.2 - 15/10/2017
--------------------------------------------------------------------------------

**Added**

#. Automatically inflate project meta data. One yehua command and typing a few
   questions are required before a complete project scaffolding
#. Automatically obtain setupmobans repo for previous task.
#. Automatically initialize package as git project and add all project files for
   the user to commit

**Removed**

#. Built-in template files are off-loaded to setupmobans, which are more
   frequently updated.

0.0.1 - 02/07/2017
--------------------------------------------------------------------------------
