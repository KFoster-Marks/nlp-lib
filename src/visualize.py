# -*- coding: utf-8 -*-
import spacy

nlp = spacy.load("en_core_web_sm")

def serve_visualization():
    doc = nlp(u'Brown bears are getting their fill on river salmon this season.')
    # spacy.displacy.serve(doc, style='dep')
    return True