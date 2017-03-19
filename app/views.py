#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
from app import apipath
from flask import request
import requests

def ping(chat_id):
    requests.get(apipath + "sendMessage", params={"chat_id":chat_id, "text": "pong"})


@app.route('/', methods=['POST'])
def index():
    print(request.form)
    return 'OK',200
