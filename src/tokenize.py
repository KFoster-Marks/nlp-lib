# -*- coding: utf-8 -*-
import spacy
from spacy import displacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

def get_tokens(text):
    tokens = []
    doc = nlp.make_doc(text)

    for token in doc:
        tokens.append(token.text)

    return tokens

def get_base_noun_phrases(text):
    noun_phrases = []
    doc = nlp(text)
    for phrase in doc.noun_chunks:
        noun_phrases.append(phrase.text)

    return noun_phrases