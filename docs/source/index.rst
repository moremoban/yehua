`yehua` - Let you focus on code, instead of setup scaffolding
================================================================================

:Author: C.W.
:Source code: http://github.com/chfw/yehua.git
:Issues: http://github.com/chfw/yehua/issues
:License: New BSD License
:Released: |version|
:Generated: |today|


Introduction
--------------------------------------------------------------------------------

* Are you tired of writing up setup.py files by hand? Have you ever wondered why
  pypi displays raw rst file for your README?
* When you add a new library to the collection of your orgnisation, how would
  you make sure the static information are the same as others?
* How would you update static information across all packages of your
  organisation? For example, one line change in your company's profile.
  Copy and paste? If yes, you still live in 20th century.

**yehua** is a command line tool to provide a default scaffolding for a python package. It provides a blank python package where
your organisation's specific static infomation is injected. Future updates
is linked with `moban`_ which instantly applies the update accurately.
What's more, the python package is github and travis-ci friendly.

What's more, you can provide your own python package templates and your own
yehua file to customize **yehua** to meet your own needs.


Installation
--------------------------------------------------------------------------------

You can install it via pip:

.. code-block:: bash

    $ pip install yehua


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/chfw/yehua.git
    $ cd yehua
    $ python setup.py install

Usage
--------------------------------------------------------------------------------

.. image:: https://github.com/chfw/yehua/raw/master/yehua-usage.gif
   :width: 600px

Simply type in ::

    $ yehua

And then go into the generate project folder::

    $ moban

Documentation
--------------------------------------------------------------------------------

.. toctree::

   usage
   extended_usage
   enterprise_usage

.. _moban: https://github.com/chfw/moban
