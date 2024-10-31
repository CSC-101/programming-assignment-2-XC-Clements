import data
import hw2
import unittest

from data import Point, Rectangle, Duration, Song
from hw2 import create_rectangle, shorter_duration_than, running_time, list_of_songs, song_shorter_than, validate_route, \
    linked_cities, longest_repetition, list_d


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
    def test_song_shorter_than_1(self):
        self.assertEqual(song_shorter_than(list_of_songs, Duration(4, 0)), [Song('Earth, Wind & Fire', 'September', Duration(3, 35)), Song('Kesha', 'Blow', Duration(3, 39)), Song('Fountains of Wayne', "Stacy's Mom", Duration(3, 17))])
    def test_song_shorter_than_2(self):
        self.assertEqual(song_shorter_than(list_of_songs, Duration(2, 0)), [])
    # Part 4
    def test_running_time_1(self):
        self.assertEqual(running_time(list_of_songs, [0, 1, 1, 3, 2]), Duration(20, 13))
    def test_running_time_2(self):
        self.assertEqual(running_time(list_of_songs, [0]), Duration(3, 35))

    # Part 5
    def test_validate_route_1(self):
        self.assertEqual(validate_route(linked_cities, ['san luis obispo', 'atascadero']), False)
    def test_validate_route_2(self):
        self.assertEqual(validate_route(linked_cities, ['san luis obispo', 'santa margarita', 'atascadero']), True)

    # Part 6
    def test_longest_repetition_1(self):
        self.assertEqual(longest_repetition(list_d), 8)
    def test_longest_repetition_2(self):
        self.assertEqual(longest_repetition([]), None)




if __name__ == '__main__':
    unittest.main()
