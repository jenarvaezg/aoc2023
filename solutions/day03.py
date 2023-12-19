from common.grid import Grid, Coord


with open("../inputs/day03.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


# Part 1

grid = Grid.from_lines(lines)


def is_part_number(grid: Grid, coord: Coord) -> bool:
    if not (cell := grid.cell_at(coord)) or not cell.isnumeric():
        return False

    for neighbor in grid.get_neighbors(coord):
        if neighbor != "." and not neighbor.isalnum():
            return True

    return False


part_numbers = []
numbers = {}
in_number = False
current_digits = []
number_coordinates = []
for y in range(grid.height):
    for x in range(grid.width):
        coord = Coord(x, y)
        if (cell := grid.cell_at(coord)) and cell.isnumeric():
            number_coordinates.append(coord)
            in_number = True
            current_digits.append(cell)
        else:
            if in_number:  # Number is finished
                in_number = False
                numbers[tuple(number_coordinates)] = int("".join(current_digits))
                current_digits = []
                number_coordinates = []

    if in_number:  # Line is finished, check number
        in_number = False
        numbers[tuple(number_coordinates)] = int("".join(current_digits))
        current_digits = []
        number_coordinates = []


for number_coordinates, number in numbers.items():
    if any(is_part_number(grid, coord) for coord in number_coordinates):
        part_numbers.append(number)

print(sum(part_numbers))
# Part 2

gear_coords = []
for y in range(grid.height):
    for x in range(grid.width):
        coord = Coord(x, y)
        if (c := grid.cell_at(coord)) == "*" and len(
            [neighbor for neighbor in grid.get_neighbors(coord) if neighbor.isalnum()]
        ) > 1:
            gear_coords.append(coord)

ratio = 0
for gear_coord in gear_coords:
    # find numbers
    gear_neighbors = grid.get_neighbors_positions(gear_coord)
    matching_numbers = []
    for number_coords, number in numbers.items():
        if any(coord in gear_neighbors for coord in number_coords):
            matching_numbers.append(number)

    if len(matching_numbers) == 2:
        ratio += matching_numbers[0] * matching_numbers[1]

print(ratio)
