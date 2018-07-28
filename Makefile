env:
	virtualenv env
	./env/bin/pip install -r requirements.txt

.PHONY:
lint: env
	./env/bin/python -m flake8 *.py

.PHONY:
test: lint
