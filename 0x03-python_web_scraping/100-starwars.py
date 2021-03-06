#!/usr/bin/python3
import requests
import sys


def print_names(url):
    if not url:
        return
    r = requests.get(url)
    j = r.json()
    results = j.get('results')
    for result in results:
        print(result.get('name'))
        print_films(result.get('films'))
    print_names(j.get('next'))


def print_films(film_list):
    for film in film_list:
        r = requests.get(film)
        j = r.json()
        print('\t{}'.format(j.get('title')))

if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search=" + sys.argv[1]
    r = requests.get(url)
    j = r.json()
    print('Number of results: {}'.format(j.get('count')))
    print_names(url)
