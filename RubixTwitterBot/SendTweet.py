import tweepy

from config import *

#----------------------------------------------------------------------------------------------#

#Creator: ItsJustRubix

#Script: Sends a tweet to your account

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

api.update_status(status="Enter Tweet Here")

print('Finished')
