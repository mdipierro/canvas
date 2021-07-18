clean:
	rm -rf dist
build:
	make clean
	python3 setup.py build
install: dist
	python3 setup.py install
test:	install
	python3 -m unittest tests
deploy:
	make clean
	python setup.py sdist
	twine upload dist/*
