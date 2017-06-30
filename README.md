# Get Tweets by id

This small piece of code expect a list of tweet ids, possibly gotten through 
[GetOldTweets-python](https://github.com/Jefferson-Henrique/GetOldTweets-python).

## Authentication
The code expects a json file containing the twitter secrets for the account you are using. Format:

```
{
    "consumer_key"    : <<your consumer key>>,
    "consumer_secret" : <<your consumer secret>>,
    "access_token"    : <<your access token>>,
    "access_secret"   : <<your access secret>>
}
```

## Way of work
The idea is as follows: the user provides a csv file with three fields (query, date 
from and date to). The software will then get the ids from the tweets fulfilling
those criteria using the GetOldTweets-python code in the module `got3`.

After obtaining the ids, the software will get the full tweets using twitters API
through `tweepy`, sending the json code straight to the mongo database, in database
`tweets` and collection `query`, changing spaces to `-`-characters.

## Invocations
Using the file `../../TweetHistory/incident_dates.txt` (from the incident database), invoke the 
GetOldTweets command line generator `../../TweetHistory/get_dates.py`.  This will create a shell script
(as stored in `../../TweetHistory/gettweets.sh`). This shell script will get the tweets from twitter
(not all tweets, still need to assess % of tweets returned) and store them in csv files.
The file `./ids_from_tweets.py` will extract the ids and print them to the command line, as in
`twitter_ids.txt`. These ids can then be processed by `download_tweets.py`.

## Opportunities for improvement
1. Add stuff in TweetHistory to the module in this directory
1. Do not use the command line as an intermediate step
1. Create a module for this
1. Add incident id to the information in the list of tweets so that the tweet can be linked to a single incident
Note: the actual incident information cannot be part of the database as this is confidential information
1. Add all to heroku
