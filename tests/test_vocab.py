from .context import src

import unittest

class VocabTestSuite(unittest.TestCase):
    def test_check_if_stop_word(self):
        text = 'the'
        assert src.check_is_stop_word(text) == True

if __name__ == '__main__':
    unittest.main()