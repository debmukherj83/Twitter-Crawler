import pandas as pd
import os
import numpy as np

def Consolidate(tags):
    headers = ["author_id", "username1", "formatted_date", "date", "text", "hashtags", "mentions", "retweets", "to"]
    df_all = pd.DataFrame(columns=headers)

    for file_no in range(121):  # if the number of files for each hashtag is more than 15, increase the number accordingly
        filename = "output/Data_" + tags[1:] + "_" + str(file_no) + ".csv"

        if os.path.exists(filename):
            df1 = pd.read_csv(filename)
            df_all = df_all.append(df1, ignore_index=True)

    out_filename = "output/Data_" + tags[1:] + "_" + "Total.csv"
    df_all['date'] = pd.to_datetime(df_all['date'])
    df_all.sort_values('date', inplace=True, ascending=False)
    df_all = df_all.replace(np.nan, ' ', regex=True)
    df_all.to_csv(out_filename, header=headers, index=False)

list_of_hashtags = ["#pandemic"]
for tags in list_of_hashtags:
    Consolidate(tags)

