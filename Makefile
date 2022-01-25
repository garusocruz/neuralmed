clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	rm -f .coverage
	rm -f pylint.out

docker_build: clean
	sudo docker-compose -f .docker/docker-compose.yml build --no-cache

# Run command to destroy all containers
destroy_containers: clean
	sudo docker rm -f $(docker ps -a -q)

# Run command to destroy all docker images
destroy_images: clean
	sudo docker rmi -f $(docker images -a -q)

# Run command to destroy all docker images
destroy_volumes: clean
	sudo docker volume rm $(docker volume ls -q)

# Run command to stop docker compose
docker_stop: clean
	sudo docker-compose -f .docker/docker-compose.yml stop

# Run command to start docker compose
docker_up: clean
	sudo docker-compose -f .docker/docker-compose.yml up

test: clean
	sudo ./pandora_box/scripts/coverage.sh