{% from "usage.rst.jj2" import usage %}
{%include "header.rst" %}


Introduction
--------------------------------------------------------------------------------

{%include "yehua.feature.rst"%}

Installation
--------------------------------------------------------------------------------

{%include "installation.rst.jj2" %}

Usage
--------------------------------------------------------------------------------

{{ usage('sphinx') }}

Documentation
--------------------------------------------------------------------------------

.. toctree::

   usage
   extended_usage
   enterprise_usage

.. _moban: https://github.com/chfw/moban
