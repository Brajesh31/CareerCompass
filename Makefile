PYTHON ?= python

.PHONY: install-dev test check syntax run

install-dev:
	$(PYTHON) -m pip install -r requirements-dev.txt

test:
	$(PYTHON) -m pytest -q

check:
	$(PYTHON) scripts/check_repository.py

syntax:
	$(PYTHON) -m compileall -q app.py session_state.py scripts

run:
	$(PYTHON) -m streamlit run app.py
