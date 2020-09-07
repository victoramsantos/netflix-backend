#!/bin/bash

echo -e "\n>> Starting applications and databases"
docker-compose up -d 

echo -e "\n>> Sleeping 30 seconds"
sleep 30

echo -e "\n>> Populating movies database"
docker-compose -f docker-compose-scraper.yml up

echo -e "\n>> All services are up"