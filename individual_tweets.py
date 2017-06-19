import tweepy
import json
from pprint import pprint
from itertools import islice
import pymongo

# global config options
max_tweets = 100  #tweepy max = 100
max_iterations = 1

# First, set up authorization, using the secrets in auth.secrets

secrets = json.load(open('auth.secrets'))
auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_secret'])

api = tweepy.API(auth)

# connect to the mongo database
client = pymongo.MongoClient()
database = client.tweets
collection = database.historic_tweets

# load first $maxtweets from file
with open("twitter_ids.txt") as id_file:
    start_pos = 0
    iteration = 1
    
    # read all ids
    all_ids = id_file.read().splitlines()
    ids = list(islice(all_ids, start_pos, start_pos + max_tweets))
    while (len(ids) > 0):
        specific_tweets = api.statuses_lookup(ids, True)
        tweet_list = [x._json for x in specific_tweets]
        res = collection.insert_many(tweet_list)
        print(res.inserted_ids)
        start_pos += max_tweets
        iteration += 1
        ids = list(islice(all_ids, start_pos, start_pos + max_tweets))
