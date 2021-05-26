# base for docker image
FROM python:3.8

ENV PYTHONUNBUFFERED 1python

# create a new directory for the app
RUN mkdir /app

# change into the new directory
WORKDIR /app

# create and activate a virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# copy files from local environment to image
COPY . /app

# install project dependencies
RUN pip3 install -r requirements.txt



