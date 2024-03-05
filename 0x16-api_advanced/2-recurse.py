#!/usr/bin/python3
"""2. Recurse it!"""
import requests


def recurse(subreddit, hot_list=[]):
    """queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"count": 0, "after": None}
    result = requests.get(url, headers=headers,
                          params=params, allow_redirects=False)
    if result.status_code >= 400:
        return None

    info = result.json()
    result = hot_list + [child.get("data").get("title")
                         for child in result.json()
                         .get("data")
                         .get("children")]
    if not info.get("data").get("after"):
        return result
    return recurse(subreddit, result, info.get("data").get("count"),
                   info.get("data").get("after"))
