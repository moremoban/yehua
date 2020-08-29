isort $(find project_yehua -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 project_yehua
black -l 79 tests
