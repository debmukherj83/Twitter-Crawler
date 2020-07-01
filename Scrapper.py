import time
import tweepy
import csv
from tweepy import TweepError
import pandas as pd
####input your credentials here


consumer_key = 'CSR9N8I5xw5gpcWvYymlKIkr5'
consumer_secret = 'AHByA2UqgwsusIJ381fE19zX0XMvt65B9HAe6a7fsoQKgPBVts'
access_token = '952206673069797376-MF9HrFs0QbX9EDolfBl2nSy3nAZVfPj'
access_token_secret = 'nARKc1QypMD6mN7cnjQ2t0eK6438KXCZONxNOHm2tLpTJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, timeout=1)
##### Shooting hashtags
##
# Open/Create a file to append data

# list_of_hashtags = ["#schoolshooting", "#EnoughisEnough", "#GunControlNow", "#SantaClarita", "#SantaClaritaShooting",
#                     "#SantaClaritaStrong", "#SaugusHighSchool", "#PrayForSaugus", "#gunreform", "#GunReformNOW",
#                     "#BanBullets", "#Shooting", "#california", "#SanDiego", "#CaliforniaShooting", "#Fresno",
#                     "#California #MassShooting", "#ACTIVESHOOTER"]

list_of_hashtags = ["#COVIDyyc"]

for tag in list_of_hashtags:
    filename = "output/Data_"+tag[1:]+".csv"

    # tweets = []
    # for tweet in api.search(q=tag, count=1000):
    #     tweets.append((tweet.created_at, tweet.id, tweet.text))

    with open(filename, 'a', newline='') as wr:
        csvWriter = csv.writer(wr)
        try:
            tt = tweepy.Cursor(api.search, q=tag, lang="en", until="2020-06-26", tweet_mode="extended").items(100)
            for tweet in tt:
                # if "retweeted_status" in dir(tweet):
                if hasattr(tweet, "retweeted_status"):
                    csvWriter.writerow([tag, tweet.created_at, tweet.retweeted_status.full_text.encode('utf-8')])
                else:
                    csvWriter.writerow([tag, tweet.created_at, tweet.full_text.encode('utf-8')])
        except TweepError as e:
            if "Failed to send request:" in e.reason:
                time.sleep(180)
                continue
        wr.close()
