#!/usr/bin/python

import requests
import sys
import getopt


def main(argv):
    '''
        Script to get the definition of a word from wordnik.com
        Sign up and get a FREE API key from http://developer.wordnik.com/ before use

        Requirements:
            Requests HTTP library v2.11.1 or later - Install using pip install requests==2.11.1
            Requests security updates (Python 2 only) - Install using pip install requests[security]
            Wordnik API key - Sign up for one for free at http://developer.wordnik.com/

        Options:
            -w or --word - The word you wish to search for
            -l or --limit - The number of defitions you would like to get back

        Usage examples:
            ./dictionary.py -w prime -l 3
            ./dictionary.py --word prime --limit 3
    '''
    api_url = 'http://api.wordnik.com/v4/word.json/'
    # Replace with your own API key
    api_key = '8d6e647dd008063e7d00d0823cc07145aab1c078e0f99e4da'
    definition_limit = 1
    word = ''

    try:
        opts, args = getopt.getopt(argv, "w:l:", ["word=", "limit="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-w", "--word"):
            word = arg
        elif opt in ("-l", "--limit"):
            definition_limit = arg

    if word == '':
        usage()
        sys.exit(2)

    headers = {'api_key': api_key}
    params = {'limit': definition_limit}

    try:
        def_resp = requests.get(api_url + word + '/definitions', params, headers=headers)
        pro_resp = requests.get(api_url + word + '/pronunciations', params, headers=headers)
    except TypeError:
        print ('\t\033[31m Error: \033[0m: Make sure you\'re using requests v2.11.1 or later \n\t pip install requests==2.11.1')
        sys.exit(2)

    definitions = def_resp.json()
    if not definitions:
        def_resp = requests.get(api_url + word.lower() + '/definitions', params, headers=headers)
        pro_resp = requests.get(api_url + word.lower() + '/pronunciations', params, headers=headers)
    definitions = def_resp.json()
    pronunciations = pro_resp.json()

    if definitions:
        print ('\033[1m' + word + '\033[0m')
        if pronunciations:
            print (pronunciations[0]['raw'])
        try:
            definitions[0]['partOfSpeech']
            print (definitions[0]['partOfSpeech'])
        except KeyError:
            pass
        for definition in definitions:
            print (definition['text'])
    else:
        print ('Word not found. Sorry.')


def usage():
    print ('Usage: ./dictionary.py -w word-to-search -l number-of-definitions-to-get')


if __name__ == "__main__":
    main(sys.argv[1:])
