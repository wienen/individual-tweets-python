import tweepy
import json

# First, set up authorization, using the secrets in auth.secrets

secrets = json.load(open('auth.secrets'))
auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'],secrets['access_secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
        print (tweet.text)
