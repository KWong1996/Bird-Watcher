import tweepy
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline(count = 10)
for tweet in public_tweets:

    #Checks for tweets with links to specific websites
    #Improve it so that it can be from general domain
    if(len(tweet.entities['urls']) >= 1):
        print(tweet.entities['urls'][0]['expanded_url'])