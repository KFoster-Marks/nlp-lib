# -*- coding: utf-8 -*-
import spacy

nlp = spacy.load("en_core_web_sm")

def get_tokens(text):
    tokens = []
    doc = nlp.make_doc(text)

    for token in doc:
        tokens.append(token.text)
    print(tokens)
    return tokens