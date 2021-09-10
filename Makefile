.PHONY: publish pytest clean lint build test

build:
	./setup.py sdist && ./setup.py bdist_wheel

test: pytest lint

publish:
	twine upload dist/* && git push && git push --tags

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf .eggs/
	rm -rf *.egg-info/

pytest:
	pytest -xvv

lint:
	flake8 --exclude=.env,.tox,dist,docs,build,*.egg,.venv --max-line-length 99 .
