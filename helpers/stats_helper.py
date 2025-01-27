import pandas as pd
import numpy as np
import re
import string
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
            text = re.sub('['+string.punctuation+']', '', text)
            like_count = tweet[1]
            if not text.startswith('rt') and not np.isnan(like_count):
                    for word in text.split():
                        if word in word_dict:
                            word_dict[word][0] = word_dict[word][0] + 1
                            word_dict[word][1] = word_dict[word][1] + like_count
                        elif not ('http' in word or word.startswith('<u')):
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
            0]**5  # calculate avg likes by dividing total likes / occurrences
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
        word = re.sub('[' + string.punctuation + ']', '', word)
        if word in avg_like_dict:
            total_likes = total_likes + avg_like_dict[
                word]  # sum the avg likes of all the words
            words_used = words_used + 1
    if words_used == 0:
        return 0
    return total_likes / words_used**5.4


def predict_and_compare_likes(df_of_tweets, avg_like_dict, start, end):
    """
    Given a Dataframe of tweets and likes, the average like dictionary, 
    and indicies to start and end predicting, predicts the number of likes 
    a tweet will receive. Returns a list of tuples containing the text,
    predicted number of likes and actual number of likes. 
    
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

def is_accurate(predicted, actual):
    """
    Given the predicted number of likes and actual number of likes, computes whether the prediction is within some range of the actual value
    
    :param predicted:
    :param actual:
    :return:
    """
    diff = abs(predicted - actual)
    if diff < (1 * actual):
        return True

def get_percent_in_range(text_predicted_actual):
    """
    Given the entire dataset, computes the percent of predictions within range
    
    :param text_predicted_actual:
    :return:
    """
    total_acc = 0.0
    for tweet in text_predicted_actual:
        predicted = tweet[1]
        actual = tweet[2]
        tweet_acc = is_accurate(predicted, actual)
        if tweet_acc:
            total_acc = total_acc + 1
    return total_acc / len(text_predicted_actual) * 100



