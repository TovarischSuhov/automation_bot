#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app

@app.route('/', methods=["POST"])
def index():
    return("OK")
