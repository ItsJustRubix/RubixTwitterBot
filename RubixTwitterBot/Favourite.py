import tweepy

from config import *

#----------------------------------------------------------------------------------------------#

#Creator: ItsJustRubix

#Script: Favourite Tweets That Has The Keyword

#License: MIT

#Bot Version: v0.5

#*NOTE* This bot is still in early development, It will be updated frequently.

#----------------------------------------------------------------------------------------------#
#Authentication
auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Login Status
user = api.me()
print('Logging In')
print('Account')
print('--------------------------------------------------------------')
print(user.name)
print('--------------------------------------------------------------')
print('Logged In Succesfully!')

#Favourites tweets with the supplied keyword
print('Favouriting Tweets')

search = "Keyword" #Put a keyword for bot to look for here


numberOfTweets = "25" #Number of tweets to favourite (Default is 25)

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favourite()
        print('Favourited The Tweet Succesfully')


    except tweepy.TweepError as e:
            print(e.reason)

    except StopIteration:
                break
