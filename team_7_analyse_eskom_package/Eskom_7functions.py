import numpy as np
import pandas as pd


# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}


"""
To do:
- Refine functions
- Create package
- Add function descriptions
- Add error handling code
- Docstring (1-4 done)
- Complete test.py assertions
"""


# Function 1:

def dictionary_of_metrics(items):

    """Return dict of descriptive statistics:
            mean, median, sample std, sample var, min, and max.
    
    Args: 
        items (list): A list containing float values.
    
    Return:
        dict: dict of 7 key, value parins:
            {'name of stat': value rounded to 2 decimals, etc}.
    
    Example:
        Input: dictionary_of_mentrics([5,10,15,20,25,30])
        Output: {'mean': 17.5, 'median': 17.5, 'std': 9.35, 'var': 87.5, 'min': 5, 'max': 30}
    """

    dictionary = {'mean':0, 'median':0, 'std':0, 'var':0, 'min':0, 'max':0}
    dictionary['mean'] = np.mean(items).round(2)
    dictionary['median'] = np.median(items).round(2)
    dictionary['std'] = np.std(items, ddof=1).round(2)
    dictionary['var'] = np.var(items, ddof=1).round(2)
    dictionary['min'] = np.min(items).round(2)
    dictionary['max'] = np.max(items).round(2)
    return dictionary

# Function 2:

def five_num_summary(items):

    """Return dict of dexcriptive statistics:
            max, median, min, q1, and q3.
    
    Args: 
        items (list): A list containing float values.
    
    Return:
        dict: dict of 7 key, value parins:
            {'name of stat': value rounded to 2 decimals, etc}.
    
    Example:
        Input: five_num_summary([5,10,15,20,25,30])
        Output: {'max': 30, 'median': 17.5, 'min': 5, 'q1': 11.25, 'q3': 23.75}
    """

    dictionary = {'max':0, 'median':0, 'min':0, 'q1':0, 'q3':0}
    dictionary['max'] = np.max(items).round(2)
    dictionary['median'] = np.median(items).round(2)
    dictionary['min'] = np.min(items).round(2)
    dictionary['q1'] = np.percentile(items, 25).round(2)
    dictionary['q3'] = np.percentile(items, 75).round(2)
    return dictionary

# Function 3:

def date_parser(dates):

    """Return list strings in truncated DateTime format ('yyyy-mm-dd').
    
    Args: 
        dates (list): A list containing string values,
            each value in the (DateTime) format 'yyyy-mm-dd hh:mm:ss'.
    
    Return:
        list: List of strings in truncated DateTime format ('yyyy-mm-dd').
    
    Example:
        Input: date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53', '2019-11-29 12:46:10'])
        Output: ['2019-11-29', '2019-11-29', '2019-11-29']
    """
    out = [item[:10] for item in dates]
    return out

# Function 4:

def extract_municipality_hashtags(df):

    """Return input pandas DataFrame with two new columns('municipality' and 'hashtags').
    
    Args: 
        df (pandas(pd) DataFrame): pd.DataFrame object with at least one column:
            'Tweets': Contains strings (pd.Series objects) of individual tweets (one tweet per value).
    
    Return input pandas DataFrame with two new columns:
        'municipality': Contains name of municipality (lowercase) if present in 'Tweet' column (else NaN value).
        'hashtags': Contains hashtags (if present - lowercase) from 'Tweets' column (else NaN vlaue).
    """

    municipality_list = []
    hashtags_list = []
    
    for index, row in df.iterrows():
        split_tweets = row['Tweets'].split()
        row_mun_list = []
        row_hasht_list = []
        for word in split_tweets:
            if word in mun_dict:
                row_mun_list.append(word.lower())
            elif word[0] == '#':
                row_hasht_list.append(word.lower())
            else:
                pass
        municipality_list.append(row_mun_list)
        hashtags_list.append(row_hasht_list)
            
    df['municipality'] = municipality_list
    df['hashtags'] = hashtags_list
    df['municipality'] = df['municipality'].map(lambda word: np.nan if word == '[]' else word)
    df['hashtags'] = df['hashtags'].map(lambda word: np.nan if word == '[]' else word)
    
    return df

# Function 5:

def number_of_tweets_per_day(df):

    """Return new pd.DataFrame object with 'Date' as index column
        and 'Tweets' as column.
    
    Args: 
        df (pandas(pd) DataFrame): pd.DataFrame object with at least two columns:
            'Tweets': Contains strings (pd.Series objects) of individual tweets (one tweet per value).
            'Date': Column of DateTime objects stating DateTime of corresponding tweet.

    Return new pandas DataFrame with two new columns:
        'Tweets': Count of tweets per 'Date', from DataFrame.groupby().count().
        'Date' (index column): Column of truncated DateTime objects in 'yyyy-mm-dd' format.
    """
    date = [item.split(" ")[0] for item in df['Date'].values]
    df['Date'] = date
    df1 = df.groupby(df['Date']).count()
    return df1

# Function 6:

def word_splitter(df):
    Split = []
    for index, row in df.iterrows():
        split_tweets = row['Tweets'].split()
        split_tweets_lowercase = list(map(lambda x: x.lower(), split_tweets))
        split_tweets_list = Split.append(split_tweets_lowercase)
    df['Split Tweets'] = Split
    return df

# Function 7:

def stop_words_remover(df):
    Without_stopwords_list = []
    
    for index, row in df.iterrows():
        split_tweets = row['Tweets'].split()
        row_temp_list = []
        split_tweets_lowercase = list(map(lambda word: word.lower(), split_tweets))
        for word in split_tweets_lowercase:
            if word not in stop_words_dict['stopwords']:
                row_temp_list.append(word)
            else:
                pass
        Without_stopwords_list.append(row_temp_list)
        
            
    df['Without Stop Words'] = Without_stopwords_list

    return df