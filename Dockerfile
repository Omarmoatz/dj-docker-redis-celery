# setup server

# 1 : setup linux slim-bullseye and download python 3.11
FROM python:3.11-slim-bullseye 

# env: to show logs
ENV PYTHONUNBUFFERED = 1

# update linux kernal and setup tools
RUN apt-get update && apt-get -y install gcc libpq-dev 

# create folder for the project
WORKDIR /app  

# copy requirments from my pc to docker
COPY requirements.txt /app/requirements.txt

# install requirments
RUN pip install -r /app/requirements.txt 

# copy project code to docker
COPY . /app/

