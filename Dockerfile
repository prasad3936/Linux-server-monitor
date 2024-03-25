
FROM ubuntu:latest AS build

#Install all Dependencies
RUN  apt-get update &&  apt-get install python3-flask python3-psutil -y

#Setting Up the working direct
WORKDIR /app

COPY . /app

CMD ["python3","app.py"]
EXPOSE 5000

