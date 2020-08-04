from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import bs4 as bs
import urllib.request
import csv
import collections
import itertools
import sys
import pprint

def get_continuous_chunks(text):
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk


scraped_data = urllib.request.urlopen('file:///C:/Users/Ajay/Desktop/Madhya%20Pradesh%20govt.%20says%20only%20less%20than%201%25%20wheat%20stocks%20drenched%20in%20untimely%20rain%20-%20The%20Hindu.html')

article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""



for p in paragraphs:
    article_text += p.text


reader = csv.DictReader(open('output.csv', 'rt'))
dict_list = []
for line in reader:
    dict_list.append(line)


# an_iterator = itertools.islice(dict_list[0].items(),2)
# key_value = next(an_iterator)
# print(key_value)

for en in get_continuous_chunks(article_text):
    an_iterator = itertools.islice(dict_list[len(en)].items(),len(en))
    key_value = next(an_iterator)
    # print(key_value)

pprint.pprint(dict_list)

with open("Entity1.txt", "w") as text_file:
    print(f"Entity1: {dict_list}", file=text_file)
