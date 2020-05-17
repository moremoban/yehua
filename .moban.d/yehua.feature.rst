

.. image:: https://github.com/moremoban/yehua/raw/dev/docs/source/_static/yehua-cookiecutter.gif
   :width: 600px

**yehua** /'jɛhwa/ is {{description|lower}} It creates a project skeleton, S
from the default project template, T,  of an organisation. `moban`_, the other
tool of moremoban organisation, keeps S in synchronisation with T forever. This
use case is what we called: **continuous templating**.

When the scope is a single project, **yehua** is no different to `cookiecutter`_ and
`PyScaffold`_. It will create a project skeleton from `pypi-mobans`_, other templates such
as cookiecutter templates, yehua mobans.

When the scope is all projects within an organisation, **yehua** helps tackle
information fragmentation problem, because all new projects after its creation,
are still in synchronisation with T. For example, removing python 2.7 test
in your travis file, can be done either manually by hand or automatically via
`moban`_. What's the difference? The latter is faster and typo-free option. Here is
`an example`_.

`PyScaffold`_ version 3 has rolled out '--update' option, recognizing the organisational
need of continous templating. Why do not **yehua** join `PyScaffold`_? Well,
moremoban organisation started with '--update' at the start so our architecture
and vision are closer to that of `cookiecutter`_:

1. we do not want to limit ourselves in pythonsphere. We wanted to serve all
   IT projects. In our mind, they are all about text templating.

1. we split the tool and the templates, serving the previous statement.
   People can create npm package template and use yehua+moban for continuous templating.
   Here are a list of examples:

* `pypkg-mobans in pyecharts project <https://github.com/pyecharts/pypkg-mobans>`_
* `echarts-js-mobans in echarts-map project <https://github.com/echarts-maps/echarts-js-mobans>`_

.. _moban: https://github.com/moremoban/moban
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _PyScaffold: https://github.com/pyscaffold/pyscaffold
.. _pypi-mobans: https://github.com/moremobans/pypi-mobans
.. _an example: https://github.com/moremoban/yehua/blob/dev/.github/workflows/moban-update.yml

