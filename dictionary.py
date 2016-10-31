from wordnik import *
import sys
import getopt


def main(argv):
    '''
        Script to get the definition of a word from wordnik.com
        Sign up and get a FREE API key from http://developer.wordnik.com/ before use

        Options:
            -w or --word - The word you wish to search for
            -l or --limit - The number of defitions you would like to get back

        Usage examples:
            python dictionary.py -w prime -l 3
            python dictionary.py --word prime --limit 3
    '''
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

    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = '8d6e647dd008063e7d00d0823cc07145aab1c078e0f99e4da'  # Replace with your own API key
    client = swagger.ApiClient(apiKey, apiUrl)
    wordApi = WordApi.WordApi(client)
    definitions = wordApi.getDefinitions(word, limit=definition_limit)
    print '\033[1m' + word + '\033[0m'
    print definitions[0].partOfSpeech
    for definition in definitions:
        print definition.text


def usage():
    print 'Usage: python dictionary.py -w word-to-search -l number-of-definitions-to-get'


if __name__ == "__main__":
    main(sys.argv[1:])
