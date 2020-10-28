import pandas as pd

"""
This is for parsing and handling and basically anything you want to do with the data
"""


def parse_raw_data_csv(csv_string):
    """
    Takes filename of csv in /data and returns pandas object
    :param csv_string: filename
    :return: [pandas Dataframe] in list
    """
    if csv_string.find('russia') > -1:
        return [pd.read_csv('data/raw/russian_troll/tweets.csv'),
                pd.read_csv('data/raw/russian_troll/users.csv')]
    elif csv_string.find('avengers') > -1:
        return [pd.read_csv('data/raw/avengers_endgame/tweets.csv')]
    elif csv_string.find('trump') > -1:
        return [pd.read_csv(
            'data/raw/donald_trump_tweets/trump_tweets_10-24-2020.csv')]
    elif csv_string.find('top20') > -1:
        return [pd.read_csv('data/raw/top_20_tweeters/tweets.csv')]
    raise Exception('invalid CSV')
