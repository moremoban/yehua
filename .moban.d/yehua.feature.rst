
* Are you tired of writing up setup.py files by hand? Have you ever wondered why
  pypi displays raw rst file for your README?
* When you add a new library to the collection of your organization, how would
  you make sure the static information are the same as others?
* How would you update static information across all packages of your
  organisation? For example, one line change in your company's profile.
  Copy and paste? If yes, you still live in 20th century.

**yehua** is {{description|lower}} The name is the pinyin of the Chinese word
“夜华”, /'jɛhwa/. It create a blank python package that is usable and ready to push to github. And future
updates on your organisation's specific static information can be instantly applies the
update accurately using `moban`_. Here is a list of features:

#. core python package
#. test configuration setup
#. ready to commit github repository
#. automated upload to pypi through twine
#. version management through jinja2
#. automated github release through gease
#. permanent parent-child bond: keep your packages in synchronization with your template forever

What's more, you can provide your own python package templates and your own
yehua file to customize **yehua** to meet your own needs. Here are a list of
examples:

* `pypkg-mobans in pyecharts project <https://github.com/pyecharts/pypkg-mobans>`_
* `echarts-js-mobans in echarts-map project <https://github.com/echarts-maps/echarts-js-mobans>`_


Feature comparision
--------------------------------------------------------------------------------

The following table is a personal feature comparision. If you have a different
opinion, especially you are the author of the following repository, please
raise an issue and we can talk. This table is not a commerical sales pitch.

#. Y: have such a feature
#. M: manual operation
#. A: automatic operation

.. table:: Detailed feature comparision

    ============== ========================== ======================= ===================== ========== =====
    Group          Feature                    cookiecutter-pypackage  cookiecutter-vanguard PyScaffold yehua
    ============== ========================== ======================= ===================== ========== =====
    essential      setup.py                   Y                        Y                     Y         Y
    .              setup.cfg                  Y                        Y                     Y         Y
    .              source code stub           Y                        Y                     Y         Y
    test setup     requirements.txt                                    Y                     Y         Y
    .              requirements_dev.txt       Y                        Y                               Y
    .              Makefile                   Y                                                        Y
    .              tests code                 Y                        Y                     Y
    .              tox                        Y                                              Y
    .              travis                     Y                                              Y         Y
    .              test coverage                                       Y                               Y
    .              flake8                                                                              Y
    documentation  README.rst                 Y                                              Y         Y
    .              labels                                                                              Y
    .              gitignore                  Y                                              Y         Y
    .              AUTHORS.rst                Y                        Y                     Y
    .              CONTRIBUTING.rst           Y                        Y
    .              HISTORY.rst/CHANGELOG .rst Y                        Y                     Y         Y
    .              LICENCE                    Y                        Y                     Y         Y
    .              MANIFEST.in                Y                        Y                               Y
    .              sphinx docs                Y                        Y                     Y         Y
    usability      interactive shell          Y                        Y                               Y
    .              one liner                                                                 Y
    .              initialize github repo                                                              Y
    maintenance    publish on pypi            A                        M                               M
    .              dependency management      M                                              M         A
    .              template customization                                                              Y
    .              version management         M                                              M         A
    .              automated github release                                                            Y
    .              continous templating                                                                Y
    ============== ========================== ======================= ===================== ========== =====


Comparing with cookiecutter, the difference comes in the later phase
of the created project. **moremoban** organisation assumes
the life time responsibility: keep its template always
up-to-date with its originating template, for the created project.
Whereas, the templates of cookiecutter are disconnected once
the project has been created successfully. In my personal experience
(maintaining pyexcel), I am finding that the documentation
changes as well. For example, someone helped to correct my spellings
in one of my project's documentation. Via moremoban's toolset, I can
upstream the spelling updates to pyexcel-mobans and propagate all
the spellings to the rest of the projects.

Comparing with PyScaffold, the first difference is the difference in
command line interface. Yehua prefers interactivity whereas PyScaffold
uses one liner. Why? I am influenced by yeoman, the scaffolding tool
for front end developers. I am convinced that conversational style
does lower the entry barrier for new comers, because the question on
the left hand side is a self-explantory sentence so the user does
not need to read up the user manual. The second difference is that
Yehua has an interface layer(YEHUA_FILE) which cuts its ties with its own
built-in templates, which means you instruct yehua to make a npm package
if your custom YEHUA_FILE instructs. That's an extreme. The third difference
is that its own templates(I called it mobans) can be overriden/customized
by another set of templates/mobans. For example, pyexcel project has
pyexcel-mobans, which overlays on top of pypi-mobans. pyexcel-mobans
is more concerned of pyexcel project's documentation.
