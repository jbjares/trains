.PHONY: build

build:
	docker build --no-cache --pull --rm -t lukaszimmermann/pht-train-helloworld:latest .
