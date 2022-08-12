FROM python:3.10


WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
COPY .env .env

RUN pip3 install -r requirements.txt

COPY . .