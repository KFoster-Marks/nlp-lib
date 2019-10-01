# -*- coding: utf-8 -*-
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def serve_dependency_viz(text):
    doc = nlp(text)
    displacy.serve(doc, style='dep')
    # return True