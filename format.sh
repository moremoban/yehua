isort -y $(find yehua -name "*.py"|xargs echo) $(find tests -name "*.py"|grep -v 'project_s'|xargs echo)
echo "blacking.."
black -l 79 yehua
black -l 79 tests --exclude=tests/fixtures/project_s/
