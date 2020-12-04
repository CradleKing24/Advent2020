from unittest import TestCase
from src.twenty_twenty.day3 import day3
import math


class TestDay1(TestCase):
    def test_run_part_1(self):
        test_input = ["..##.......",
                      "#...#...#..",
                      ".#....#..#.",
                      "..#.#...#.#",
                      ".#...##..#.",
                      "..#.##.....",
                      ".#.#.#....#",
                      ".#........#",
                      "#.##...#...",
                      "#...##....#",
                      ".#..#...#.#"]

        answer = day3.run_part_1(test_input)
        self.assertEqual(7, answer)

    def test_loop_input_part_2(self):
        test_input = ["..##.......",
                      "#...#...#..",
                      ".#....#..#.",
                      "..#.#...#.#",
                      ".#...##..#.",
                      "..#.##.....",
                      ".#.#.#....#",
                      ".#........#",
                      "#.##...#...",
                      "#...##....#",
                      ".#..#...#.#"]

        total = []
        total.append(day3.run_part_2(test_input, 1, 1))
        total.append(day3.run_part_2(test_input, 3, 1))
        total.append(day3.run_part_2(test_input, 5, 1))
        total.append(day3.run_part_2(test_input, 7, 1))
        total.append(day3.run_part_2(test_input, 1, 2))
        total = math.prod(total)
        self.assertEqual(336, total)


