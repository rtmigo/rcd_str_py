import unittest

from rcd_str import keep_letters_dashes_spaces


class TestKeepLetters(unittest.TestCase):

    def test(self):
        self.assertEqual(keep_letters_dashes_spaces("Санкт-Петербург"),
                         "Санкт-Петербург")

        self.assertEqual(keep_letters_dashes_spaces("-Узда-"), "Узда")
        self.assertEqual(keep_letters_dashes_spaces("- Узда -"), "Узда")

        self.assertEqual(keep_letters_dashes_spaces("Усть---Каменогорск"),
                         "Усть-Каменогорск")
        self.assertEqual(keep_letters_dashes_spaces("Усть - --- Каменогорск"),
                         "Усть-Каменогорск")

        self.assertEqual(keep_letters_dashes_spaces("Космонавтов, 6"),
                         "Космонавтов")

        self.assertEqual(keep_letters_dashes_spaces(":) Нижний__Тагил!!!"),
                         "Нижний Тагил")
        self.assertEqual(keep_letters_dashes_spaces("  Красная\t\tПоляна "),
                         "Красная Поляна")
        self.assertEqual(keep_letters_dashes_spaces("Красная Поляна"),
                         "Красная Поляна")
        self.assertEqual(keep_letters_dashes_spaces("Кривой   Рог"), "Кривой Рог")
        self.assertEqual(keep_letters_dashes_spaces("Кривой_Рог"), "Кривой Рог")