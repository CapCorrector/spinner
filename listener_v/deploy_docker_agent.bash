#!/bin/bash

# Stop and remove existing docker entries

echo *** Stopping listener process
docker stop listener 2>&1 > /dev/null

echo *** Removig listener process
docker rm listener 2>&1 > /dev/null

# Build frontend from inside Vagrant host
echo *** Build  listener
cd /vagrant/listener
docker build . -t u:listener

# Start docker listener service in background as listener
echo *** Run listener and map to port 998 on Vagrant host
docker run -d --restart=always --name listener -p 998:998 u:listener
