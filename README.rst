================================================================================
yehua - Let you focus on code, instead of setup scaffolding
================================================================================

.. image:: https://api.travis-ci.org/moremoban/yehua.svg
   :target: http://travis-ci.org/moremoban/yehua

.. image:: https://codecov.io/github/moremoban/yehua/coverage.png
   :target: https://codecov.io/github/moremoban/yehua


.. image:: https://readthedocs.org/projects/yehua/badge/?version=latest
   :target: http://yehua.readthedocs.org/en/latest/

.. image:: https://badges.gitter.im/chfw_yehua/Lobby.svg
   :alt: Join the chat at https://gitter.im/chfw_yehua/Lobby
   :target: https://gitter.im/chfw_yehua/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Introduction
================================================================================

* Are you tired of writing up setup.py files by hand? Have you ever wondered why
  pypi displays raw rst file for your README?
* When you add a new library to the collection of your organization, how would
  you make sure the static information are the same as others?
* How would you update static information across all packages of your
  organisation? For example, one line change in your company's profile.
  Copy and paste? If yes, you still live in 20th century.

**yehua** is a command line tool to provide a default scaffolding for a python package. It create a blank python package that is
usable and ready to push to github. 

Future updates on your organisation's specific static information can be instantly applies the update accurately using `moban`_ . What's more, the python package is github and travis-ci friendly.

What's more, you can provide your own python package templates and your own
yehua file to customize **yehua** to meet your own needs.


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

Usage
================================================================================



.. image:: https://github.com/chfw/yehua/raw/master/yehua-usage.gif
   :width: 600px

Please note, since version 0.0.2, the command line is shortened. Due to
time constaints, the demo video uses `yehua` still.

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
will be `hello` and it prints `world`. You will need to issue::

    $ pip install yehua

before proceeding.

Step 1 Let's launch yehua
******************************
|slide1|

Step 2 Fill-in the meta data for your project
***********************************************
|slide2|

At the end, yehua generates a folder named 'hello', which contains all necessary
files for

#. installing it as a package
#. testing via nose
#. sharing it on github
#. configuring travis via github

Step 3 Inflates the meta data
**********************************
Let's change to 'hello' directory

|slide3|

All meta data is inflated via **`moban`_ automatically**
The templates come from `setupmobans`_
Run moban. It inflates the all meta data.

|slide4|

Why is moban involved here? It helps reduce duplicated meta data when
your project grows. For example, yehua had this tutorial in README and in sphinx
documentation. I wrote it in one file and moban copies it to both
places. What's more, it helps further when the number of your
project grows. For example, `pyexcel`_ project has dozens of
sub projects. I wrote most of the generic documentation in
`pyexcel commons`_ and moban copies them across all sub projects.

Step 4 Start coding
*************************
Let's write up the actual code in hello/main.py

|slide5|

Put in just a main() function and save it.

|slide6|

Why is it enough? yehua generates a command utility python and
it has pre-wired to invoke hello.main.main() function. You
can find it out in setup.py.

Step 5 Install it
*********************
Now all is done. Let's install it

|slide7|

Step 6 Run it
********************

Let's run it

|slide8|

All done.

Step 7 push to github
***************************

Suppose you are happy with everything. Please do the following to
push it to your github::

    $ git init
    $ git add *
    $ git add .gitignore .moban.d/ .moban.yml .travis.yml
    $ git commit -am ":sparkle: initial commit"

Then create your project repository in github and do these to push it out::

    $ git remote add origin https://github.com/chfw/hello.git
    $ git push origin master


You can find the `hello project`_ on github.

Step 8 enable travis
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
.. |slide7| image:: docs/source/_static/yehua-6.png
   :scale: 100%
.. |slide8| image:: docs/source/_static/yehua-7.png
   :scale: 100%
.. |slide9| image:: docs/source/_static/github.png
   :scale: 60%
.. |slide10| image:: docs/source/_static/push2github.png
   :scale: 60%

.. _hello project: https://github.com/chfw/hello
.. _pyexcel commons: https://github.com/pyexcel/pyexcel-commons
.. _pyexcel: https://github.com/pyexcel
.. _moban: https://github.com/moremoban/moban
.. _setupmobans: https://github.com/moremoban/setupmobans


License
================================================================================

NEW BSD License
