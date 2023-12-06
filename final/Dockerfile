FROM python:3.10.12-slim-bullseye

LABEL maintainer="srimel@pdx.edu"

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y wkhtmltopdf

CMD gunicorn --bind :$PORT --workers 1 --threads 8 app:app