# NLP-Assignments
Assignments submitted during the course of Natural Language Processing - CSE4022.

## Index

1. WordNet
2. NER using NLTK
3. Summary Extraction

### WordNet

- Import wordnet
- Use the term program to find 'synsets'
- Example of synset
- Printing just the word
- Definition of word
- Examples of the word in use
- Generating synonyms and antonyms
- Use WordNet to compare the similarity of two words and their tenses, by incorporating the Wu and Palmer method for semantic related-ness.

### NER using NLTK

Named-entity recognition (NER) (also known as entity identification, entity chunking and entity extraction) is a sub-task of information extraction that seeks to locate and classify named entities in text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.
NER systems have been created that use linguistic grammar-based techniques as well as statistical models such as machine learning. Hand-crafted grammar-based systems typically obtain better precision, but at the cost of lower recall and months of work by experienced computational linguists . Statistical NER systems typically require a large amount of manually annotated training data. Semi-supervised approaches have been suggested to avoid part of the annotation effort.
Being a free and an open-source library, NLTK has made advanced Natural Language Processing (NLP) much simpler in Python. NLTK provides an exceptionally efficient statistical system for named entity recognition in python, which can assign labels to groups of tokens which are contiguous. It provides a default model which can recognize a wide range of named or numerical entities, which include company-name, location, organization, product-name, etc to name a few. 

### Summary Extraction

First we will be scraping the desired webpage to get our article with the help of Beautiful soup. Next we will be removing square brackets and extra spaces, and save it as a text file. After input of txt file, we generate clean sentences. Then we will be using cosine similarity to find similarity between sentences. Then using summary method  we will keep calling all other help functions to keep our summarization pipeline going.

**Step 1 - Read text and tokenize**
**Step 2 - Generate Similarity Matrix across sentences** 
**Step 3 - Rank sentences in similarity matrix** 
**Step 4 - Sort the rank and pick top sentences**
**Step 5 - Of course, output the summarize text**










