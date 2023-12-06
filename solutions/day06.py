from functools import reduce
import itertools


with open("../inputs/day06.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

times = [int(x) for x in lines[0].split(" ")[1:] if x]
distances = [int(x) for x in lines[1].split(" ")[1:] if x]

# Part 1


def get_min_hold_time(time: int, distance: int) -> int:
    for hold_time in range(1, time):
        travelled = (time - hold_time) * hold_time
        # print(hold_time, travelled, time, distance)
        if travelled > distance:
            return hold_time
    return 0


def get_max_hold_time(time: int, distance: int) -> int:
    for hold_time in range(time, 0, -1):
        travelled = (time - hold_time) * hold_time
        # print(hold_time, travelled, time, distance)
        if travelled > distance:
            return hold_time
    return time


ways = []
for time, distance in zip(times, distances):
    min_time = get_min_hold_time(time, distance)
    max_time = get_max_hold_time(time, distance)

    ways.append(max_time - min_time + 1)


print(reduce((lambda x, y: x * y), ways, 1))

# Part 2

big_time = int("".join([str(t) for t in times]))
big_distance = int("".join([str(t) for t in distances]))

min_time = get_min_hold_time(big_time, big_distance)
max_time = get_max_hold_time(big_time, big_distance)
print(max_time - min_time + 1)
