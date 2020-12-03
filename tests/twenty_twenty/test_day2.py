from unittest import TestCase
from src.twenty_twenty.day2 import day2


class TestDay1(TestCase):
    def test_run_part_1(self):
        test_input = ["1-3 a: abcde",
                      "1-3 b: cdefg",
                      "2-9 c: ccccccccc"]

        answer = day2.run_part_1(test_input)
        self.assertEqual(2, answer)

    def test_loop_input_part_2(self):
        test_input = ["1-3 a: abcde",
                      "1-3 b: cdefg",
                      "2-9 c: ccccccccc"]

        answer = day2.run_part_2(test_input)
        self.assertEqual(1, answer)
