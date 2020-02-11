from group_19_support_func import *

#function 1
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
 
 
#function 4
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

#function 5
def number_of_tweets_per_day(df):
    # your code here
    df["Date"] = pd.to_datetime([date[:10] for date in df["Date"].to_list()])
    tweets_count_df = df.groupby(['Date']).size().reset_index(name='Tweets').set_index('Date')
    
    return(tweets_count_df)

#function 7
def stop_words_http_remover(df):  
    '''
    replace split(), lower()
    '''      
    #tokenising the strings
    df_col=[ x.split()   for x in df['Tweets']]
    #removing the stop words
    no_sw=[[ c for c in new if not(c.lower() in stop_words_dict['stopwords'])] for new in df_col]
    #removing the urls and insert it to twitter dictionary
    df['Without Stop Words']=[[ x for x in dflist if not('http' in x)] for dflist in no_sw]
    return df

