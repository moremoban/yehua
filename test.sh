pip freeze
nosetests --with-coverage --cover-package yehua --cover-package tests  tests docs/source yehua && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
