#Using Ubuntu as base OS for our application
FROM ubuntu:latest AS build

#Install all Dependencies
RUN  apt-get update &&  apt-get install python3-flask python3-psutil -y

#Setting Up the working direct
WORKDIR /app
#copying required data to target directory 
COPY . /app

CMD ["python3","app.py"]
#To Use port 5000, need to expose it first
EXPOSE 5000

