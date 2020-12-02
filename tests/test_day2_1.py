from unittest import TestCase
from src.day2 import day2


class TestDay1(TestCase):
    def test_day2_1_main(self):
        data = [1, 0, 0, 0, 99]
        index1 = day2.day_2_1(data)
        self.assertEqual([2,0,0,0,99], index1)

        data = [2,3,0,3,99]
        index1 = day2.day_2_1(data)
        self.assertEqual([2,3,0,6,99], index1)

        data = [2,4,4,5,99,0]
        index1 = day2.day_2_1(data)
        self.assertEqual([2,4,4,5,99,9801], index1)

        data = [1,1,1,4,99,5,6,0,99]
        index1 = day2.day_2_1(data)
        self.assertEqual([30,1,1,4,2,5,6,0,99], index1)


