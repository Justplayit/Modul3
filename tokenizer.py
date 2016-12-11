import nltk
import re

def sentenceTokenizer(text):
    enders = re.compile('[.!?]')
    sentenceList = enders.split(text)
    returnList=list()
    for sentence in sentenceList:
        if len(sentence) != 0:
            returnList.append(sentence.strip())
    return returnList
