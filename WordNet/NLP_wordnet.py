# NLP_WordNet

# import wordnet
from nltk.corpus import wordnet

# Use the term program to find 'synsets'
syns = wordnet.synsets("program")

# example of synset
print("synset: "+syns[0].name())

# printing just the word
print("word: "+syns[0].lemmas()[0].name())

# Definition of word
print("Definition: "+syns[0].definition())

# Examples of the word in use
print("Examples: ")
print(syns[0].examples())
print("\n")
# Generating synonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("gorgeous"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("Synonyms: ")
print(set(synonyms))
print("\n")
print("Antonyms: ")
print(set(antonyms))
print("\n")
# use WordNet to compare the similarity of two words and their tenses,
# by incorporating the Wu and Palmer method for semantic related-ness.

print("Similarity: ")
w1 = wordnet.synset('giant.n.01')
w2 = wordnet.synset('short.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))