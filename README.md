# Group_19_module

Group_19_module is a module housing multiple functions that perform analysis on the Eskom data and return key business metrics.

## Installation

Use the package manager [pip](https://github.com/Mikovhe/Group_19_JHB.git) to install group_19_module.

```bash
pip install group_19_package
```

## Usage

```python
from group_19_package import group_19_module as g_19

g_19.dictionary_of_metrics(data) # returns dictionary of business metrics
g_19.five_num_summary(items) # returns five number summary of data
g_19.date_parser(dates) # returns dates without the time stamp
g_19.extract_municipality_hashtags(df,mun_dict) #returns municipalities and hashtags from tweets
g_19.number_of_tweets_per_day(df) #returns dataframe showing number of tweets per day
g_19.stop_words_http_remover(df,stop_words_dict) # returns dataframe without stop and urls on 'Tweets' column

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[MIT](https://choosealicense.com/licenses/mit/)