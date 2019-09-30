# -*- coding: utf-8 -*-
import spacy

nlp = spacy.load("en_core_web_sm")

def logUtil(text):
    print(text, end=' | ')

def get_tokens(text):
    tokens = []
    doc = nlp.make_doc(text)

    for token in doc:
        tokens.append(token.text)

    return tokens

def get_named_entities(text):
    entities = []
    doc = nlp(text)
    for ent in doc.ents:
        entities.append(ent.text)

    return entities

def get_base_noun_phrases(text):
    noun_phrases = []
    doc = nlp(text)
    for phrase in doc.noun_chunks:
        logUtil(phrase.text)
        noun_phrases.append(phrase.text)

    return noun_phrases