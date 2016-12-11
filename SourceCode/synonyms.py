#the synonyms of word
from nltk.corpus import wordnet as wn

synonyms = []

for syn in wn.synsets("good"):
    for l in syn.lemmas():
       synonyms.append(l.name())

print(set(synonyms))


print(wn.morphy('denied', wn.VERB))
