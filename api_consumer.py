#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
# define URLs for Request and payload

API_URL = 'http://127.0.0.1:5000/predict'
SPEC_PATH = 'spec/test.json'

# create payload

specification = open(SPEC_PATH, 'rb').read()

payload = specification

# create the request

req = requests.post(API_URL, json=specification).json()
# process the response and respond to the user
print(req.content)