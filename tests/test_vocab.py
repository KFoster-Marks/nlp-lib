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

        # os.remove('tests/__test_files__/linguistic_relativity.txt')
        # os.remove('tests/__test_files__/financial_diet.txt')

    def test_get_text_match(self):
        file = open('tests/__test_files__/financial_diet.txt', 'r')
        text = file.read()
        result = src.get_text_match(text, ['totally'], 5, 5)
        assert result == ['you mean you haven’t totally changed your career, launched']

        result2 = src.get_text_match(text, ['life'], 5, 5)
        assert result2[0] == 'don’t_ have your life together? I’ve taken'

    def test_get_raw_part_of_speech_counts(self):
        text = 'Natural language processing presents some of the earliest and most challenging problems computer scientists have attempted to solve.'
        result = src.get_raw_part_of_speech_counts(text)
        assert result == {84: 3, 92: 5, 100: 4, 90: 2, 85: 1, 89: 1, 86: 1, 94: 1, 97: 1}

        text = 'Reading makes me very, very nervous.'
        result = src.get_raw_part_of_speech_counts(text)
        assert result == {92: 1, 100: 1, 95: 1, 86: 2, 97: 2, 84: 1}

if __name__ == '__main__':
    unittest.main()