# Pull base image
FROM python:3.7.13-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

COPY ./poetry.lock .
COPY ./pyproject.toml .

COPY ./requirements.txt .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
# RUN poetry install --no-dev
RUN poetry add $( cat requirements.txt )

# Copy project
COPY . /code/