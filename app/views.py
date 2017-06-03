#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
from app import apipath
from flask import request
import requests
import json

help_message = u"Known commands are:\n - /ping\n - /help"

def send_message(chat_id, text):
    requests.get(apipath + "sendMessage", params={"chat_id":chat_id, "text": text})

@app.route('/', methods=['POST'])
def index():
    message=request.json
    if(message["message"]["text"] == "/ping"):
        send_message(message["message"]["chat"]["id"], u"pong")
    elif(message["message"]["text"] == "/help"):
        send_message(message["message"]["chat"]["id"], help_message)
    else:
        send_message(message["message"]["chat"]["id"], u"Unknown command\n" + help_message)
    return 'OK',200

@app.route('/test')
def test():
    message=request
    return message
