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
