#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search=" + sys.argv[1]
    r = requests.get(url)
    j = r.json()
    print('Number of results: {}'.format(j.get('count')))
    results = j.get('results')
    for result in results:
        print(result.get('name'))
