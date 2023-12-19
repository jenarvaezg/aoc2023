from functools import cache
from common.grid import Grid, Coord, Direction
import sys

sys.setrecursionlimit(1000000)

with open("../inputs/day10.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

grid = Grid.from_lines(lines)

# Valid ways to ENTER a connection
connections_input_directions = {
    ".": (),
    "S": (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT),
    "|": (Direction.UP, Direction.DOWN),
    "-": (Direction.LEFT, Direction.RIGHT),
    "L": (Direction.DOWN, Direction.LEFT),
    "J": (Direction.DOWN, Direction.RIGHT),
    "7": (Direction.UP, Direction.RIGHT),
    "F": (Direction.UP, Direction.LEFT),
}

# Valid ways to EXIT a connection
connections_output_directions = {
    ".": (),
    "S": (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT),
    "|": (Direction.UP, Direction.DOWN),
    "-": (Direction.LEFT, Direction.RIGHT),
    "L": (Direction.UP, Direction.RIGHT),
    "J": (Direction.UP, Direction.LEFT),
    "7": (Direction.DOWN, Direction.LEFT),
    "F": (Direction.DOWN, Direction.RIGHT),
}


def is_connection_valid(from_cell: str, to_cell: str, direction: Direction) -> bool:
    return (
        direction in connections_output_directions[from_cell]
        and direction in connections_input_directions[to_cell]
    )


# Part 1


def traverse_loop(
    grid: Grid, coord: Coord, loop: set[Coord], depth: int
) -> tuple[int, set[Coord]]:
    current_cell = grid.cell_at(coord)

    for neighbor, direction in grid.get_ortogonal_neighbors_with_direction(coord):
        if neighbor in loop:
            continue

        neighbor_cell = grid.cell_at(neighbor)
        if not is_connection_valid(current_cell, neighbor_cell, direction):
            continue

        loop.add(neighbor)

        return traverse_loop(grid, neighbor, loop, depth + 1)

    return depth, loop


start = grid.position_of("S")
loop: set[Coord] = {start}
print(traverse_loop(grid, start, loop, 0)[0] // 2 + 1)


# Part 2
enclosed_count = 0
for y in range(grid.height):
    walls = 0
    prev_cell = None
    for x in range(grid.width):
        coord = Coord(x, y)
        if coord in loop:
            cell = grid.cell_at(coord)
            if cell == "-":
                continue

            walls += 1
            if (cell == "J" and prev_cell == "F") or (cell == "7" and prev_cell == "L"):
                walls -= 1

            prev_cell = cell

        elif walls % 2 == 1:
            enclosed_count += 1


print(enclosed_count)
