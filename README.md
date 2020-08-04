# mypackage 
---

This package contains 7 functions (details below) that satisfy the requirements of the Analyse Sprint Predict.
Standard code refinement has been applied selectively, trading refinement off with readability when no large benefit (computational resources) was possible.

## Function details
----
-Refer to docstring or copy/paste docstring?
-Short description

Function 1: dictionary_of_metrics
    - Given a list that contains only numerical entries. Calculate: mean, median, variance, standard deviation, minimum and maximum.
    - See docstring ([SHIFT]+[TAB]) for deatils

Function 2: five_num_summary
    - Given a list that contains only numerical entries. Takes in a list of integers and return a dictionary of : max, median, min, q1 and q3.
    - see docstring ([SHIFT]+[TAB]) for details.

Function 3: date_parser
     - return a list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.
     - See docstring ([SHIFT]+[TAB]) for details

Function 4: extract_municipality_hashtags
    - Processes pandas dataframe (twitter data) to extract municipalities and hashtags contained in tweets.
    - See docstring ([SHIFT]+[TAB]) for details.


Function 5: number_of_tweets_per_day
    - Processes pandas dataframe (twitter data) to extract the number of tweets per day.
    - See docstring ([SHIFT]+[TAB]) for details.

Function 6: word_splitter
	- Processes pandas DataFrame (twitter data) and adds a new column with tweets as list of words.
	- See docstring ([SHIFT]+[TAB]) for details.  

Function 7: stop_words_remover
	- Processes pandas Dataframe (twitter data) and removes all [English] stop words and retuunrs a new column 'Without Stop Words'.
	- See docstring ([SHIFT]+[TAB]) for details.  

<span style="color: gray;">pip git+https://github.com/bmqhamane/team_7_analyse_eskom.git</span> 

## Where to get this package
---- 
The source code for this package is hosted on github: git+https://github.com/bmqhamane/team_7_analyse_eskom_package.git

<span style="color: gray;">python setup.py sdist</span> 


## Installing this package from Github
----
<span style="color: gray;">pip git+https://github.com/bmqhamane/team_7_analyse_eskom.git</span> 

### Updating this package from Github
----
<span style="color: gray;">pip install --upgrade git+https://github.com/bmqhamane/team_7_analyse_eskom.git</span> 

## How to use this package
----
-describe usage and cases

<span style="color: gray;">pip install --upgrade git+https://github.com/bmqhamane/team_7_analyse_eskom.git</span> 

## Authors
----
-names alphabetically with email addrs

<span style="color: gray;">pip git+https://github.com/bmqhamane/team_7_analyse_eskom.git</span> 

License
MIT

[![EDSA](https://img.shields.io/travis/numpy/numpy/master.svg?label=Travis%20CI)](explore-datascience.net)
