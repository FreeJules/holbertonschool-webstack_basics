#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'
    r = requests.get(url)
    j = r.json()
    commits = 10
    num_commits = len(j)
    if num_commits < 10:
        commits = num_commits
    for i in range(commits):
        print('{}: {}'.format(j[i].get('sha'), j[i].get('commit')
                              .get('author').get('name')))
