import pandas as pd
import numpy as np
import sys
from helpers.data_helpers import *


def create_word_occurrence_like_dict(df_of_tweets, start,
                                     end):
    """
    Given a list of tweets, returns a dict with the total
    occurrences and total number of likes for each word

    :param df_of_tweets: list of df is a list of tweets
    :param start: start index
    :param end: end index
    :return: bag of words dict
    """
    # each key is a word that corresponds to
    # (number of occurrences of word, number of likes total
    # in tweets containing word)
    word_dict = {}
    for index, tweet in df_of_tweets[0].iterrows():
        if start <= index <= end:
            text = tweet[0].lower()
            like_count = tweet[1]
            if not text.startswith('rt') and not np.isnan(like_count):
                    for word in text.split():
                        if word in word_dict:
                            word_dict[word][0] = word_dict[word][0] + 1
                            word_dict[word][1] = word_dict[word][1] + like_count
                        else:
                            word_dict[word] = [1, like_count]
    return word_dict


def calc_avg_likes(word_dict):
    """
    Given a map of words with their # of occurences and # of total likes
    in tweets containing the word, returns a dict with the
     avg number of likes on a tweet containing that word

    :param word_dict: bag of words dict
    :return: dict
    """

    # each key is a word and value is avg #
    # of likes a tweet with that word receives
    avg_like_dict = {}
    for word in word_dict:
        avg_likes = word_dict[word][1] / word_dict[word][
            0]  # calculate avg likes by dividing total likes / occurrences
        avg_like_dict[word] = avg_likes
    return avg_like_dict


def predict_likes(tweet_text, avg_like_dict):
    """
    Given some string and the dictionary of avg likes on a word,
    predict the number of likes the tweet will receive

    :param tweet_text:
    :param avg_like_dict:
    :return: the avg likes of a word averaged over all the words in the tweet
    """

    tweet_as_list = tweet_text.split()  # get tweet as list of words
    total_likes = 0
    words_used = 0
    for word in tweet_as_list:
        if word in avg_like_dict:
            total_likes = total_likes + avg_like_dict[
                word]  # sum the avg likes of all the words
            words_used = words_used + 1
    if words_used == 0:
        return 0
    return total_likes / words_used


def predict_and_compare_likes(df_of_tweets, avg_like_dict, start, end):
    """
    ...
    :param df_of_tweets:
    :param avg_like_dict:
    :param start:
    :param end:
    :return:
    """
    text_predicted_actual = []
    for index, tweet in df_of_tweets[0].iterrows():
        if start <= index <= end:
            text = tweet[0].lower()
            like_count = tweet[1]
            if not np.isnan(like_count) and not text.startswith("rt "):
                predicted = predict_likes(text, avg_like_dict)
                text_predicted_actual.append([text, predicted, like_count])
    return text_predicted_actual
