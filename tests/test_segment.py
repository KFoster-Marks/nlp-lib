# -*- coding: utf-8 -*-

from .context import src

import unittest

class SegmentTestSuite(unittest.TestCase):
    """Segment test cases."""

    def test_get_segments(self):
        text = u'My husband is going for a long run. He will run for about four hours. He will run around the ponds.'

        assert src.get_segments(text) == ['My husband is going for a long run.', 'He will run for about four hours.', 'He will run around the ponds.']

    def test_get_custom_segment(self):
        text = u'Not everyone agrees on the best way to build software; many argue over the costs and benefits of waterfall versus agile, for example.'

        assert src.get_custom_segment(text) == ['Not everyone agrees on the best way to build software;', 'many argue over the costs and benefits of waterfall versus agile, for example.']

if __name__ == '__main__':
    unittest.main()