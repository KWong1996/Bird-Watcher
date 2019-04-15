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


tweets = []

saved_tweets = open('tweets.json', 'w')

# Search through timelines for tweets containing certain text
def find_keywords(keywords):

    for term in keywords:

        for tweet in public_tweets:

            if(term in tweet.text):
                tweets.append(tweet._json)


# Search through timelines for tweets linking to specific domains
def find_websites(websites):
    
    print(*websites)


# Search through timelines for tweets containing media
def find_media(media):

    if media == True:

        for tweet in public_tweets:
            
            # Look through the tweet object and confirm if they have a media object
            value = tweet.entities.get('media')

            if value != None:
                tweets.append(tweet._json)


# Load in search criteria 
with open("criteria.json", "r") as read_file:
    data = json.load(read_file)
    #print(data.items())


# Iterate through every key in the search criteria and call respective functions if they aren't empty   
for key in data:

    # Call text function
    if(key == "keywords"):
        find_keywords(data["keywords"])

    # Call domain function
    if(key == "websites"):
        find_websites(data["websites"])

    # Call media function
    if(key == "media"):
        find_media(data["media"])


json.dump(tweets, saved_tweets, indent=4)

print(len(tweets))

saved_tweets.close()


#for tweet in public_tweets:

    #Checks for tweets with links to specific websites
    #Improve it so that it can be from general domain
    #if(len(tweet.entities['urls']) >= 1):
       #print(tweet.entities['urls'][0]['expanded_url'])