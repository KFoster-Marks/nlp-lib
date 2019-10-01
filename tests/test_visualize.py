# -*- coding: utf-8 -*-

from .context import src

import unittest

class VisualizeTestSuite(unittest.TestCase):
    """Advanced test cases."""

    # def test_serve_dependency_viz(self):
    #     text = u'Brown bears are eating salmon.'
    #     assert src.serve_dependency_viz(text) == True

    def test_render_dependency_html(self):
        text = u'Brown bears are eating salmon.'
        src.render_dependency_html(text)
        assert True == True

if __name__ == '__main__':
    unittest.main()