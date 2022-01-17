import unittest

from rcd_str import capitalize_word_sequences


class TestCapita(unittest.TestCase):
    def test(self):
        self.assertEqual(capitalize_word_sequences('усть-каменогорск'),
                         'Усть-Каменогорск')
        self.assertEqual(capitalize_word_sequences('нижний тагил'), 'Нижний Тагил')
