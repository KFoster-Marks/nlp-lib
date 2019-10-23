# -*- coding: utf-8 -*-

from .context import src

import unittest
import spacy
nlp = spacy.load("en_core_web_sm")

class TokenizeTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_get_tokens(self):
        text = 'Denver is the biggest city in Colorado.'
        assert src.get_tokens(text) == ['Denver', 'is', 'the', 'biggest', 'city', 'in', 'Colorado', '.']

        text2 = 'Life is good :)'
        assert src.get_tokens(text2) == ['Life', 'is', 'good', ':)']

        text3 = 'We spent nearly 4 million dollars in N.Y.C.!'
        assert src.get_tokens(text3) == ['We', 'spent', 'nearly', '4', 'million', 'dollars', 'in', 'N.Y.C.', '!']

    def test_get_noun_phrases(self):
        text = 'The doughnuts fell into my belly with disconcerting speed.'
        assert src.get_base_noun_phrases(text) == ['The doughnuts', 'my belly', 'disconcerting speed']

        text2 = 'A national park system must be maintained by a concerned and capable group of outdoor enthusiasts and animal lovers.'
        assert src.get_base_noun_phrases(text2) == ['A national park system', 'a concerned and capable group', 'outdoor enthusiasts', 'animal lovers']

if __name__ == '__main__':
    unittest.main()