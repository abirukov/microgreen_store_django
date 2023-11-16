ifneq (,$(wildcard .env))
$(info Found .env file.)
	include .env
	export
endif

export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

isort:
	isort .
style:
	flake8 .
types:
	mypy .
test:
	pytest --lf -vv --cov=microgreen_store --cov-branch .
check:
	make isort style types test
