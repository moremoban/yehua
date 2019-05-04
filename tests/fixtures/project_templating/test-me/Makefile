all: test

test:
	bash test.sh

lint:
	bash lint.sh

format:
	isort -y $(find test_me -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 test_me
	black -l 79 tests
