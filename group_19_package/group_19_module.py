from group_19_support_func import *

def dictionary_of_metrics(data):
    sorted_list = my_sort(data)

    mean = my_mean(data)
    median = my_median(data)
    maximum = sorted_list[-1]
    minimum = sorted_list[0]
    variance  = my_var(data)
    std_dev = variance**0.5

    result_dict = {"mean":round(mean,2),'median':round(median,2),
                    'standard deviation':round(std_dev,2),'variance':round(variance,2),
                    'maximum':round(maximum,2),'minimum':round(minimum,2)}

    return result_dict

def extract_municipality_hashtags(df):
    # your code here
    muni_per_tweet = []
    hashtags_per_tweet = []

    for tweet in df['Tweets']:
        tweet_list = tweet.split()
        hash_tags = [word.lower() for word in tweet_list if word[0]=='#']
        handles = [word for word in tweet_list if word[0]=='@']

        if hash_tags ==[]:
            hash_tags = np.nan

        municipality = np.nan

        for handle in handles:
            mun_handle = ''
            for char in handle:
                if mun_handle in mun_dict:
                    municipality = mun_dict[mun_handle]

                mun_handle +=char

        muni_per_tweet.append(municipality)
        hashtags_per_tweet.append(hash_tags)

    df['municipality'] = muni_per_tweet
    df['hashtags'] = hashtags_per_tweet

    return df
