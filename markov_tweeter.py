import os

import twitter

import markov_at_tweet #import TweetableMarkovGenerator

import sys

# Use Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# # This will print info about credentials to make sure they're correct
print api.VerifyCredentials()


if __name__ == "__main__":
    script, txt_filename = sys.argv

    tweet_bot_instance = markov_at_tweet.TweetableMarkovGenerator()
    tweet_bot_instance.char_lmt = 140


    chain_dict = tweet_bot_instance.make_chains(tweet_bot_instance.read_file(txt_filename))


    random_text = tweet_bot_instance.make_text(chain_dict)


    print random_text
#tweet_this = tweet_bot_instance.make_text(txt_filename)
#print random_text

# Send a tweet

    status = api.PostUpdate(random_text)

    # # chain_dict = tweet_instance.make_chains(tweet_instance.read_file(filename))

    print status.text