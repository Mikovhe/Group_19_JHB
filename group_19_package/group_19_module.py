import pandas as pd
import numpy as np




###################################################################################
#support functions
def my_sort(data):
    sorting = True
    while sorting:
        data_copy = tuple(data)
        for i in range(1,len(data)):
            j = i-1

            if data[i]<data[j]:
                data = switch(data,i,j)

        if data_copy == tuple(data):
            sorting =False

    return(data)

def my_sum(numlist):
    total=0
    for num in numlist:
        total+=num
    return total


def my_len(data):
    count = 0
    for _ in data:
        count += 1
    return count

def my_median(num_list):
    s_list = my_sort(num_list)
    if my_len(s_list)%2 == 1:
        ind = int(my_len(s_list)/2)
        return s_list[ind]

    else:
        ind = int(my_len(s_list)/2)
        return (s_list[ind]+s_list[ind-1])/2


def switch(data,ind1,ind2):
    '''
        takes in a list and indices and switch places
        of values at those indices

    '''    
    #store the values to memory
    value_ind1 = data[ind1]
    value_ind2 = data[ind2]

    #assign values to new position
    data[ind1] = value_ind2
    data[ind2] = value_ind1

    return data


def my_mean(my_list):
    '''
    the function takes in a list of numeric values
    then returns the mean of the  list.
    '''
    return(my_sum(my_list)/my_len(my_list))


def my_var(nums):
    '''
    This function calculates the variance of the values in the list: nums
    Remember to replace the sum and len functions with our own functions
    '''
    mean=my_mean(nums)
    varnums=[(num-mean)**2 for num in nums]
    varvalue=my_sum(varnums)/(my_len(nums)-1)
    return varvalue
###################################################################################
#function 1
def dictionary_of_metrics(data):
    '''
    parameters
    -----------
    data: input list.

    returns
    ----------
    a dictionary containing the mean, median, maximum, minimum, variance and the
        standard deviation
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
    '''
    This function returns the five number summary of the 
    iterable list or tuple: items
    '''

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
        dates_only += [date_list[0]]

    return (dates_only)

#########################################################################################

#function 4
def extract_municipality_hashtags(df,mun_dict):
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
    
    df["Date"] = pd.to_datetime([date[:10] for date in df["Date"].to_list()])
    tweets_count_df = df.groupby(['Date']).size().reset_index(name='Tweets').set_index('Date')

    return(tweets_count_df)

##########################################################################################
#function 6
def word_splitter(df,column):
    '''
    Word splitter takes in a column from a data frame. 
    The requested column will be broken down into a list of the
    individual words. The function will create a new column and 
    insert the list into the new column. 
    '''
    new_df=[i.lower().split() for i in df[column]]
    df['Split tweets']= new_df
    return df

################################################################################
#function 7
def stop_words_http_remover(df,stop_words_dict):
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
    df_col=[ x.split()   for x in df['Tweets']]
    #removing the stop words
    no_sw=[[ c.lower() for c in new if not(c.lower() in stop_words_dict['stopwords'])] for new in df_col]
    #removing the urls and insert it to twitter dictionary
    df['Without Stop Words']=[[ x for x in dflist if not('http' in x)] for dflist in no_sw]
    return df
