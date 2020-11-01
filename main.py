from helpers.stats_helper import *
import pickle


def run_prediction_and_pickle(data_string):
    # example
    parsed_df = get_simple_parsed_dataframe(data_string)

    wordDict = create_word_occurrence_like_dict(parsed_df, 0, 25000)

    avg_like_dict = calc_avg_likes(wordDict)

    prediction = predict_and_compare_likes(parsed_df, avg_like_dict, 25000,
                                           50000)
    with open('notebooks/'+data_string + '.pkl', 'wb') as f:
        pickle.dump(prediction, f)


if __name__ == "__main__":
    run_prediction_and_pickle('trump')
    run_prediction_and_pickle('avengers')
    run_prediction_and_pickle('russia')
    run_prediction_and_pickle('top20')
    print('done :)')
