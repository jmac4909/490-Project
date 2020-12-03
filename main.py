from helpers.stats_helper import *
import pickle


def run_prediction_and_pickle(data_string, split, size):
    # example
    parsed_df = get_simple_parsed_dataframe(data_string)

    wordDict = create_word_occurrence_like_dict(parsed_df, 0, split)

    avg_like_dict = calc_avg_likes(wordDict)

    prediction = predict_and_compare_likes(parsed_df, avg_like_dict, split,
                                        size)

    accuracy = get_percent_in_range(prediction)

    print(accuracy)

    with open('notebooks/'+data_string + '.pkl', 'wb') as f:
        pickle.dump(prediction, f)


if __name__ == "__main__":
    run_prediction_and_pickle('trump', 25000, 50000)
    run_prediction_and_pickle('avengers', 5000, 10000)
    run_prediction_and_pickle('top20', 25000, 50000)
    run_prediction_and_pickle('russia', 7500, 15000)
    print('done :)')
