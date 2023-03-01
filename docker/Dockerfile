FROM python:3.9-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY . .

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt 

EXPOSE 8000