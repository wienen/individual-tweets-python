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