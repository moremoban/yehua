Custom use case: scaffolding a npm package
================================================================================

As mentioned in previous section, **yehua** would take a yehua.yml from command
line options. This section walk you through creating a npm package, **non-python
package**.

If you are familiar with npm, you can try and compare with yehua::

    $ npm init

Evaluation
--------------------------------------------------------------------------------

Please first checkout yehua repository so that you will have the access to
example directory. Then make sure you have **yehua** installed.

.. image:: https://github.com/chfw/yehua/raw/master/yehua-npm-usage.gif
   :width: 600px


yehua.yml for npm package
--------------------------------------------------------------------------------

Let us go through the variant yehua file.

configuration section
********************************************************************************

.. literalinclude:: ../../examples/npm-init/yehua.yml
   :lines: 12-15

the current directory where yehua.yml file is, is configured as the folder for
templates and static files.

user questions section
********************************************************************************

.. literalinclude:: ../../examples/npm-init/yehua.yml
   :lines: 15-24

the questions here are prompted to collect user inputs.

templates section
********************************************************************************

.. literalinclude:: ../../examples/npm-init/yehua.yml
   :lines: 25-26

Now the variables are used in template package.json.jj2 into package.json.

static section
********************************************************************************

.. literalinclude:: ../../examples/npm-init/yehua.yml
   :lines: 27-28

Now, **yehua** simply copies index.js to target package folder.
