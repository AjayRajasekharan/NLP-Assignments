# -*- coding: utf-8 -*-

import nltk
from matplotlib import style
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
import urllib.request
import bs4 as bs

# Web scraping of required article
scraped_data = urllib.request.urlopen('file:///C:/Users/Ajay/Desktop/China%20to%20ban%20pork%20imports%20from%20India%20-%20The%20Hindu.html')

article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text


# Writing article into text format
with open("article.txt", "w") as txt_file:
    print(f"{article_text}", file=txt_file)



style.use('fivethirtyeight')


# Process text
def process_text(txt_file):
    raw_text = open("article.txt").read()
    token_text = word_tokenize(raw_text)
    return token_text


# NLTK POS and NER taggers
def nltk_tagger(token_text):
    tagged_words = nltk.pos_tag(token_text)
    ne_tagged = nltk.ne_chunk(tagged_words)
    return (ne_tagged)


# Parse named entities from tree
def structure_ne(ne_tree):
    ne = []
    for subtree in ne_tree:
        if type(subtree) == Tree:  # If subtree is a noun chunk, i.e. NE != "O"
            ne_label = subtree.label()
            ne_string = " ".join([token for token, pos in subtree.leaves()])
            ne.append((ne_string, ne_label))
    return ne


# def nltk_main():
#     print(structure_ne(nltk_tagger(process_text(txt_file))))
#
# if __name__ == '__main__':
#     nltk_main()
#
print(structure_ne(nltk_tagger(process_text(txt_file))))

with open("Entity2.txt", "w") as text_file:
    print(f"Entity2: {structure_ne(nltk_tagger(process_text(txt_file)))}", file=text_file)
