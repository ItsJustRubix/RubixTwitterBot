import tweepy

from config import *

#----------------------------------------------------------------------------------------------#

#Creator: ItsJustRubix

#Script: #Follows Everyone Who Is Currently Following you

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


#Follows Everyone Who Is Currently Following you
def mainFunction():
    print('Following All Users Who Follow')
for follower in tweepy.Cursor(api.followers).items():
    try:
        follower.follow()
print("Followed everyone that is following" + user.name)
