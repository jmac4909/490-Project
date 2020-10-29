import pandas as pd
import numpy as np
import sys
from helpers.data_helpers import *

def create_word_occurence_like_dict(df_of_tweets, start, end): #list of tweets is a list of tweet tuples (content, # of likes)
    "Given a list of tweets where the second element is a dataframe, returns a dict with the total occurences and total number of likes for each word"
    wordDict = {} #each key is a word that corresponds to (number of occurences of word, number of likes total in tweets containing word)
    for index, tweet in df_of_tweets[0].iterrows():
        if index >= start and index <= end:
            text = tweet[0].lower()
            like_count = tweet[1]
            if not np.isnan(like_count):
                for word in text.split():
                    if word in wordDict:
                        wordDict[word][0] = wordDict[word][0] + 1
                        wordDict[word][1] = wordDict[word][1] + like_count
                    else:
                        wordDict[word] = [1, like_count]
    return wordDict

def calc_avg_likes(wordDict):
    "Given a map of words with their # of occurences and # of total likes in tweets containing the word, returns a dict with the avg number of likes on a tweet containing that word"
    avg_like_dict = {} #each key is a word and value is avg # of likes a tweet with that word receives
    for word in wordDict:
        avg_likes = wordDict[word][1] / wordDict[word][0] # calculate avg likes by dividing total likes / occurences
        avg_like_dict[word] = avg_likes
    return avg_like_dict

def predict_likes(tweet_text, avg_like_dict):
    "Given some string and the dictionary of avg likes on a word, predict the number of likes the tweet will receive"
    tweet_as_list = tweet_text.split() #get tweet as list of words
    total_likes = 0
    words_used = 0
    for word in tweet_as_list:
        if word in avg_like_dict:
            total_likes = total_likes + avg_like_dict[word] #sum the avg likes of all the words
            words_used = words_used + 1
    if words_used == 0:
        return 0
    return total_likes / words_used #return the avg likes of a word averaged over all the words in the tweet

def predict_and_compare_likes(df_of_tweets, avg_like_dict, start, end):
    text_predicted_actual = []
    for index, tweet in df_of_tweets[0].iterrows():
        if index >= start and index <= end:
            text = tweet[0].lower()
            like_count = tweet[1]
            if not np.isnan(like_count):
                predicted = predict_likes(text, avg_like_dict)
                text_predicted_actual.append([text, predicted, like_count])
    return text_predicted_actual

parsed_df = get_simple_parsed_dataframe("trump")

wordDict = create_word_occurence_like_dict(parsed_df, 0, sys.maxsize)

avg_like_dict = calc_avg_likes(wordDict)

tweet = "this is going to be a really bad bad bad ending"

# print("\nexamples/tests")
# print("\nwordDict: ", wordDict)
# print("\navg_like_dict: ", avg_like_dict)
# print("\npredicted likes in tweet: ", tweet, predict_likes(tweet, avg_like_dict))

