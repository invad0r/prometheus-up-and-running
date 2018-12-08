.PHONY: curl up build update clean

curl:
	curl localhost:8000
	curl localhost:8001

up:
	docker-compose -f docker-compose.yml up -d

build:
	docker-compose -f docker-compose.yml build

clean:
	docker-compose -f docker-compose.yml down -v

update: build clean up
