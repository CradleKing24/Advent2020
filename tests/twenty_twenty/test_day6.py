from unittest import TestCase
from src.twenty_twenty.day6 import day6
from src import custom_read_file as reader


class TestDay1(TestCase):
    def test_run_part_1(self):
        test_input = reader.return_data_day6("./day6_test_input.csv")

        answer = day6.run_part_1(test_input)
        self.assertEqual(11, answer)

    def test_run_part_2(self):
        test_input = reader.return_data_day6_2("./day6_test_input.csv")

        answer = day6.run_part_2(test_input)
        self.assertEqual(6, answer)


