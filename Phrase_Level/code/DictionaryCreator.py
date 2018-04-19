from Replacer import *
from collections import defaultdict


def loadDictionary():
    # Create emoticons dictionary
    f = open("./code/emoticonsWithPolarity.txt", 'r')
    data = f.read().split('\n')
    emoticonsDict = {}
    for i in data:
        if i:
            i = i.split()  # [':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^)', 'Positive']
            # print i
            value = i[-1]  # value =  Positive
            # print "value = " , (value)
            key = i[:-1]  # [':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^)']
            # print key
            for j in key:
                emoticonsDict[j] = value
    f.close()

    # print emoticonsDict

    # Create acronym dictionary
    f = open("./code/acronym_tokenised.txt", 'r')
    data = f.read().split('\n')
    acronymDict = {}
    for i in data:
        if i:
            i = i.split('\t')
            word = i[0].split()  # ['a$$', 'a', '**']
            # print word
            token = i[1].split()[1:]  # ['D', 'N']
            # print token
            key = word[0].lower().strip(specialChar)  # a$$
            # print key
            value = [j.lower().strip(specialChar) for j in word[1:]]
            acronymDict[key] = [value, token]
    f.close()

    print acronymDict

    # Create stopWords dictionary
    stopWords = defaultdict(int)
    f = open("./code/stopWords.txt", "r")
    for line in f:
        if line:
            line = line.strip(specialChar).lower()
            stopWords[line] = 1
    f.close()

    return acronymDict, stopWords, emoticonsDict
