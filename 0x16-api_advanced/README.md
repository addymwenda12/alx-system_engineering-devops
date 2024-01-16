## API Advanced Project

This project contains solutions for the API Advanced task from the Alx System Engineering and DevOps program. The task requires writing several functions that query the Reddit API and return various information about subreddits.

## Files
- `0-subs.py`
This file contains the function `number_of_subscribers(subreddit)` which takes a subreddit name as an argument and returns the number of subscribers for that subreddit. If the subreddit is invalid, the function returns 0

- `1-top_ten.py`
This file contains the function `top_ten(subreddit)` which takes a subreddit name as an argument and prints the titles of the first 10 hot posts listed for that subreddit. If the subreddit is invalid, the function prints None.

- `2-recurse.py`
This file contains the recursive function `recurse(subreddit, hot\_list=[])` which takes a subreddit name as an argument and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

- `3-count.py`
This file contains the recursive function `count_words(subreddit, word_list)` which takes a subreddit name and a list of keywords as arguments, queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not). If no posts match or the subreddit is invalid, print nothing.

## Usage

To use the functions, you can import them into your Python script and call them with the appropriate arguments.

## Dependencies
This project requires the praw library to interact with the Reddit API. You can install it using pip:

```bash
pip install praw
```
## Testing
To test the functions, you can use the provided `main.py` files in each directory. Simply run the file with the appropriate arguments:

```
python 0-main.py programming
python 1-main.py programming
python 2-main.py programming
python 3-main.py programming 'python java javascript'
```
