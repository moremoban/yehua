{%block pretest%}
{%endblock%}
{%if external_module_library%}
  {%set package=external_module_library%}
{%else%}
  {%if webframework%}
    {%set package=webframework + '_excel' %}
  {%else%}
    {%if misc%}
      {%set package=misc %}
    {%else%}
      {%if command_line_interface%}
        {%set package=command_line_interface + '_cli' %}
      {%else%}
        {% if name == nick_name %}
          {%set package=name%}
        {%else%}
          {%set package='pyexcel_' + nick_name%}
        {%endif%}
      {%endif%}
	{%endif%}
  {%endif%}
{%endif%}
pip freeze
nosetests --with-cov --cover-package {{package|lower}} --cover-package tests {%if not exclude_doctest%}--with-doctest --doctest-extension=.rst README.rst{%endif%} tests {%if not nodocs%}docs/source{%endif%} {%if not external_module_library%}{{package|lower}}{%endif%} && flake8 . --exclude=.moban.d {%block flake8_options%}--builtins=unicode,xrange,long{%endblock%}

{%block posttest%}
{%endblock%}
