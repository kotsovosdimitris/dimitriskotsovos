from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy

consumer_key = 'BbLi4xrg5DyVhrXixL4IHhOXN'
consumer_secret = 'mmO3DG6jdMrFY0nwpYvtZZkG7vI5nIqDSlDNr6nUFtjS0qzqi1'
access_token = '2574978056-0fhfgc3upQlVt4LjLPp10xuKywtwhGFOca7d5BD'
access_secret = 's5AneiEbyivRcP3LivzEqxloJM1HjnOmUYEx7TzCxHdfp'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

screen_name = input("Give the name of the first user: ")
screen_name2 = input("Give the name of the second user: ")

try:
    new_tweets = api.user_timeline(screen_name = screen_name,count=50, tweet_mode="extended")
    tweets = [[tweet.full_text] for tweet in new_tweets]
    sum = 0

    new_tweets2 = api.user_timeline(screen_name = screen_name2,count=50, tweet_mode="extended")
    tweets2 = [[tweet2.full_text] for tweet2 in new_tweets2]
    sum2 = 0

    for i in range(0,50):
        listToStr = ' '.join([str(elem) for elem in tweets[i]])
        position = listToStr[listToStr.find(":")+1:]
        sum = sum + len(position.split())

        listToStr2 = ' '.join([str(elem2) for elem2 in tweets2[i]])
        position2 = listToStr2[listToStr2.find(":")+1:]
        sum2 = sum2 + len(position2.split())

    if(sum>sum2):
        print("the user with the more words in their tweets is the", screen_name, "with ", sum, "words")

    elif(sum==sum2):
        print("they have the same number of words")
    else:
        print("the user with the more words in their tweets is the", screen_name2, "with ", sum2, "words")
except Exception as e:
    print("Something is going Wrong! Please try again!")
