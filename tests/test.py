# -*- coding: utf-8 -*-

from .context import src

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_get_tokens(self):
        text = "Denver is the biggest city in Colorado."
        assert src.get_tokens(text) == ['Denver', 'is', 'the', 'biggest', 'city', 'in', 'Colorado', '.']

        text2 = "Life is good :)"
        assert src.get_tokens(text2) == ['Life', 'is', 'good', ':)']

        text3 = "We spent nearly 4 million dollars in N.Y.C.!"
        assert src.get_tokens(text3) == ['We', 'spent', 'nearly', '4', 'million', 'dollars', 'in', 'N.Y.C.', '!']

if __name__ == '__main__':
    unittest.main()