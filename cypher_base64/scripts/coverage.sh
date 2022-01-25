#!/usr/bin/env bash
docker-compose -f .docker/docker-compose.yml run --rm neuralmed-cypher-base64 bash -c "
    coverage run -m pytest"
