#!/bin/bash

docker-compose -f test.yml up --build -V --abort-on-container-exit &&
docker-compose -f test.yml down
