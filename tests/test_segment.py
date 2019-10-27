# -*- coding: utf-8 -*-

from .context import src

import unittest

class SegmentTestSuite(unittest.TestCase):
    """Segment test cases."""

    def test_get_segments(self):
        text = u'My husband is going for a long run. He will run for about four hours. He will run around the ponds.'

        assert src.get_segments(text) == ['My husband is going for a long run.', 'He will run for about four hours.', 'He will run around the ponds.']

if __name__ == '__main__':
    unittest.main()