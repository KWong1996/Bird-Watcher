import tweepy
import json
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Load in search criteria 
with open("criteria.json", "r") as read_file:
    data = json.load(read_file)

print(data.get("keywords")[0])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline(count = 1)

#for tweet in public_tweets:

    #Checks for tweets with links to specific websites
    #Improve it so that it can be from general domain
    #if(len(tweet.entities['urls']) >= 1):
    #   print(tweet.entities['urls'][0]['expanded_url'])