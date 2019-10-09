# -*- coding: utf-8 -*-
import spacy
from spacy import displacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

def logUtil(text):
    print(text, end=' | ')

def add_named_entity(doc, start_index, end_index, entity_label):
    # The spacy NER list will not include all named entities; we may need to add some manually in order to achieve the desired textual analysis.


    # We need to first check if it already exists!!!
    entity_hash = doc.vocab.strings[entity_label]
    new_ent = Span(doc, start_index, end_index, label=entity_hash)
    print('before: ', doc.ents)
    doc.ents = list(doc.ents) + [new_ent]
    print('after: ', doc.ents)

    return doc

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

def get_named_entities_metadata(text):
    metadata = []
    doc = nlp(text)

    for ent in doc.ents:
        entMetadata = dict(text=ent.text, label=ent.label_)
        metadata.append(entMetadata)

    return metadata

def get_named_entity_label_explanations(labels):
    explanations = []

    for label in labels:
        labelExplanation = dict(label=label, explanation=str(spacy.explain(label)))
        explanations.append(labelExplanation)

    return explanations

def get_base_noun_phrases(text):
    noun_phrases = []
    doc = nlp(text)
    for phrase in doc.noun_chunks:
        noun_phrases.append(phrase.text)

    return noun_phrases