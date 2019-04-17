import tweepy
import json
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.home_timeline(count = 20)


all_tweets = {}

tweets = []

saved_tweets = open('tweets.json', 'a+')

# Search through timelines for tweets containing certain text
def find_keywords(keywords):

    all_tweets['Keywords'] = []

    for term in keywords:

        for tweet in public_tweets:

            if(term in tweet.text):
                all_tweets['Keywords'].append(tweet._json)


# Search through timelines for tweets linking to specific domains
def find_websites(websites):
    
    all_tweets['Websites'] = []

    for term in websites:

        for tweet in public_tweets:

            #check size of 'urls' to see if it is non-empty
            if(len(tweet.entities['urls']) >= 1):

                if term in tweet.entities['urls'][0]['expanded_url']:
                    all_tweets['Websites'].append(tweet._json)


# Search through timelines for tweets containing media
def find_media(media):

    all_tweets['Media'] = []

    if media == True:

        for tweet in public_tweets:
            
            # Look through the tweet object and confirm if they have a media object
            value = tweet.entities.get('media')

            if value != None:
                all_tweets['Media'].append(tweet._json)


# Load in search criteria 
with open("criteria.json", "r") as read_file:
    data = json.load(read_file)


# Iterate through every key in the search criteria and call respective functions if they aren't empty   
for key in data:

    # Call text function
    if(key == "keywords"):
        find_keywords(data["keywords"])

    # Call domain function
    elif(key == "websites"):
        find_websites(data["websites"])

    # Call media function
    elif(key == "media"):
        find_media(data["media"])


json.dump(all_tweets, saved_tweets, indent=4)

# Print staement to check how many tweets have matched search criteria
#print(len(tweets))

saved_tweets.close()