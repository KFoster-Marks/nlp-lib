# -*- coding: utf-8 -*-
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def serve_dependency_viz(text):
    doc = nlp(text)
    options = {
        "compact": True,
        "bg": "#09a3d5",
        "color": "white",
        "font": "Source Sans Pro"
    }
    displacy.serve(doc, style='dep', options=options)
    # return True

def render_dependency_html(text):
    doc = nlp(text)
    html = displacy.render([doc], style="dep", minify=True)

    return html