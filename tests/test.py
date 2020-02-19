from group_19_package import group_19_module



def test_dictionary_of_metric():
    '''make sure dictionary_of_metrics works'''

    assert group_19_module.dictionary_of_metrics([1,2,3,4,5])== {'mean':3.0,
    'median':3, 'std': 1.41,'variance':2.0,'max':5,'min':1}
    assert group_19_module.dictionary_of_metrics([7, 8, 5, 2, 5, 9, 5, 4, 8, 6])==
    {'mean': 5.9, 'median': 5.5, 'std': 2.02, 'variance': 4.09, 'max': 9, 'min': 2}


#add tests for other functions
def test_five_number_summary():
    '''make sure test_five_number_summary works'''

    assert group_19_module.test_five_number_summary([1,2,3,4,5]) ==
    {'min': 1, 'q1': 2.0, 'median': 3.0, 'q3': 4.0, 'max': 5}
    assert group_19_module.dictionary_of_metrics([7, 8, 5, 2, 5, 9, 5, 4, 8, 6])==
    {'mean': 5.9, 'median': 5.5, 'std': 2.02, 'variance': 4.09, 'max': 9, 'min': 2}

def test_date_parser():
    '''make sure the date parser works'''
    assert group_19_module.date_parser(['2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10']) == ['2019-11-29',
    '2019-11-29',
    '2019-11-29']


Tweets=['@thulamela #loadsheding is a problem #mukovhe do your job', '@ekhuruleni #izinyokaproblems bring our copper', '@polokwane #toomanytsotsi ba nyakile go nhlaba ka mphaka please help ','did jesus make it to northcliff']
Dates=['2019-02-23 12:56:53','2019-02-23 11:56:53','2018-05-23 12:56:53','2017-02-23 12:56:53']
df1={
    'Tweets': Tweets,
    'Dates': Dates
}
df=pd.DataFrame(df1)
dict1={
    '@thulamela':'thulamela',
    '@polokwane':'polokwane',
    '@ekhuruleni':'ekhuruleni'
}

def test_extract_munipality_hashtags():
    result=df.copy()
    result['municipality']= ['thulamela','ekhuruleni','polokwane', 'NaN']
    result['hashtags']=[['#loadsheding','#mukovhe'], ['#izinyokaproblems'], ['#toomanytsotsi'],'NaN']
    assert group_19_module.extract_munipality_hashtags(df,dict1)==result

def test_number_of_tweets_per_day():
    resu={
    'Date': ['2019-02-23','2018-05-23','2017-02-23'],
    'Tweets' : [2,1,1]
    }
    result=pd.DataFrame(resu)
    result=result.set_index('Date')
    assert group_19_module.number_of_tweets_per_day(df)==result

def test_word_splitter():
    reslist=[sentence.split() for sentence in Tweets]
    func6fd = df.copy()
    func6fd['Split Tweets'] = [sentence.split() for sentence in Tweets]
    assert group_19_module.word_splitter(df)==func6fd

def test_stop_words_http_remover():
    func7fd = df.copy()
    dm=[['@thulamela',
    '#loadsheding',
    'is',
    'a',
    '#mukovhe',
    'do',
    'your',
    'job'],
    ['@ekhuruleni', '#izinyokaproblems', 'our', 'copper'],
    ['@polokwane',
    '#toomanytsotsi',
    'ba',
    'nyakile',
    'go',
    'nhlaba',
    'ka',
    'mphaka',
    'please',
    'help'],
    ['did', 'jesus', 'it', 'to', 'northcliff']]
    stop_words_dict={'stopwords': ['problem', 'bring','make']}
    func7fd['Without Stop Words']=dm
    assert group_19_module.stop_words_http_remover(df)==func7fd



