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


#tests that require dataframes are tedious to do
