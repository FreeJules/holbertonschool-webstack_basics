#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'
    r = requests.get(url)
    j = r.json()
    commiters = {}
    for i in range(10):
        name_req_url = j[i].get('committer').get('url')
        if name_req_url not in commiters:
            name_req = requests.get(name_req_url)
            commiters[name_req_url] = name_req.json().get('name')
        print('{}: {}'.format(j[i].get('sha'), commiters[name_req_url]))
