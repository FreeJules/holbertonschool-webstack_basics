#!/usr/bin/python3
import requests

url = 'https://intranet.hbtn.io/status'
r = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(type(r.text)))
