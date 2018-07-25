#!/bin/bash

# Stop and remove existing docker entries

echo *** Stopping frontend process
docker stop agent > /dev/null

echo *** Removig frontend process
docker rm agent > /dev/null

# Build frontend from inside Vagrant host
echo *** Build  agent
cd /vagrant/agent
docker build . -t u:agent

# Start docker frontend service in background as frontend
echo *** Run agent and map to port 999 on Vagrant host
docker run -d --restart=always --name agent -p 999:999 u:agent

