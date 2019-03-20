FROM ubuntu:latest
LABEL dockerhub="sowens81"
LABEL contact="steve.owens@uk.fujitsu.com"
LABEL version="1.0.1"
LABEL description="Ubuntu container with Python 3"
RUN apt-get update -y 
RUN apt-get install -y python3-pip 
COPY . /project
WORKDIR /project 
RUN pip3 install -r requirements.txt 
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD [ "run.py" ]