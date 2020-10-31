from helpers.data_helpers import *
from helpers.stats_helper import *

if __name__ == "__main__":
    # example
    d = parse_raw_data_csv("trump")
    parsed_df = get_simple_parsed_dataframe("trump")
    wordDict = create_word_occurence_like_dict(parsed_df, 0, 25000)

    avg_like_dict = calc_avg_likes(wordDict)

    prediction = predict_and_compare_likes(parsed_df, avg_like_dict, 25000, 50000)

    print(prediction)

    pass
