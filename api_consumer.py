#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

# define URLs for Request and payload

API_URL = ''
SPEC_PATH = 'spec/test.json'

# create payload

specification = open(SPEC_PATH, 'rb').read()
payload = {'specOpenApi': specification}

# create the request

req = requests.post(API_URL, files=payload).json()

# process the response and respond to the user

if r['success']:
    for (i, result) in enumerate(r['predictions']):
        print
        '{}. {}: {:.4f}'.format(i + 1, result['label'],
                                result['probability'])
else:
    print
    'Error with Request'
