# https://docs.docker.com/get-started/part2/#apppy

# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app
RUN wget https://raw.githubusercontent.com/capcorrector/spinner/master/listener/listener.py

RUN pip install -r requirements.txt

# Run Frontend.py when the container launches

CMD python listener.py
