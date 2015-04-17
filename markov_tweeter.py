import os

import twitter

from markov_at_tweet import TweetableMarkovGenerator

import sys

tweet_instance = TweetableMarkovGenerator()

script, txt_filename = sys.argv

# Use Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

# api = twitter.Api(
#     consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
#     consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
#     access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
#     access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# # This will print info about credentials to make sure they're correct
# print api.VerifyCredentials()

tweet_this = tweet_instance.make_text(txt_filename)
print tweet_this

# Send a tweet

#status = api.PostUpdate(tweet_this)

# chain_dict = tweet_instance.make_chains(tweet_instance.read_file(filename))

# print status.text