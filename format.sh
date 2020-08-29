isort $(find yehua -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 yehua
black -l 79 tests  --exclude=tests/fixtures/project_
