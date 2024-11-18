# Makefile for running pytest with coverage

# Virtual environment directory
VENV_DIR = venv

# Activate the virtual environment and install dependencies if not present
VENV_ACTIVATE = . $(VENV_DIR)/bin/activate && pip install -r requirements.txt

# Deactivate the virtual environment
VENV_DEACTIVATE = deactivate

# Default target (run all tests with coverage)
.PHONY: test
test:
	@echo "Running tests for function$(function) with coverage (terminal report)"
	@if [ -z "$(function)" ]; then \
		$(VENV_ACTIVATE) && PYTHONPATH=$(PWD) pytest --cov=example_functions --cov-report=term-missing; \
	else \
		$(VENV_ACTIVATE) && PYTHONPATH=$(PWD) pytest --cov=example_functions.function$(function) --cov-report=term-missing tests/test_function$(function).py; \
	fi

# HTML coverage report (run all tests or specific function based on parameter)
.PHONY: test-html
test-html:
	@echo "Running tests for function$(function) with coverage (HTML report)"
	@if [ -z "$(function)" ]; then \
		$(VENV_ACTIVATE) && PYTHONPATH=$(PWD) pytest --cov=example_functions --cov-report=html; \
	else \
		$(VENV_ACTIVATE) && PYTHONPATH=$(PWD) pytest --cov=example_functions.function$(function) --cov-report=html tests/test_function$(function).py; \
	fi

# XML coverage report (for integration with CI tools)
.PHONY: test-xml
test-xml:
	@echo "Running tests for function$(function) with coverage (XML report)"
	@if [ -z "$(function)" ]; then \
		$(VENV_ACTIVATE) && PYTHONPATH=$(PWD) pytest --cov=example_functions --cov-report=xml; \
	else \
		$(VENV_ACTIVATE) && PYTHONPATH=$(PWD) pytest --cov=example_functions.function$(function) --cov-report=xml tests/test_function$(function).py; \
	fi

# Clean up HTML report
.PHONY: clean
clean:
	@echo "Cleaning up HTML report"
	rm -rf htmlcov/
