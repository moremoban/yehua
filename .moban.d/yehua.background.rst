The original problem I was trying to solve is: I would like to place
common paragraphs in the documentation of my projects in a central
place (pyexcel-mobans), and all projects could reference it dynamically
so that when those common paragraphs get updated, the updates can be
easily propagated to all relevant projects. The derived problem is:
what could I do to a new project? I found myself doing a lot of
copy-and-paste a lot, which lead to the creation of "yehua". Later,
John Vandenberg, an active member of coala, suggested extracting the
generic sets of pyexcel-mobans to form pypi-mobans, so that
a vanilla python package can be created.

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


Why to choose "yehua"? Here is `the little story<https://github.com/moremoban/yehua/issues/5#issuecomment-317218010>`_ behind the choice of name. And this `music video<https://www.youtube.com/watch?v=_JFTOQ6F1-M&frags=pl%2Cwn>`_ would help bridge the cultural gap between you and me.


