#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
# define URLs for Request and payload

API_URL = 'http://127.0.0.1:5000/predict'
SPEC_PATH = 'spec/test.json'

# create payload

specification = open(SPEC_PATH, 'rb').read()
payload = {'spec': specification}

# create the request

req = requests.post(API_URL, files=payload)

# process the response and respond to the user

if req["success"]:
    	# loop over the predictions and display them
	for (i, result) in enumerate(r["predictions"]):
		print("{}. {}: {:.4f}".format(i + 1, result["label"]))

# otherwise, the request failed
else:
	print("Request failed")
