#Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Ilya Sukhov <tovarischsuhov0@yandex.ru>
ARG BRANCH
ARG ENVIRONMENT
RUN apt-get update
RUN apt-get install -y python3 python3-flask git python3-pip

RUN git clone -b ${BRANCH} --single-branch https://github.com/TovarischSuhov/tjvj.git /root/tjvj
RUN ln -s /root/automation_bot/run.py /usr/bin/automation_bot

RUN apt-get remove -y git

CMD ["python3", "/root/automation_bot/run.py"]

