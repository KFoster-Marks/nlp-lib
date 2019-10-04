from .context import src

import unittest

class LemmatizeTestSuit(unittest.TestCase):
    """Lemmatization test cases."""

    def test_get_lemmas(self):
        text = 'This accuser alleges a whole different category of impropriety.'
        assert src.get_lemmas(text) == ['this', 'accuser', 'allege', 'a', 'whole', 'different', 'category', 'of', 'impropriety', '.']

if __name__ == '__main__':
    unittest.main()