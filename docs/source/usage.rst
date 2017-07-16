Default use case: scaffolding a python package
================================================================================

**yehua** reads a configuration file named yehua.yml which then instruct **yehua
to ask questions to collect project specific variables, and create the file
structures.

It takes a yehua file from command line option, or YEHUA_FILE in the environment
variable. If none is found, it resorts to the default yehua.yml file included
in the package. And the default yehua.yml create a blank python package.


Default yehua.yml file
--------------------------------------------------------------------------------

Let us go through the default yehua file. And then talk about the customization
in the next chapter

configuration section
********************************************************************************

**yehua** expects two set of files: templates and static files. configuration
section tells where they are relative to yehua.yml file.

.. literalinclude:: ../../yehua/resources/yehua.yml
   :lines: 4-6

In the default use case, the templates are located in yehua/resources/templates
and the static files are located in yehua/resources/static.

The files in the static folder will not be templated and will be copied across.

As a rule of thumb, if your file needs user input, please place it in templates
folder. Otherwise, please place your files in static folder, which is copied
across.

user question section
********************************************************************************

**yehua** will then ask a list of questions. The quoted lines are prompted to
the end user and the answers are given to the variable names on the left hand
side of semi-colon. Here is a simple format::

   - holding_variable_name_for_the_answer: "What is most intuitive question for the variable?"

Then "holding_variable_name_for_the_answer" can be used in your template files.

.. literalinclude:: ../../yehua/resources/yehua.yml
   :lines: 7-13

layout section
********************************************************************************

layout section outlines the folder structure of the resulting project folder.
**yehua** will create the folder layout before generating any outputs.

.. literalinclude:: ../../yehua/resources/yehua.yml
   :lines: 22-30

In this case, a default python package will have tests, docs and .moban.d at
its first level. **yehua** would always create a sub folder named after
project_name.

templates section
********************************************************************************

The files in this section follows this spec:

    - templated_target_file: template.file.in.templates.folder

.. literalinclude:: ../../yehua/resources/yehua.yml
   :lines: 31-33

As you can see, **yehua** would expand `project_name` for you.


static section
********************************************************************************

File in this section is simply copied over. Here is the spec::

  - relative_file_path: relative_static_file_path_in_static_folder

.. literalinclude:: ../../yehua/resources/yehua.yml
   :lines: 34-46


Template files
--------------------------------------------------------------------------------

Let's examine the beginning of project.yml in templates folder.

.. literalinclude:: ../../yehua/resources/templates/project.yml
   :lines: 1-5

#. project_name
#. organisation
#. author
#. contact
#. company

are unknown to yehua and only the user knows the answer. Hence, it brings
us to the next section: user questions

Static files
--------------------------------------------------------------------------------

The static files in yehua/resources/static are copied over by yehua according to
the instruction file.
