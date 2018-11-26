#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json


# define URLs for Request and payload
API_URL = 'http://localhost:5000/predict'
SPEC_PATH = 'spec/test.json'

# create the request
headers = {'Content-Type': 'application/json'}
req = requests.post(API_URL, data=open(SPEC_PATH, 'rb'), headers=headers)

# process the response and respond to the user
print(req.content)
