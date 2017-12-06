RUN := run --rm
DOCKER_COMPOSE_RUN := docker-compose $(RUN)

default: compose-test

test:
	raco test */*.rkt

compose-build:
	docker-compose build

compose-test:
	${DOCKER_COMPOSE_RUN} app raco test */*.rkt

compose-bash:
	${DOCKER_COMPOSE_RUN} app bash

.PHONY: test
