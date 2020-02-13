from group_19_support_func import *
import pandas as pd
import numpy as np

###################################################################################
#function 1
def dictionary_of_metrics(data):
    '''
        Function takes a list of numbers as parameter and returns
         a dictionary containing the mean, median, maximum, minimum, variance and the
        standard deviation...

        Example: dictionary_of_metrics([1,2,3,4,5]) == {"mean":3.0,"median":3.0,
                    }
    '''
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

#######################################################################################
#funtion 2
def five_num_summary(items):

    return {'max':max(items),
            'median':np.median(items),
            'min': min(items),
            'q1': np.quantile(items,0.25),
            'q3': np.quantile(items,0.75)}

########################################################################################
#function 3
def date_parser(dates):
    dates_only = []
    for date in dates:
        date_list = [date[:10],date[10:]]
        dates_only.append(date_list[0])

    return (dates_only)

#########################################################################################

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

##########################################################################################
#function 5
def number_of_tweets_per_day(df):
    # your code here
    df["Date"] = pd.to_datetime([date[:10] for date in df["Date"].to_list()])
    tweets_count_df = df.groupby(['Date']).size().reset_index(name='Tweets').set_index('Date')

    return(tweets_count_df)

##########################################################################################
#function 6
def word_splitter(df):
    '''
    Word splitter takes in a column from a data frame. 
    The requested column will be broken down into a list of the
    individual words. The function will create a new column and 
    insert the list into the new column. 
    '''
    new_df=[i.lower().split() for i in df['Tweets']]
    df['Split tweets']= new_df
    return df

###########################################################################################
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
