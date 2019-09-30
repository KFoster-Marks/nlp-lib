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