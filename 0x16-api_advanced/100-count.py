#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import praw

def count_words(subreddit, word_list, reddit_instance=None, results=None):
    """
    Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """

    if reddit_instance is None:
        reddit_instance = praw.Reddit(user_agent='Reddit Keyword Counter by YourUsername')
    if results is None:
        results = {}

    subreddit_obj = reddit_instance.subreddit(subreddit)

    try:
        hot_articles = subreddit_obj.hot(limit=25)
    except praw.exceptions.Redirect:
        # Invalid subreddit or no posts match
        return

    for submission in hot_articles:
        title = submission.title.lower()
        for word in word_list:
            # Check for whole word match, ignoring special characters
            if f' {word} ' in f' {title} ':
                results[word] = results.get(word, 0) + 1

    if hasattr(hot_articles, 'params') and 'after' in hot_articles.params:
        # Recursive call with the next set of articles
        count_words(subreddit, word_list, reddit_instance, results)
    else:
        # Print the results in the required format
        sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_results:
            print(f'{word}: {count}')
