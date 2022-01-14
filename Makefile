.EXPORT_ALL_VARIABLES:
.PHONY: venv help docker
# Unlike most variables, the variable SHELL is never set from the environment.
# This is because the SHELL environment variable is used to specify your personal
# choice of shell program for interactive use. It would be very bad for personal
# choices like this to affect the functioning of makefiles. See Variables from the Environment.
SHELL=/bin/bash
VIRTUAL_ENV=${PWD}/.venv
# LOCAL ENVIRONMENT
PYTHONUNBUFFERED=1

.ONESHELL:
venv:
	rm -rf $(VIRTUAL_ENV) && python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip3 install --upgrade pip wheel setuptools
	$(VIRTUAL_ENV)/bin/pip3 install --compile --upgrade --force-reinstall --requirement requirements.txt

.ONESHELL:
pytest:
	$(VIRTUAL_ENV)/bin/pytest -rP

.ONESHELL:
run:
	$(VIRTUAL_ENV)/bin/python src/app.py

test: venv pytest

help:
	@echo "Usage:"
	@echo "  make venv - create virtual environment for the project"
	@echo "  make test - run automated tests"
