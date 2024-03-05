#!/usr/bin/python3
"""1. Top Ten"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in result.json().get("data").get("children")]
