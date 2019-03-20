FROM python:3.6
LABEL dockerhub="sowens81"
LABEL contact="steve.owens@uk.fujitsu.com"
LABEL version="1.0.1"
LABEL description="Python Application"
ADD . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 5000
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3","run.py"]
CMD ["migratedata.sh"]