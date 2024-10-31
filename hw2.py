from typing import Optional

import data
from data import Point, Rectangle, Duration, Song

def total_duration(time:Duration):
    output_duration = (time.minutes * 60) + time.seconds
    return output_duration
def time_to_duration(time:int):
    output_duration = Duration((time // 60), (time % 60))
    return output_duration
# Write your functions for each part in the space below.

# Part 1
#takes two input points in any order, and returns a Rectangle that is properly formatted
def create_rectangle(point_a:Point, point_b:Point):
    top_left = Point(0, 0)
    bottom_right = Point(0,0)
    if point_a.x < point_b.x:
        bottom_right.x = point_b.x
        top_left.x = point_a.x
    else:
        bottom_right.x = point_a.x
        top_left.x = point_b.x
    if point_a.y > point_b.y:
        top_left.y = point_a.y
        bottom_right.y = point_b.y
    else:
        bottom_right.y = point_a.y
        top_left.y = point_b.y
    return Rectangle(top_left, bottom_right)

print(create_rectangle(Point(0, 0), Point(10, 10)))

# Part 2
#Takes two Durations, and if the first duration is less than the second returns True else False
def shorter_duration_than(dur_a:Duration, dur_b:Duration):
    dur_a_tot = (dur_a.minutes * 60) + dur_a.seconds
    dur_b_tot = (dur_b.minutes * 60) + dur_b.seconds
    if dur_a_tot < dur_b_tot:
        return True
    else:
        return False



# Part 3
#takes a list of songs, and returns the list of songs that are under the given duration
def song_shorter_than(song_list:list[Song], max_dur:Duration):
    output_list = []
    for n in song_list:
        if total_duration(n.duration) < total_duration(max_dur):
            output_list.append(n)
    return output_list

list_of_songs = [Song("Earth, Wind & Fire", "September", Duration(3, 35)),
                 Song("Jack Stauber's Micropop", "Baby Hotline", Duration(4, 51)),
                 Song("Kesha", "Blow", Duration(3,39)),
                 Song("Fountains of Wayne", "Stacy's Mom", Duration(3, 17))]
print(song_shorter_than(list_of_songs, Duration(4, 0)))

# Part 4
#takes an input song list, and a list of which indices to take songs from, compiles them into a list and adds together the total duration of the new playlist
def running_time(input_song_list:list[Song], playlist_numbers:list[int]):
    output_time = total_duration(Duration(0,0))
    for n in playlist_numbers:
        output_time += total_duration(input_song_list[n].duration)
    output_duration = time_to_duration(output_time)
    return output_duration

print(running_time(list_of_songs, [0,1,1,3,2]))


# Part 5
#takes a list of linked cities and a route, and if the route is possible based on the links, outputs True
def validate_route(city_links:[list[list[str]]], route:list[str]):
    for i in range(len(route) -1):
        l = [route[i], route[i+1]]
        x = [route[i+1], route[i]]
        if [route[i], route[i+1]] not in linked_cities and [route[i+1], route[i]] not in linked_cities:
            return False
    else:
        return True



linked_cities = [['san luis obispo', 'santa margarita'],
    ['san luis obispo', 'pismo beach'],
    ['atascadero', 'santa margarita'],
    ['atascadero', 'creston']]
print(validate_route(linked_cities, ['san luis obispo', 'atascadero']))

# Part 6
#takes an input list, and outputs the index at the longest repetition of integers within the list
def longest_repetition(int_list:list[int]) -> Optional[int]:
    if int_list != []:
        longest_repetition_length = 0
        longest_repetition_index = 0
        temp_rep_length = 0
        temp_idx = 0
        for idx in range(len(int_list) -1):
            if int_list[idx+1] == int_list[idx]:
                temp_rep_length += 1
            if int_list[idx+1] != int_list[idx] or idx == len(int_list) - 2:
                if longest_repetition_length < temp_rep_length:
                    longest_repetition_length = temp_rep_length
                    longest_repetition_index = temp_idx
                temp_rep_length = 0
                temp_idx = idx+1


        return longest_repetition_index

list_d = [1, 1, 1, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
print(longest_repetition(list_d))
