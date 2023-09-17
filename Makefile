.PHONY: install format lint test sec

install:
	@poetry install
format:
	@isort .
	@black .
lint:
	@black . --check
	@isort . --check
	@prospector --with-tool pydocstyle --doc-warning
test:
	@pytest -v
sec:
	@pip-audit


