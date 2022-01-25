#!/usr/bin/env bash
docker-compose -f .docker/docker-compose.yml run --rm neuralmed-pandora-box bash -c "
    coverage run -m pytest"
