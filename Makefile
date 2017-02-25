lint:
	flake8 src/ api/

test:
	py.test --cov=src/ --cov=api/ --cov-report term-missing

init:
	pip3 install -r requirements.txt
