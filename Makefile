.PHONY:
lint:
	flake8 kestrel/ test/

.PHONY:
start:
	python bin/kestrel.py

.PHONY:
test: lint
	python -m pytest
