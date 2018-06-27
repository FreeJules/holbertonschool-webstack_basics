#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    uname = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get(url, auth=(uname, pwd))
    j = r.json()
    print(j.get('id'))
