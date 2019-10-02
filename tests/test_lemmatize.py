from .context import src

import unittest

class LemmatizeTestSuit(unittest.TestCase):
    """Lemmatization test cases."""

    def test_get_lemmas(self):
        text = 'This accuser alleges a whole different category of impropriety.'
        assert src.get_lemmas(text) == 'This         | DET   | this
accuser      | NOUN  | accuser
alleges      | VERB  | allege
a            | DET   | a
whole        | ADJ   | whole
different    | ADJ   | different
category     | NOUN  | category
of           | ADP   | of
impropriety  | NOUN  | impropriety
.            | PUNCT | .'

if __name__ == '__main__':
    unittest.main()