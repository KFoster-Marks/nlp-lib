# -*- coding: utf-8 -*-

from .context import src

import unittest

class SegmentTestSuite(unittest.TestCase):
    """Segment test cases."""

    def test_get_segments(self):
        text = u'My husband is going for a long run. He will run for about four hours. He will run around the ponds.'

        assert src.get_segments(text) == ['My husband is going for a long run.', 'He will run for about four hours.', 'He will run around the ponds.']

        text2 = u'The weekend has arrived! What will we do? We will play...'
        assert src.get_segments(text2) == ['The weekend has arrived!', 'What will we do?', 'We will play...']

    def test_get_custom_segment(self):
        text = u'Not everyone agrees on the best way to build software; many argue over the costs and benefits of waterfall versus agile, for example.'

        assert src.get_custom_segment(text) == ['Not everyone agrees on the best way to build software;', 'many argue over the costs and benefits of waterfall versus agile, for example.']

        text2 = u'Applying for jobs can be painstaking; however, you must trust that it will work out for the best.'

        assert src.get_segments(text2) == ['Applying for jobs can be painstaking;', 'however, you must trust that it will work out for the best.']

if __name__ == '__main__':
    unittest.main()