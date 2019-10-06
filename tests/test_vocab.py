from .context import src
import os.path

import unittest

class VocabTestSuite(unittest.TestCase):
    def test_check_if_stop_word(self):
        text = 'the'
        assert src.check_is_stop_word(text) == True

        text = 'a'
        assert src.check_is_stop_word(text) == True

        text = 'bear'
        assert src.check_is_stop_word(text) == False

    def test_write_url_html_to_file(self):
        url = 'https://en.wikipedia.org/wiki/Linguistic_relativity'
        file_name = 'tests/__test_files__/linguistic_relativity.txt'
        src.write_url_html_to_file(url, file_name)
        assert os.path.exists(file_name) == True

        url = 'https://thefinancialdiet.com/7-gentle-but-fulfilling-ways-to-rejuvenate-your-life-this-fall/'
        file_name = 'tests/__test_files__/financial_diet.txt'
        src.write_url_html_to_file(url, file_name)
        assert os.path.exists(file_name) == True

    # def test_get_text_match(self):
    #     text = ''

if __name__ == '__main__':
    unittest.main()