import tweepy
import json
from pprint import pprint
from itertools import islice

# global config options
max_tweets = 1  #tweepy max = 100

# First, set up authorization, using the secrets in auth.secrets

secrets = json.load(open('auth.secrets'))
auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'],secrets['access_secret'])

api = tweepy.API(auth)

# load first $maxtweets from file
with open("twitter_ids.txt") as id_file:
    ids = list(islice(id_file.read().splitlines(), max_tweets))

specific_tweets = api.statuses_lookup(ids, True)

for tweet in specific_tweets:
    pp = tweet._json
    pprint (pp)
