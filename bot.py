import os
from time import sleep
import tweepy

# Load credentials
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_file = open('ginsberg.txt', 'r')
tweets = tweet_file.readlines()
tweet_file.close()

for tweet in tweets:
    print('Ginsberg Bot Says: {0}'.format(tweet))
    api.update_status('Ginsberg Bot Says: {0}'.format(tweet))
    sleep(5)
