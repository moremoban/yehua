================================================================================
yehua - Project template tool for an organisation
================================================================================

.. image:: https://api.travis-ci.org/moremoban/yehua.svg
   :target: http://travis-ci.org/moremoban/yehua

.. image:: https://codecov.io/github/moremoban/yehua/coverage.png
   :target: https://codecov.io/github/moremoban/yehua
.. image:: https://badge.fury.io/py/yehua.svg
   :target: https://pypi.org/project/yehua

.. image:: https://pepy.tech/badge/yehua/month
   :target: https://pepy.tech/project/yehua/month

.. image:: https://img.shields.io/github/stars/moremoban/yehua.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/yehua/stargazers

.. image:: https://readthedocs.org/projects/yehua/badge/?version=latest
   :target: http://yehua.readthedocs.org/en/latest/

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/chfw

.. image:: https://badges.gitter.im/chfw_yehua/Lobby.svg
   :alt: Join the chat at https://gitter.im/chfw_yehua/Lobby
   :target: https://gitter.im/chfw_yehua/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


Introduction
================================================================================


.. image:: https://github.com/moremoban/yehua/raw/dev/yehua-usage.gif
   :width: 600px

**yehua** /'jɛhwa/ is yet another a project template tool for an organisation. It creates a project skeleton, S
from the default project template, T,  of an organisation. `moban`_, the other
tool of moremoban organisation, keeps S in synchronisation with T forever. This
use case is what we called: **continuous templating**.

.. image:: https://github.com/moremoban/yehua/raw/dev/docs/source/_static/yehua-story.png
   :width: 600px

Cookiecutter users
--------------------------

Yes, we now support cookiecutter templates. It has been requested since 2018
Europython. Simply there is tons of cookiecutter templates out there.


.. image:: https://github.com/moremoban/yehua/raw/dev/docs/source/_static/yehua-cookiecutter.gif
   :width: 600px

What you do is to replace 'cookiecutter' with 'yh'::

    $ yh git://github.com/audreyr/cookiecutter-pypackage.git

And what moremoban promise is, whenever your source template changes, you
can `synchronize` them any time with another moremoban's command 'moban'::

    $ moban

Yes, you need a separate command, which replaces your effort to synchronize
the upstream templates all the time.

What's different with Yehua
------------------------------------

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

2. we split the tool and the templates, serving the previous statement.
   People can create npm package template and use yehua+moban for continuous templating.
   Here are a list of examples:

* `pypkg-mobans in pyecharts project <https://github.com/pyecharts/pypkg-mobans>`_
* `echarts-js-mobans in echarts-map project <https://github.com/echarts-maps/echarts-js-mobans>`_

.. _moban: https://github.com/moremoban/moban
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _PyScaffold: https://github.com/pyscaffold/pyscaffold
.. _pypi-mobans: https://github.com/moremobans/pypi-mobans
.. _an example: https://github.com/moremoban/yehua/blob/dev/.github/workflows/moban-update.yml



Installation
================================================================================


You can install yehua via pip:

.. code-block:: bash

    $ pip install yehua


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/yehua.git
    $ cd yehua
    $ python setup.py install


For offline usage, you need to get `pypi-mobans-pkg` installed::

    $ pip install yehua[pypi-mobans]


or::

    $ pip install pypi-mobans-pkg


Usage
================================================================================



Simply type in and you are taken care of::

    $ yh

It will do these for you:

#. Consult you on your project static information which can update as
   many as you want to.
#. Create the Python package folder structure
#. Initialize the package as git project

You will simply need to commit it after you will have reviewed the
generated files.

Tutorial
-----------------

Let's make a python command line utility using `yehua`. The command
will be `hello` and it prints `world`. 

Step 1 Let's launch yehua
******************************
|slide1|

Step 2 Fill-in the meta data for your project
***********************************************
|slide2|

At the end, yehua generates a folder named 'hello', which contains [all necessary
files](https://github.com/moremoban/pypi-mobans).

Step 3 Start coding
*************************

.. image:: https://github.com/moremoban/yehua/raw/dev/docs/source/_static/yehua-hello.gif
   :width: 600px


In above animation, we write up the actual code in hello/main.py

.. code:: python

    def main():
        print('world')

Why is it enough? yehua generates a command utility python and
it has pre-wired to invoke hello.main.main() function. You
can find it out in setup.py.

Step 4 Install it
*********************
Now all is done. Let's install it

|slide7|

You can now run `hello` at your command line. 

Step 5 push to github
***************************

Suppose you are happy with everything. Please do the following to
push it to your github::

    $ git commit -am ":sparkle: initial commit"

Then create your project repository in github and do these to push it out::

    $ git remote add origin https://github.com/moremoban/hello.git
    $ git push origin master

You can find the `hello project`_ on github.

Step 7 enable travis
***************************

The generated project already has `.travis.yml` file. What you
will need to do is to register with travis.org if you have not
done so. And then go to travis and activate your project. 


.. |slide1| image:: docs/source/_static/yehua-0.png
   :scale: 100%
.. |slide2| image:: docs/source/_static/yehua-1.png
   :scale: 100%
.. |slide3| image:: docs/source/_static/yehua-2.png
   :scale: 100%
.. |slide4| image:: docs/source/_static/yehua-3.png
   :scale: 100%
.. |slide5| image:: docs/source/_static/yehua-4.png
   :scale: 100%
.. |slide6| image:: docs/source/_static/yehua-5.png
   :scale: 100%
.. |slide7| image:: docs/source/_static/yehua-7.png
   :scale: 100%
.. |slide9| image:: docs/source/_static/github.png
   :scale: 60%
.. |slide10| image:: docs/source/_static/push2github.png
   :scale: 60%

.. _hello project: https://github.com/moremoban/hello
.. _pyexcel commons: https://github.com/pyexcel/pyexcel-commons
.. _pyexcel: https://github.com/pyexcel
.. _moban: https://github.com/moremoban/moban
.. _setupmobans: https://github.com/moremoban/setupmobans


Background
================================================================================

The original problem I was trying to solve is: I would like to place
common paragraphs in the documentation of my projects in a central
place (pyexcel-mobans), and all projects could reference it dynamically
so that when those common paragraphs get updated, the updates can be
easily propagated to all relevant projects. The derived problem is:
what can I do to a new project? I found myself doing a lot of
copy-and-paste a lot, which lead to the creation of "yehua". Later,
John Vandenberg, an active member of coala, suggested extracting the
generic sets of pyexcel-mobans to form pypi-mobans, so that
a vanilla python package can be created. Why not cookiecutter?
Well, I have not heard of it at the time of creation. But it turns out
that this project started to pave the way to be the cookiecutter
for organisations.

Why to choose "yehua"? Here is `the little story`_ behind the
choice of name. And this `music video`_ would help bridge the
cultural gap between you and me.

.. _the little story: https://github.com/moremoban/yehua/issues/5#issuecomment-317218010
.. _music video: https://www.youtube.com/watch?v=_JFTOQ6F1-M&frags=pl%2Cwn




License
================================================================================

NEW BSD License


It embeds MIT licensed `cutie <https://github.com/kamik423/cutie>`_ from
Hans Schülein. Please refer to LICENSE file for more details
