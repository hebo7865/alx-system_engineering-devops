#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, header=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")
