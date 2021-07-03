import unittest

from rcd_str import sentence_case


class TestSentenceCase(unittest.TestCase):

    def test(self):
        self.assertEqual(sentence_case("иван"), "Иван")
        self.assertEqual(sentence_case("иван Евгеньевич Смирнов"),
                         "Иван Евгеньевич Смирнов")
        self.assertEqual(sentence_case("красный богатырь"), "Красный богатырь")

        self.assertEqual("«шербурские зонтики»".capitalize(),
                         "«шербурские зонтики»")
        self.assertEqual(sentence_case("«шербурские зонтики»"),
                         "«Шербурские зонтики»")
        self.assertEqual(sentence_case("«the Beatles»"), "«The Beatles»")

        self.assertEqual(sentence_case(""), "")
        self.assertEqual(sentence_case("1"), "1")
        self.assertEqual(sentence_case("123"), "123")
        self.assertEqual(sentence_case("1x"), "1X")
        self.assertEqual(sentence_case("x"), "X")