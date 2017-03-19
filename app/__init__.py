#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
import configparser
import os
app = Flask(__name__)

config = configparser.RawConfigParser()
config.read([os.path.expanduser('~/conf/config.cfg')])
apipath = "https://api.telegram.org/bot" + config.get("bot","bot_id") + "/"

from app import views
