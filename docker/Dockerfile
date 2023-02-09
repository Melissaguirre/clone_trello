FROM python:3.9-slim

COPY ./requirements.txt /app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000