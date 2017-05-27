import sys
import csv
import got
import urllib2
import tweepy
import json
import pymongo

# global config options
max_tweets = 100 # tweepy max = 100

def get_queries_from_file(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')
        queries = [row for row in reader]
    return queries

def get_ids_from_queries(queries):
    query_results = []

    for query in queries:
        querystr = query[0]
        datefromstr = query[1]
        datetostr = query[2]

        # set up the criteria
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(querystr).setSince(datefromstr).setUntil(datetostr).setLanguage("nl")
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        ids = [tweet.id for tweet in tweets]
        query_results += [[ query, ids ]]
    return query_results

def connect_to_twitter():
    secrets = json.load(open('auth.secrets'))
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_secret'])

    api = tweepy.API(auth)
    return api

def connect_to_database():
    # connect to the mongo database
    client = pymongo.MongoClient()
    database = client.tweets
    return database

def get_tweets_by_id(api, ids):
    # get the tweets in chunks of max_tweets
    first_tweet = 0
    last_tweet = max_tweets
    tweet_list = []
    while (len(ids) > first_tweet):
        last_tweet = min(len(ids), last_tweet)
        specific_ids = ids[first_tweet: last_tweet]
        print(specific_ids)
        specific_tweets = api.statuses_lookup(specific_ids, True)
        tweet_list += [x._json for x in specific_tweets]
        first_tweet = last_tweet
        last_tweet += max_tweets
        
    return tweet_list

def store_tweets(database, collection_name, tweets):
    collection = database[collection_name]
    result = collection.insert_many(tweets)
    return result


# First, get the ids from file (for now)
id_file = open("twitter_ids.txt")
all_ids = id_file.read().splitlines()
part_ids = all_ids #[0:getlength]

api = connect_to_twitter()
database = connect_to_database()
tweet_list = get_tweets_by_id(api, part_ids)
dbresult = store_tweets(database, 'kpn', tweet_list)
print(len(part_ids), len(dbresult.inserted_ids))
