FROM centos:latest
LABEL dockerhub="sowens81"
LABEL contact="steve.owens@uk.fujitsu.com"
LABEL version="1.0"
LABEL description="Centos 7 container with Python 7.3"
RUN yum update -y \
    && yum groupinstall -y "development tools" \
    && yum install -y wget libffi-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel \
    && cd /usr/src \
    && wget http://python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz \
    && tar xf Python-3.7.2.tar.xz \
    && cd Python-3.7.2 \
    && ./configure --enable-optimizations \
    && make altinstall \
    && pip3.7 install --upgrade pip \
ENTRYPOINT [ "/bin/bash" ]