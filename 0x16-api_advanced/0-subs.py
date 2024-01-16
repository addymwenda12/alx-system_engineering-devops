#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
	"""Return the total number of subscribers in a given  subreddit"""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {
		'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
	}
	# Send a GET requesr to the API endpoint
	response = requests.get(url, headers=headers, allow_redirects=False)

	# If the request was unsuccessful
	if response.status.code == 404:
		return 0
	data = response.json()
	return data['data']['subscribers']
