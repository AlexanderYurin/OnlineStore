FROM python:3.11-alpine3.16
COPY . /app
WORKDIR /app
EXPOSE 8000

RUN pip install -r requirements.txt

