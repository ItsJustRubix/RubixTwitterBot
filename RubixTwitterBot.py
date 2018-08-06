import tweepy

#----------------------------------------------------------------------------------------------#

#Creator: ItsJustRubix

#Script: Multi-Purpose Twitter Bot

#License: MIT

#Bot Version: v0.01a

#*NOTE* This bot is still in early development, It will be updated frequently.

#----------------------------------------------------------------------------------------------#
#To create an app go to the following: https://apps.twitter.com/app/new
#Once created go into your app and get your Keys & Tokens

#As of July 2018 Twitter doesn't allow you to make a application without applying for a Developer Account to gain access to the API

consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_token = 'XXXX' 
access_token_secret = 'XXXX'

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

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

print('Finished All Tasks Succesfully')
