def create_word_occurence_like_dict(list_of_tweets): #list of tweets is a list of tweet tuples (content, # of likes)
    "Given a list of tweets in the format (content, likes), returns a dict with the total occurences and total number of likes for each word"
    wordDict = {} #each key is a word that corresponds to (number of occurences of word, number of likes total in tweets containing word)
    for tweet in list_of_tweets:
        for word in tweet[0].split(): #tweet[0] is actual content of tweet as string
            if word in wordDict:
                wordDict[word][0] = wordDict[word][0] + 1
                wordDict[word][1] = wordDict[word][1] + tweet[1]
            else:
                wordDict[word] = [1, tweet[1]]
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
    return total_likes / words_used #return the avg likes of a word averaged over all the words in the tweet

wordDict = create_word_occurence_like_dict( [("gee i hope this works work g this", 9), ("this is a really bad tweet", 2), ("no tweets are really bad, some just dont find their audience", 12), ("this tweet uses some words that are not bad but work", 7) ])

avg_like_dict = calc_avg_likes(wordDict)

tweet = "this is going to be a really bad bad bad ending"

print("\nexamples/tests")
print("\nwordDict: ", wordDict)
print("\navg_like_dict: ", avg_like_dict)
print("\npredicted likes in tweet ", tweet, predict_likes(tweet, avg_like_dict))

