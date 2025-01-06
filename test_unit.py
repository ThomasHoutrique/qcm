import unittest
from qcm import QCM
from question import question

class TestQCM(unittest.TestCase):
    def test_answer_not_in_choices(self):
        with self.assertRaises(ValueError):
            q = question("Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin"], 'd')
    def test_question_not_str(self):
        with self.assertRaises(ValueError):
            q = question(123, ["Paris", "Londres", "Berlin"], 'a')

if __name__ == '__main__':
    unittest.main()