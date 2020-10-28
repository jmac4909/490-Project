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
        return [pd.read_csv('data/raw/avengers_endgame/tweets.csv',
                            encoding='cp1252')]
    elif csv_string.find('trump') > -1:
        return [pd.read_csv(
            'data/raw/donald_trump_tweets/trump_tweets_10-24-2020.csv')]
    elif csv_string.find('top20') > -1:
        return [pd.read_csv('data/raw/top_20_tweeters/tweets.csv')]
    raise Exception('invalid CSV')


def get_simple_parsed_dataframe(csv_string):
    """
    Return a normalized dataframe of (Text, Likes) for a given CSV
    :param csv_string: csv file
    :return: pandas dataframe
    """
    df = parse_raw_data_csv(csv_string)

    if csv_string.find('russia') > -1:
        return [
            df[0][['text', 'favorite_count']].copy().rename(
                columns={'favorite_count': 'likes'})]
    elif csv_string.find('avengers') > -1:
        return [
            df[0][['text', 'favoriteCount']].copy().rename(
                columns={'favoriteCount': 'likes'})]
    elif csv_string.find('trump') > -1:
        return [df[0][['text', 'favorites']].copy().rename(
            columns={'favorites': 'likes'})]
    elif csv_string.find('top20') > -1:
        return [df[0][['content', 'number_of_likes']].copy().rename(
            columns={'content': 'text', 'number_of_likes': 'likes'})]
    raise Exception('invalid CSV')
