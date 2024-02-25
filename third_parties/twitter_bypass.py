import json

def scrape_user_tweets(num_tweets=20):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """

    with open('third_parties/edens_tweets.json', 'r') as file:
        tweet_list = json.load(file)

    return tweet_list
# print (scrape_user_tweets(num_tweets=20))