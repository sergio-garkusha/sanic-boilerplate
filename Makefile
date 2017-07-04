help:
	@echo "To setup and/or use environment for this project run:"
	@echo "    source ./env.sh"
	@echo ""
	@echo "Available commands:"
	@echo "    install"
	@echo "       Install project dependencies from requirements.txt."
	@echo "    run"
	@echo "        Run the `my_project` service on your local machine."
	@echo "    list"
	@echo "       Shows packages available from current environment."
	@echo "    freeze"
	@echo "       Makes requirements.txt file."
	@echo "    clean-pyc"
	@echo "       Remove python artifacts."
	@echo "    isort"
	@echo "        Sort import statements."
	@echo "    lint"
	@echo "        Check style with flake8."
	@echo "    test"
	@echo "        Run tests."

install:
	pip install -r requirements.txt

run:
	python server.py --host $(HOST) --port $(PORT)

lint:
	flake8 --exclude=.tox

test:
	@echo "Not implemented yet."

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

list:
	pip list --format=columns

freeze:
	pip freeze > requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +
