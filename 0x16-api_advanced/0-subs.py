#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""

    header = {'User-Agent': 'MyPythonScript/1.0'}
    request = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json", header=header)

    if request.status_code == 200:
        subscribers = request.json().get('data').get('subscribers')
        return subscribers if subscribers else 0
    return 0
