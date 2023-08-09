# Makefile

# Constants
DOCKER_COMPOSE = docker compose  # For Linux users, it could be necessary to modify this line to docker-compose
APP_NAME = lottery
DOCKER_COMPOSE_FILE = docker-compose.yml
LOTTERY_IMAGE = lottery_app-lottery_app


# Targets
.PHONY: build
build:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) build

.PHONY: up
up:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up -d

.PHONY: down
down:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

.PHONY: test
test: up
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run --rm lottery_app python manage.py test $(APP_NAME)

.PHONY: clean
clean: down
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down -v

.PHONY: clean_image
clean_image: down
	docker rmi $(LOTTERY_IMAGE)

.PHONY: logs
logs:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f lottery_app

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  build    Build the Docker containers"
	@echo "  up       Start the Docker containers"
	@echo "  down     Stop and remove the Docker containers"
	@echo "  test     Run Django tests inside a Docker container"
	@echo "  clean    Stop and remove the Docker containers along with volumes"
	@echo "  help     Display this help message"
