import spacy

from spacy.lang.en.stop_words import STOP_WORDS

from sklearn.feature_extraction.text import CountVectorizer

import en_core_web_sm

nlp = spacy.load("en_core_web_sm")

#reading text file

with open("TT.txt", "r", encoding="utf-8") as f:

        text = " ".join(f.readlines())

doc = nlp(text)

#priting word and part of speech of the word

print([(w.text, w.pos_) for w in doc])

print(doc)
