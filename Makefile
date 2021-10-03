.PHONY: tests build

build-base:
	docker build --rm -t robotic-mowers-base -f ./docker/base/Dockerfile .

build:
	docker build --rm -t robotic-mowers -f ./docker/development/Dockerfile .

tests: export FILE=tests
tests:
	docker run -it robotic-mowers:latest sh -c "PYTHONPATH=. python -m pytest ${FILE} -vvv"

all: build tests
