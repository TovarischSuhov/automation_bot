#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
from app import apipath
from flask import request
import requests
import json


def send_message(chat_id, text):
    requests.get(apipath + "sendMessage", params={"chat_id":chat_id, "text": text})


def ping(chat_id):
    send_message(chat_id, "pong")

@app.route('/', methods=['POST'])
def index():
    message=json.dumps(request.json)
    if(message["message"]["text"] == "/ping"):
        ping(message["message"]["chat"]["id"])
    else:
        send_message(message["message"]["chat"]["id"], u"Что")
    return 'OK',200
