pip freeze
pip install -e .
pytest --cov=yehua --cov=tests tests/ --ignore=tests/fixtures/project_s
