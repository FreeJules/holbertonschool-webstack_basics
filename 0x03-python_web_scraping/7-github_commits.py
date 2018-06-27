#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'
    r = requests.get(url)
    j = r.json()
    for i in range(10):
        print('{}: {}'.format(j[i].get('sha'), j[i].get('commit')
                              .get('author').get('name')))
