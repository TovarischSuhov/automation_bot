#Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Ilya Sukhov <tovarischsuhov0@yandex.ru>
RUN apt-get update
RUN apt-get install -y python3 python3-flask git python3-pip

RUN git clone https://github.com/TovarischSuhov/automation_bot.git /root/automation_bot
RUN ln -s /root/automation_bot/run.py /usr/bin/automation_bot

RUN apt-get remove -y git

CMD ["python3", "/root/automation_bot/run.py"]

