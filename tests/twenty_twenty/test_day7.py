from unittest import TestCase
from src.twenty_twenty.day7 import day7
from src import custom_read_file as reader


class TestDay1(TestCase):
    def test_run_part_1(self):
        test_input = reader.return_reader_lines("./day7_test_input.csv")

        answer = day7.run_part_1(test_input)
        self.assertEqual(5, answer)

    def test_run_part_2(self):
        test_input = reader.return_reader_lines("./day7_test_input_2.csv")

        answer = day7.run_part_2(test_input)
        self.assertEqual(0, answer)


