import pandas as pd
import numpy as np
from group_19_package.group_19_support_func import *

##############################################################################
#function 1
def dictionary_of_metrics(data):
    '''
    parameters
    -----------
    data: input list of numbers.

    returns
    ----------
    a dictionary containing the mean, median, maximum, minimum, variance and the
        standard deviation
    '''

    if type(data) != list:
        raise TypeError('Not a list')

    for element in data:
        if isinstance(element, (str,bool)):
            raise ValueError('List should only contain numbers')

    if my_len(data)==0:
        raise ValueError('Empty list provided')

    sorted_list = my_sort(data)

    mean = my_mean(data)
    median = my_median(data)
    maximum = sorted_list[-1]
    minimum = sorted_list[0]
    variance  = my_var(data)
    std_dev = variance**0.5

    result_dict = {"mean":round(mean,2),'median':round(median,2),
                    'std':round(std_dev,2),'variance':round(variance,2),
                    'max':round(maximum,2),'min':round(minimum,2)}

    return result_dict

#######################################################################################
#funtion 2
def five_num_summary(items):
    '''
    This function returns the five number summary of the
    given items list.

    Parameters
    ----------
    items: a list of integers

    Returns
    -------
    a dictionary of the five number summary
    '''
    if type(data) != list:
        raise TypeError('Not a list')
    for element in items:
        if isinstance(element, (str,bool)):
            raise ValueError('List should only contain numbers')

    if my_len(data)==0:
        raise ValueError('Empty list provided')

    return {'max':max(items),
            'median':np.median(items),
            'min': min(items),
            'q1': np.quantile(items,0.25),
            'q3': np.quantile(items,0.75)}

########################################################################################
#function 3
def date_parser(dates):
    '''
    parameters
    -----------
    dates: dates including the times
    returns
    -----------
    This function returns the date without the time stamps
    '''
    if type(dates) != list:
        raise TypeError('Not a list')
    for numbers in dates:
        if isinstance(element, (int, float, bool)):
            raise ValueError("List should only contain a str") 
    if my_len(dates)==0:
        raise ValueError('Empty list provided')
    
    dates_only = []
    for date in dates:
        date_list = [date[:10],date[10:]]
        dates_only += [date_list[0]]

    return (dates_only)

#########################################################################################

#function 4
def extract_municipality_hashtags(df,mun_dict = mun_dict):
    '''
        Function takes in a data frame and dictionary of
        municipalilties and returns the municipality
        mentioned in the tweet as well as the all the hashtags.

        parameters
        ----------
        df: pandas dataframe
        mun_dict: municipality dictionary

        Returns
        ----------
        dataframe with added municipalities and hashtags fields.
    '''
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

        muni_per_tweet += [municipality]
        hashtags_per_tweet += [hash_tags]

    df['municipality'] = muni_per_tweet
    df['hashtags'] = hashtags_per_tweet

    return df

##########################################################################################
#function 5
def number_of_tweets_per_day(df):
    '''
    This function groups tweets based on the date they were posted and returns a dataframe
    with number of dates per day and dates columns.

    Parameters
    ----------
    df: Pandas dataframe

    Returns
    ---------
    dataframe
    '''
    #Adds a new column 'Dates' to dataframe df with dates in format HH:MM:SS
    df["Date"] = pd.to_datetime([date[:10] for date in df["Date"].to_list()])
    #Groups with 'Dates' and count the tweets into a new dataframe
    tweets_count_df = df.groupby(['Date']).size().reset_index(name='Tweets').set_index('Date')

    return(tweets_count_df)

##########################################################################################
#function 6
def word_splitter(df,column='Tweets'):
    '''
    Word splitter takes in a column from a data frame.
    The requested column will be broken down into a list of the
    individual words. The function will create a new column and
    insert the list into the new column.

    Parameters:
    __________________________________________________
    DataFrame

    Column from a DataFrame
    ______________________________________________________
    Returns :
    ___________________________________________________
    New column with the Splitted Tweets
    '''
    new_df=[my_split(i.lower()) for i in df[column]]
    df['Split tweets']= new_df
    return df

##########################################################################################
#function 7
def stop_words_http_remover(df,stop_words_dict='stop_words_dict'):
    '''
    replace split(), lower()
    This function removes stop words and urls from a Series of
    tweets in a dataframe. The df dataframe must have 'Tweets' column.

    Parameters
    ----------
    df: Pandas dataframe
    stop_words_dict: dictionary of stop words

    Returns
    -------
    dataframe
    '''
    #tokenising the strings
    df_col=[ my_split(x)   for x in df['Tweets']]
    #removing the stop words
    no_sw=[[ c.lower() for c in new if not(c.lower() in stop_words_dict['stopwords'])] for new in df_col]
    #removing the urls and insert it to twitter dictionary
    df['Without Stop Words']=[[ x for x in dflist if not('http' in x)] for dflist in no_sw]
    return df
