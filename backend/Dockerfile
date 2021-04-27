# syntax=docker/dockerfile:1
FROM python:3.8.5-slim-buster

WORKDIR /code

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y netcat

# Pipenv setup
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project code
COPY . .

ENTRYPOINT ["/code/entrypoint.sh"]
