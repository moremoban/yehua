

================================================================================
yehua - Let you focus on code, instead of setup scaffolding
================================================================================

.. image:: https://api.travis-ci.org/chfw/yehua.svg?branch=master
   :target: http://travis-ci.org/chfw/yehua

.. image:: https://codecov.io/gh/chfw/yehua/coverage.png
    :target: https://codecov.io/gh/chfw/yehua

.. image:: https://readthedocs.org/projects/yehua/badge/?version=latest
   :target: http://yehua.readthedocs.org/en/latest/

.. image:: https://badges.gitter.im/chfw_yehua/Lobby.svg
   :alt: Join the chat at https://gitter.im/chfw_yehua/Lobby
   :target: https://gitter.im/chfw_yehua/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


Installation
================================================================================

You can install it via pip:

.. code-block:: bash

    $ pip install yehua


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/chfw/yehua.git
    $ cd yehua
    $ python setup.py install

Usage
================================================================================



.. image:: https://github.com/chfw/yehua/raw/master/yehua-usage.gif
   :width: 600px

Simply type in ::

    $ yehua

And then go into the generate project folder::

    $ moban

Tutorial
-----------------

Let's make a python command line utility using `yehua`. The command
will be `hello` and it prints `world`. You will need to issue::

    $ pip install yehua moban

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

Run moban. It inflates the all meta data.

|slide4|

Why is moban involved here? It helps reduce duplicated meta data when
your project grows. For example, yehua had this tutorial in README and in sphinx
documentation. I wrote it in one file and moban copies it to both
places. What's more, it helps further when the number of your
project grows. For example, `pyexcel` project has dozens of
sub projects. I wrote most of the generic documentation in
`pyexcel-commons`_ and moban copies them across all sub projects.

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


|slide9|

|slide10|


You can find the `hello project`_ on github.

Step 8 enable travis
***************************

The generated project already has `.travis.yml` file. What you
will need to do is to register with travis.org if you have not
done so. And then go to travis and activate your project. 


.. |slide1| image:: _static/yehua-0.png
   :scale: 100%
.. |slide2| image:: _static/yehua-1.png
   :scale: 100%
.. |slide3| image:: _static/yehua-2.png
   :scale: 100%
.. |slide4| image:: _static/yehua-3.png
   :scale: 100%
.. |slide5| image:: _static/yehua-4.png
   :scale: 100%
.. |slide6| image:: _static/yehua-5.png
   :scale: 100%
.. |slide7| image:: _static/yehua-6.png
   :scale: 100%
.. |slide8| image:: _static/yehua-7.png
   :scale: 100%
.. |slide9| image:: _static/github.png
   :scale: 60%
.. |slide10| image:: _static/push2github.png
   :scale: 60%

.. _hello project: https://github.com/chfw/hello
.. _pyexcel commons: https://github.com/pyexcel/pyexcel-commons

