#!/bin/bash

# Stop and remove existing docker entries

echo *** Stopping listener process
docker stop listener > /dev/null 2>&1

echo *** Removig listener process
docker rm listener > /dev/null 2>&1

# Build frontend from inside Vagrant host
echo *** Build  listener
cd /vagrant/listener
docker build . -t u:listener

# Start docker listener service in background as listener
echo *** Run listener and map to port 998 on Vagrant host
docker run -d --restart=always --name listener -p 998:998 u:listener
