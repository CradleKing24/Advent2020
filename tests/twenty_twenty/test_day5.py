from unittest import TestCase
from src.twenty_twenty.day5 import day5
from src import custom_read_file as reader
import math


class TestDay1(TestCase):
    def test_run_part_1(self):
        test_input = ["BFFFBBFRRR",
                      "FFFBBBFRRR",
                      "BBFFBBFRLL"]

        answer = day5.run_part_1(test_input)
        self.assertEqual(820, max(answer))

    def test_run_part_2(self):
        test_input = reader.return_data_day4("./day4_p2.csv")

        answer = day4.run_part_2(test_input)
        self.assertEqual(4, answer)


