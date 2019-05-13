REGISTRY_HOST ?= git2.devebs.net:4567
IMAGE ?= /tribes/main-api
REGISTRY ?= $(REGISTRY_HOST)$(IMAGE)
CONSOLE_COLUMNS ?= `echo $$(tput cols)`
CONSOLE_LINES ?= `echo $$(tput lines)`
DOCKER_COMEPOSE ?= docker/docker-compose.yaml
APP_NAME := $(word 3,$(subst _, ,$(MAKECMDGOALS)))
VERSION ?= $(shell bash -c 'git describe --abbrev=0 --tags')
PYTHON_BIN ?= python
# Image version default
ifndef IMAGE_VERSION
IMAGE_VERSION :=  0.0.1
endif

TMP_YAML=docker/docker-compose-$(IMAGE_VERSION).tmp.yaml

# app environment
ENV ?= development

PYV:=''

VARIABLE:="ls"
SECONDVAR:=$(shell $(VARIABLE))

all:
	@echo "VARIABLE=$(VARIABLE)"
	@echo "SECONDVAR=$(SECONDVAR)"

version:
	PYV:=$(PYTHON_BIN) --version
#	$(PYTHON_BIN) --version
	@echo $(PYV)

help:
	@echo "------------------------------------------"
	@echo "|    Let's MAKE!"
	@echo "|    Current version $(IMAGE_VERSION)"
	@echo "|    Default env $(ENV) "
	@echo "------------------------------------------"


validate:
	@docker --version >/dev/null 2>&1 || { echo "Docker is not installed! Aborting." >&2; exit 100; }

docker-build:
	@read -p "Enter environment:" ENV;
	@echo "**** ENV $(ENV) ****"
	docker build  -t $(REGISTRY):$(IMAGE_VERSION) .

docker-push :
	docker push $(REGISTRY):$(IMAGE_VERSION)

docker-up:
    # add release version in deployment yaml
	NEXUS_IMG=$(IMAGE) \
	CLEAN_VERSION=$(IMAGE_VERSION) \
	SERVING_DEPLOYMENT_SOURCE=$(DOCKER_COMEPOSE) \
	DEPLOYMENT_VERSIONED=$(TMP_YAML) \
	./docker/sed.sh
	docker-compose -f $(TMP_YAML) up

docker-down:
	rm $(TMP_YAML); \
	docker-compose down

docker-shell:
	@docker ps
	@read -p "Enter Container:" container; \
	clear; \
	docker exec -e TERM=$(TERM) -e "COLUMNS=$(CONSOLE_COLUMNS)" -e "LINES=$(CONSOLE_LINES)" -it $$container /bin/bash

add-module:
	@read -p "Enter Module Name:" module; \
	mkdir -p apps/$$module; \
	$(PYTHON_BIN) manage.py startapp $$module apps/$$module && echo "Module \"$$module\" created successfully!" || \
	(echo "Module creation failed with exit code $$?"; exit 1)

start:
	$(PYTHON_BIN) manage.py runserver 8005


test:
	$(PYTHON_BIN) manage.py test

deploy:
	@bash -c "ENV=${ENV} NEXUS_IMG=${IMAGE} ./docker/deploy.sh"
