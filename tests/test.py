# -*- coding: utf-8 -*-

from .context import src

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_hello_world(self):
        assert src.hello_world() == 'Hello, world.'

if __name__ == '__main__':
    unittest.main()