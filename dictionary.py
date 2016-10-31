from wordnik import *
import sys
import getopt


def main(argv):

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
    apiKey = '8d6e647dd008063e7d00d0823cc07145aab1c078e0f99e4da'
    client = swagger.ApiClient(apiKey, apiUrl)
    wordApi = WordApi.WordApi(client)
    example = wordApi.getDefinitions(word, limit=definition_limit)
    print word
    print example[0].partOfSpeech
    for definition in example:
        print definition.text


def usage():
    print 'Usage: python dictionary.py -w word-to-search -l number-of-definitions-to-get'


if __name__ == "__main__":
    main(sys.argv[1:])
