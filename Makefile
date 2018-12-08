.PHONY: curl up build update clean update-app

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

update-app:
	docker-compose -f docker-compose.yml build metrics
	docker-compose -f docker-compose.yml up -d metrics
