# Python Word Lookup

Script to get the definition of a word from wordnik.com

Sign up and get a FREE API key from http://developer.wordnik.com/ before use

##Requirements:
Requests HTTP library v2.11.1 or later - Install using `pip install requests==2.11.1`

Requests security updates (Python 2 only) - Install using `pip install requests[security]`

Wordnik API key - Sign up for one for free at http://developer.wordnik.com/


##Options:
-w or --word - The word you wish to search for

-l or --limit - The number of defitions you would like to get back

##Usage:
``./dictionary.py -w prime -l 3``

``./dictionary.py --word prime --limit 3``
