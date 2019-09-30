# -*- coding: utf-8 -*-

from .context import src

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_get_tokens(self):
        text = 'Denver is the biggest city in Colorado.'
        assert src.get_tokens(text) == ['Denver', 'is', 'the', 'biggest', 'city', 'in', 'Colorado', '.']

        text2 = 'Life is good :)'
        assert src.get_tokens(text2) == ['Life', 'is', 'good', ':)']

        text3 = 'We spent nearly 4 million dollars in N.Y.C.!'
        assert src.get_tokens(text3) == ['We', 'spent', 'nearly', '4', 'million', 'dollars', 'in', 'N.Y.C.', '!']

    def test_get_named_entities(self):
        text = 'Ms. Harris ordered the National Guard to the Canadian border.'
        assert src.get_named_entities(text) == ['Harris', 'the National Guard', 'Canadian']

    def test_get_named_entities_metadata(self):
        text = 'Ms. Harris ordered the National Guard to the Canadian border.'
        assert src.get_named_entities_metadata(text) == [{'text': 'Harris', 'label': 'PERSON'}, {'text': 'the National Guard', 'label': 'ORG'}, {'text': 'Canadian', 'label': 'NORP'}]

        text2 = 'Members of the Sackler family profit almost 4 billion dollars from the sale of several ski resorts.'
        assert src.get_named_entities_metadata(text2) == [{'text': 'Sackler', 'label': 'PERSON'}, {'text': 'almost 4 billion dollars', 'label': 'MONEY'}]

    def test_get_named_entity_label_explanations(self):
        labels = ['PERSON', 'MONEY', 'ORG', 'NORP']
        assert src.get_named_entity_label_explanations(labels) == [{'label': 'PERSON', 'explanation': 'People, including fictional'}, {'label': 'MONEY', 'explanation': 'Monetary values, including unit'}, {'label': 'ORG', 'explanation': 'Companies, agencies, institutions, etc.'}, {'label': 'NORP', 'explanation': 'Nationalities or religious or political groups'}]

    def test_get_noun_phrases(self):
        text = 'The doughnuts fell into my belly with disconcerting speed.'
        assert src.get_base_noun_phrases(text) == ['The doughnuts', 'my belly', 'disconcerting speed']

        text2 = 'A national park system must be maintained by a concerned and capable group of outdoor enthusiasts and animal lovers.'
        assert src.get_base_noun_phrases(text2) == ['A national park system', 'a concerned and capable group', 'outdoor enthusiasts', 'animal lovers']

if __name__ == '__main__':
    unittest.main()