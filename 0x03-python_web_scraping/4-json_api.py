#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        j = r.json()
    except:
        print("Not a valid JSON")
    if not j:
        print("No result")
    else:
        print("[{}] {}".format(j.get('id'), j.get('name')))
