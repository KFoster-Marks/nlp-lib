# -*- coding: utf-8 -*-
import spacy
from spacy import displacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

def add_named_entity(doc, start_index, end_index, entity_label):
    # The spacy NER list will not include all named entities
    # Some may need to be added manually in order to achieve the desired textual analysis

    # We need to first check if it already exists
    entity_hash = doc.vocab.strings[entity_label]
    new_ent = Span(doc, start_index, end_index, label=entity_hash)
    doc.ents = list(doc.ents) + [new_ent]

    return f'Entity "{new_ent}" successfully added to type {entity_label}.'

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

def get_named_entities_by_label(text, label):
    doc = nlp(text)

    return [ent.text for ent in doc.ents if ent.label_ == label]

def get_number_of_named_entities_by_label(text, label):
    doc = nlp(text)

    return len([ent.text for ent in doc.ents if ent.label_ == label])