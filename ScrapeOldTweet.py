import GetOldTweets3_local as got
import pandas as pd
import time, datetime

def crawl(tag, start_date, end_date):
    # Creation of query object
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(tag).setSince(str(start_date)) \
        .setUntil(str(end_date)).setEmoji("unicode")

    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Creating list of chosen tweet data
    if tweets is not None:
        text_tweets = [[tweet.author_id, tweet.username, tweet.formatted_date, tweet.date, tweet.text,
                        tweet.hashtags, tweet.mentions, tweet.retweets, tweet.to] for tweet in tweets]

    return text_tweets

def main():
    date_1 = "2020-04-23"
    headers = ["author_id", "username1", "formatted_date", "date", "text", "hashtags", "mentions", "retweets", "to"]
    list_of_hashtags = ["@citypfcalgary", "#pandemic", "#CoronaUpdate"]
    for tag in list_of_hashtags:
        start_date = end_date = datetime.datetime.strptime(date_1, "%Y-%m-%d").date()
        count = 0
        print("Start ------ " + tag)
        df_all = pd.DataFrame(columns=headers)
        filename = "output/Data_" + tag[1:] + ".csv"
        while end_date < datetime.date.today():
            end_date = start_date + datetime.timedelta(days=1)
            print("Start Start_date " + str(start_date))
            filename_temp = "output/Data_" + tag[1:] + "_" + str(count) +".csv"
            try:
                text_tweets = crawl(tag, start_date, end_date)
            except Exception as e:
                time.sleep(1200)
                try:
                    text_tweets = crawl(tag, start_date, end_date)
                except Exception as e:
                    print("Failed for Start_date " + str(start_date))

            if text_tweets is not None:
                df = pd.DataFrame(text_tweets, columns=headers)
                df.to_csv(filename_temp, index=False)
                df_all = df_all.append(df, ignore_index=True)
            time.sleep(600)
            count += 1
            start_date = end_date
        try:
            df_all['date'] = pd.to_datetime(df_all['date'])
            df_all.sort_values('date', inplace=True, ascending=False)
        except:
            print("Failed to sort the date column")
        df_all.to_csv(filename, index=False)
        print("End ----", tag)

main()
