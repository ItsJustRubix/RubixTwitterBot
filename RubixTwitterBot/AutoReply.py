import tweepy

from config import *

#----------------------------------------------------------------------------------------------#

#Creator: ItsJustRubix

#Script: Auto Reply To Tweets

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

twt = api.search(q="Hello World")

#Keyword to look for in tweets
txt = ['Hello world!',
    'Hello World!',
    'Hello World!!!',
    'Hello world!!!',
    'Hello, world!',
    'Hello, World!']

for st in twt:
	for s in txt:
		if s == st.text:
			usr = st.user.screen_name
			msg = ("@%s Hello!" %(usr))
			st = api.update_status(msg, st.id)
print('Finished')
			
