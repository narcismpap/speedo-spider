ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

build:
	docker build . -t docker.pkg.github.com/narcismpap/speedo-spider/speedo:latest

run:
	docker run --rm -v $(ROOT_DIR)/crawler:/speedo/code docker.pkg.github.com/narcismpap/speedo-spider/speedo:latest "http://news.ycombinator.com"

test: 
	docker run --rm -v $(ROOT_DIR)/crawler:/speedo/code --entrypoint pytest docker.pkg.github.com/narcismpap/speedo-spider/speedo:latest -v

lint:
	docker run --rm -v $(ROOT_DIR)/crawler:/apps alpine/flake8:3.8.4 --ignore="W,E302,E501,E225,E265,E128,E261,E303,E127,E231,E251,E402" .
