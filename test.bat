pip freeze
nosetests --with-cov --cover-package yehua_cli --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source yehua_cli && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
