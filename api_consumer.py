import requests

#define URLs for Request and payload
API_URL = ""
SPEC_PATH = "spec/test.json"

#create payload
specification = open(SPEC_PATH, "rb").read()
payload = {"specOpenApi": specification}