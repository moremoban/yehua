all: test

test:
	bash test.sh

doc:
	sphinx-build -b html docs/source docs/build

spelling:
	sphinx-build -b spelling docs/source/ docs/build/spelling

format:
	isort -y $(find yehua -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 yehua
	black -l 79 tests
