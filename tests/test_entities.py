# -*- coding: utf-8 -*-

from .context import src

import unittest
import spacy
nlp = spacy.load("en_core_web_sm")

class EntitiesTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_add_named_entity(self):
        text = "Paisley"
        doc = nlp(text)
        start_index = 0
        end_index = 1
        entity_type = "PERSON"

        assert src.add_named_entity(doc, start_index, end_index, entity_type) == 'Entity "Paisley" successfully added to type PERSON.'

        text2 = "Cape Breton International Seaport"
        doc2 = nlp(text2)
        start_index2 = 0
        end_index2 = 4
        entity_type2 = "FAC"

        assert src.add_named_entity(doc2, start_index2, end_index2, entity_type2) == 'Entity "Cape Breton International Seaport" successfully added to type FAC.'

    def test_get_named_entities(self):
        text = 'Ms. Harris ordered the National Guard to the Canadian border.'
        assert src.get_named_entities(text) == ['Harris', 'the National Guard', 'Canadian']

        text2 = 'Nova Scotia and Cape Breton Island are wonderful places to get away from the U.S. vacation crowds.'
        assert src.get_named_entities(text2) == ['Nova Scotia', 'Cape Breton Island', 'U.S.']

    def test_get_named_entities_metadata(self):
        text = 'Ms. Harris ordered the National Guard to the Canadian border.'
        assert src.get_named_entities_metadata(text) == [{'text': 'Harris', 'label': 'PERSON'}, {'text': 'the National Guard', 'label': 'ORG'}, {'text': 'Canadian', 'label': 'NORP'}]

        text2 = 'Members of the Sackler family profit almost 4 billion dollars from the sale of several ski resorts.'
        assert src.get_named_entities_metadata(text2) == [{'text': 'Sackler', 'label': 'PERSON'}, {'text': 'almost 4 billion dollars', 'label': 'MONEY'}]

    def test_get_named_entity_label_explanations(self):
        labels = ['PERSON', 'MONEY', 'ORG', 'NORP']
        assert src.get_named_entity_label_explanations(labels) == [{'label': 'PERSON', 'explanation': 'People, including fictional'}, {'label': 'MONEY', 'explanation': 'Monetary values, including unit'}, {'label': 'ORG', 'explanation': 'Companies, agencies, institutions, etc.'}, {'label': 'NORP', 'explanation': 'Nationalities or religious or political groups'}]

    def test_get_named_entities_by_label(self):
        label = 'MONEY'
        text = 'I have four dollars in my pocket, which is about a million dollars less than I need to buy a house in this state.'
        assert src.get_named_entities_by_label(text, label) == ['four dollars', 'about a million dollars']

        label2 = 'LANGUAGE'
        text2 = 'Many people believe that English is harder to learn than Spanish.'
        assert src.get_named_entities_by_label(text2, label2) == ['English', 'Spanish']

    def test_get_number_of_named_entities_by_label(self):
        label = 'GPE'
        text = 'I have visited many countries. In 2008, I moved to South Korea. In 2009, I traveled to Chile and Ecuador for a few months. In the past five years, I have visited several provinces in Canada.'
        assert src.get_number_of_named_entities_by_label(text, label) == 4

if __name__ == '__main__':
    unittest.main()