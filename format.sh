isort $(find yehua -name "*.py"|xargs echo) $(find tests -name "*.py"|grep -v 'project_'| xargs echo)
black -l 79 yehua
black --exclude "/tests\/fixtures\/project_.*/" -l 79 tests
