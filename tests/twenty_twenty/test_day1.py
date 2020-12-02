from unittest import TestCase
from src.twenty_twenty.day1 import day1


class TestDay1(TestCase):
    def test_loop_input(self):
        test_input = [1721,979,366,299,675,1456]
        answer = day1.loop_input(test_input)
        self.assertEqual(514579, answer)

    def test_loop_input_part_2(self):
        test_input = [1721,979,366,299,675,1456]
        answer = day1.loop_input_part_2(test_input)
        self.assertEqual(241861950, answer)
