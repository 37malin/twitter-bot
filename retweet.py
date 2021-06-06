import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#weet_list = api.favorites(screen_name='SharegaiOsusume', count=5)
#print(tweet_list)

#for tweet in tweet_list:
#    print(tweet.id)

#tweet_id = 1396813334637203456
#api.retweet(tweet_id)

for tweet in api.favorites(screen_name='SharegaiOsusume'):
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)
