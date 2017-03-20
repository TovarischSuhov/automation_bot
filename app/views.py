#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
from app import apipath
from flask import request
import requests


def send_message(chat_id, text):
    requests.get(apipath + "sendMessage", params={"chat_id":chat_id, "text": text})


def ping(chat_id):
    send_message(chat_id, "pong")

@app.route('/', methods=['POST'])
def index():
    app.logger.error(request.json)
    return 'OK',200
