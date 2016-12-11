import nltk
import re

def splitParagraphIntoSentences(paragraph):
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    returnList=list()
    for sentence in sentenceList:
        if len(sentence) != 0:
            returnList.append(sentence.strip())
    return returnList


print(splitParagraphIntoSentences("Hello   ...My name is Lucian.!..    asdasdad fafa"))