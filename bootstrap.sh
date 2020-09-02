#!/bin/bash

echo -e "Starting applications and databases"
docker-compose up -d 

echo -e "Sleeping 30 seconds"
sleep 30

echo -e "Populating movies database"
docker-compose -f docker-compose-scraper.yml up -d 