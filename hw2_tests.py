import data
import hw2
import unittest

from data import Point, Rectangle, Duration
from hw2 import create_rectangle, shorter_duration_than, running_time, list_of_songs


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        output_rect = create_rectangle(Point(0,0), Point(10, 10))
        self.assertEqual(output_rect, Rectangle(Point(0, 10), Point(10, 0)))
    def test_create_rectangle_2(self):
        output_rect = create_rectangle(Point(-4,15), Point(10, 10))
        self.assertEqual(output_rect, Rectangle(Point(-4, 15), Point(10, 10)))
    # Part 2
    def test_shorter_duration_than_1(self):
        dur_1 = Duration(10, 5)
        dur_2 = Duration(15, 27)
        self.assertEqual(shorter_duration_than(dur_1,dur_2), True)
    def test_shorter_duration_than_2(self):
        dur_1 = Duration(4, 107)
        dur_2 = Duration(5, 20)
        self.assertEqual(shorter_duration_than(dur_1,dur_2), False)
    # Part 3
    def test_running_time_1(self):
        self.assertEqual(running_time(list_of_songs, [0, 1, 1, 3, 2]), Duration(20, 13))
    def test_running_time_2(self):
        self.assertEqual(running_time(list_of_songs, [0]), Duration(3, 35))
    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
