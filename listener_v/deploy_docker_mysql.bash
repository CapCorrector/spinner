#!/bin/bash

# Stop and remove existing docker entries

echo *** Stopping listener process
docker stop mysql > /dev/null 2>&1

echo *** Removig listener process
docker rm mysql > /dev/null 2>&1

# Build frontend from inside Vagrant host
echo *** Pull MySQL
docker pull mysql/mysql-server:latest

# Start docker listener service in background as listener
echo *** Run mysql and map to port 3306 on Vagrant host
mkdir -p /etc/mysql
mkdir -p /var/lib/mysql/mysqlmon
cp -f /vagrant/my.cnf /etc/mysql/d_monmy.cnf
docker run --restart=always --name=mysql-mon -d -p 3306:3306 --mount type=bind,src=/etc/mysql/d_monmy.cnf,dst=/etc/my.cnf --mount type=bind,src=/var/lib/mysql/mysqlmon,dst=/var/lib/mysql mysql/mysql-server:latest
docker logs mysql-mon 2>&1 | grep GENERATED > /vagrant/mysql.pass