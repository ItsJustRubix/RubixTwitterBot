import tweepy

from config import *

#----------------------------------------------------------------------------------------------#

#Creator: ItsJustRubix

#Script: User account lookup

#License: MIT

#Bot Version: v0.5

#*NOTE* This bot is still in early development, It will be updated frequently.

#----------------------------------------------------------------------------------------------#

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Type username you want to get details on without the '@'
user = api.get_user('username')

print("Name:", user.name)
print("User id: ", user.id_str)
print("Description: ", user.description)
print("Location:",user.location)
print("Time zone: ", user.time_zone)
print("Number of Following:",user.friends_count)
print("Number of Followers:",user.followers_count)
print("Number of tweets: ", str(user.statuses_count))
