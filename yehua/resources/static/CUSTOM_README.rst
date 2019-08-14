{% extends 'README.rst.jj2' %}

{%block documentation_link%}
.. image:: https://dev.azure.com/{{orgnisation}}/{{name}}/_apis/build/status/{{orgnisation}}.{{name}}?branchName=master
   :target: https://dev.azure.com/{{organisation}}/{{name}}/_build/latest?definitionId=2&branchName=master
{%endblock%}
