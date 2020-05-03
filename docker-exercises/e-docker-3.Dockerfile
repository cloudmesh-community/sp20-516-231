FROM ubuntu:18.04
ARG mongo_user
ARG mongo_pw
ENV MONGO_USER=$mongo_user
ENV MONGO_PW=$mongo_pw

MAINTAINER Gregor von Laszewski <laszewski@gmail.com>

# because otherwise it can't install cloudmesh-openstack
# because cloudmesh.common.systeminfo needs os.environ['USER']
ENV USER=root

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y --no-install-recommends install build-essential
RUN apt-get -y --no-install-recommends install git
RUN apt-get -y --no-install-recommends install curl
RUN apt-get -y --no-install-recommends install wget
RUN apt-get -y --no-install-recommends install sudo
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install cloudmesh-installer

RUN mkdir cm
WORKDIR cm

RUN ls
RUN echo
RUN cloudmesh-installer git clone cloud
RUN cloudmesh-installer install cloud

#COPY ./cloudmesh.yaml ~/.cloudmesh/cloudmesh.yaml
#RUN export MONGO_USER=$(cms config value cloudmesh.data.mongo.MONGO_USERNAME | tail -n1)
#RUN export MONGO_PW=$(cms config value cloudmesh.data.mongo.MONGO_PASSWORD | tail -n1)
# much easier to have these be build args since the export doesn't persist through layers
RUN echo $MONGO_USER
RUN echo $MONGO_PW

RUN apt-get install -y libcurl4 openssl
RUN wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1804-4.2.6.tgz
RUN tar -xzvf mongodb-linux-x86_64-ubuntu1804-4.2.6.tgz
RUN cp mongodb-linux-x86_64-ubuntu1804-4.2.6/bin/* /usr/local/bin/
RUN mkdir -p /data/db
ENTRYPOINT ["sh", "-c", "mongo -u ${MONGO_USER} -p ${MONGO_PW} --host mongo-auth"]
