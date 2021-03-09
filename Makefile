ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

build:
	docker build . -t speedo:latest

run:
	docker run --rm -v $(ROOT_DIR)/crawler:/speedo/code speedo:latest "http://news.ycombinator.com"

test: 
	docker run --rm -v $(ROOT_DIR)/crawler:/speedo/code --entrypoint pytest speedo:latest -v

lint:
	docker run --rm -v $(ROOT_DIR)/crawler:/apps alpine/flake8:3.8.4 --ignore="W,E302,E501,E225,E265,E128,E261,E303,E127,E231,E251,E402" .
