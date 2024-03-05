#!/usr/bin/python3
"""0. How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code >= 300:
        return 0
    return result.json().get("data").get("subscribers")
