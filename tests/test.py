import pandas as pd
import numpy as np
from group_19_package import group_19_module




def test_dictionary_of_metric():
    '''make sure dictionary_of_metrics works'''

    assert group_19_module.dictionary_of_metrics([1,2,3,4,5])=={'mean':3.0,'median':3, 'std': 1.58,'variance':2.5,'max':5,'min':1}
    assert group_19_module.dictionary_of_metrics([7, 8, 5, 2, 5, 9, 5, 4, 8, 6])=={'mean': 5.9, 'median': 5.5, 'std': 2.13, 'variance': 4.54, 'max': 9, 'min': 2}

#test_dictionary_of_metric()
#add tests for other functions
def test_five_number_summary():
    '''make sure test_five_number_summary works'''

    assert group_19_module.five_num_summary([1,2,3,4,5]) == {'min': 1, 'q1': 2.0, 'median': 3.0, 'q3': 4.0, 'max': 5}
    assert group_19_module.five_num_summary([7, 8, 5, 2, 5, 9, 5, 4, 8, 6])=={'min': 2,'q1': 5.0, 'median':5.5,'q3': 7.75, 'max': 9}

def test_date_parser():
    '''make sure the date parser works'''
    assert group_19_module.date_parser(['2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10']) == ['2019-11-29',
    '2019-11-29',
    '2019-11-29']


Tweets=['@thulamela #loadsheding is a problem #mukovhe do your job', '@ekhuruleni #izinyokaproblems bring our copper', '@polokwane #toomanytsotsi ba nyakile go nhlaba ka mphaka please help ','did jesus make it to northcliff']
Date=['2019-02-23 12:56:53','2019-02-23 11:56:53','2018-05-23 12:56:53','2017-02-23 12:56:53']
df1={
    'Tweets': Tweets,
    'Date': Date
}
df=pd.DataFrame(df1)
dict1={
    '@thulamela':'thulamela',
    '@polokwane':'polokwane',
    '@ekhuruleni':'ekhuruleni'
}

def test_extract_munipality_hashtags():
    assert group_19_module.extract_municipality_hashtags(df.copy(),dict1).loc[0, "hashtags"]==['#loadsheding', '#mukovhe']

def test_number_of_tweets_per_day():
    assert group_19_module.number_of_tweets_per_day(df.copy())['Tweets'][0]==1

def test_word_splitter():
    assert group_19_module.word_splitter(df.copy()).loc[0, "Split tweets"]==['@thulamela',
    '#loadsheding',
    'is',
    'a',
    'problem',
    '#mukovhe',
    'do',
    'your',
    'job']

def test_stop_words_http_remover():

    stop_words_dict={'stopwords': ['problem', 'bring','make']}

    assert group_19_module.stop_words_http_remover(df.copy(),stop_words_dict).loc[0, "Without Stop Words"]==['@thulamela', '#loadsheding', 'is', 'a', '#mukovhe', 'do', 'your', 'job']
