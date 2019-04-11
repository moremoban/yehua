all: test

test:
	bash test.sh

lint:
	bash lint.sh

format:
	isort -y $(find {{project_name | replace('-', '_')}} -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 {{project_name | replace('-', '_')}}
	black -l 79 tests
