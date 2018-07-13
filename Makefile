.PHONY:
lint:
	flake8 bin/ src/ test/

.PHONY:
start:
	python bin/kestrel.py

.PHONY:
test: lint
	python -m pytest
