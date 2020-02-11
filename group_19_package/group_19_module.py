from group_19_support_func import *
import pandas as pd

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
 
 #funtion 2
 import numpy as np
 def five_num_summary(items):
    nlen=len(items)#replace the len
    med_ind=0 #median index initialise
    q1=0 #quartile 1
    q3=0 #quartile 3
    #this block passes
    items =sorted(items)
    if nlen%2==0 and nlen%4==0:#even length and quarter of length is int#########PASS
        q1=sum(items[int(nlen/4-1):int(nlen/4+1)])/2
        q3=sum(items[int(nlen*(3/4)-1):int(nlen*(3/4)+1)])/2
        
    elif nlen%2==0 and nlen%4!=0: #for even length and non even quartile######pass
        q1=items[nlen//4]
        q3=items[(nlen*3)//4]
        
    elif nlen%2!=0:#for the odd lengths
        med_ind=nlen//2+1
        
        print(type(med_ind/2))#checking the type of number when dividing a number
        print(med_ind/2)
        if med_ind%2==0: #when medindex is even
            q1=sum(items[med_ind//2-1:med_ind//2+1])/2
            print(q1)
            q3=sum(items[int(med_ind*(3/2))-2:int((med_ind*(3/2)))])/2
            print(q3)
        else:
            q1=sum(items[med_ind//2-1:med_ind//2+1])/2
            q3=sum(items[int(med_ind*(3/2)//1-1):int(med_ind*(3/2)//1)+1])/2
    return {'max':max(items),
            'median':np.median(items),
            'min': min(items),
            'q1': q1,
            'q3': q3} #change some to our functions
            #remember that when index you have to count from zero

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

#function 6
def word_splitter(df):
    new_df=[i.lower().split() for i in twitter_df['Tweets']]
    twitter_df['Split tweets']= new_df
    return twitter_df

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

