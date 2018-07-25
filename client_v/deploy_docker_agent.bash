#!/bin/bash

# Stop and remove existing docker entries

echo *** Stopping agent process
docker stop agent 2>&1 > /dev/null

echo *** Removig agent process
docker rm agent 2>&1 > /dev/null

# Build frontend from inside Vagrant host
echo *** Build  agent
cd /vagrant/agent
docker build . -t u:agent

# Start docker frontend service in background as frontend
echo *** Run agent and map to port 999 on Vagrant host
docker run -d --restart=always --name agent -p 999:999 -e HOSTIP=$(ip addr | grep enp0s8 | awk {'print $2'} | tail -1) u:agent

