import itertools
import math

with open("../inputs/day08.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


turns = itertools.cycle(lines[0])

locations = {}

for line in lines[2:]:
    location, destinations = line.split(" = ")
    locations[location] = destinations.replace("(", "").replace(")", "").split(", ")

# Part 1
steps = 0
current_location = "AAA"
while True:
    next_turn = next(turns)
    if next_turn == "L":
        current_location = locations[current_location][0]
    else:
        current_location = locations[current_location][1]

    steps += 1
    if current_location == "ZZZ":
        break

print(steps)

# Part 2
steps = 0
current_locations = [
    location for location in locations.keys() if location.endswith("A")
]

steps_per_location = []

for starting_location in current_locations:
    turns = itertools.cycle(lines[0])
    current_location = starting_location
    steps = 0
    while True:
        next_turn = next(turns)
        if next_turn == "L":
            current_location = locations[current_location][0]
        else:
            current_location = locations[current_location][1]

        steps += 1
        if current_location.endswith("Z"):
            steps_per_location.append(steps)
            break

print(math.lcm(*steps_per_location))
