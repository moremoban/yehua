Enterprise use case: scaffolding all projects in your organisation
================================================================================

Previous example shows that you can write up your own yehua.yml and supporting
templates and static files and **yehua** creates the scaffolding for you.

Now in an enterprise context, you as the team lead or the architect would like
to propagate the best practices to all new projects. What you can do is to
make the yehua.yml and its files into repository. And then you could set::

   $ export YEHUA_FILE=/location/to/the/cloned/yehua/repo/yehua.yml

Since then, yehua would always use that yehua file for scaffolding.

if you want to try it now, you could do this::

   $ export YEHUA_FILE=/location/to/yehua/repo/examples/npm-init/yehua.yml
   $ yehua
