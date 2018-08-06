import tweepy

from config import *

#----------------------------------------------------------------------------------------------#

#Creator: ItsJustRubix

#Script: Retweets Tweets with a keyword

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

#Rewteets tweets with the supplied keyword
numberOfTweets = "25" #Number of tweets to retweet (Default is 25)

print('Retweeting Tweets')

search = "Keyword" #Put keyword here

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted The Tweet Succesfully')
    except tweepy.TweepError as e:
            print(e.reason)

    except StopIteration:
                break
