class Grid:
    @classmethod
    def from_lines(cls, lines: list[str]) -> "Grid":
        width = len(lines[0])
        height = len(lines)
        cells = []
        for line in lines:
            for cell in line:
                cells.append(cell)

        return cls(width, height, cells)

    def __init__(self, width: int, height: int, cells: str) -> None:
        self.width = width
        self.height = height
        self.cells = cells

    def __str__(self) -> str:
        s = ""
        for i, c in enumerate(self.cells):
            s += c
            if (i + 1) % self.width == 0:
                s += "\n"

        return s

    def cell_at(self, x: int, y: int) -> str | None:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return None
        return self.cells[y * self.height + x]

    @staticmethod
    def get_neighbors_positions(x: int, y: int) -> list[tuple[int, int]]:
        neighbor_deltas = (
            (-1, -1),  # TOP LEFT
            (0, -1),  # TOP
            (1, -1),  # TOP RIGHT
            (-1, 0),  # LEFT
            (1, 0),  # RIGHT
            (-1, 1),  # BOTTOM LEFT
            (0, 1),  # BOTTOM
            (1, 1),  # BOTTOM RIGHT
        )
        positions = []
        for xd, yd in neighbor_deltas:
            xtarget, ytarget = x + xd, y + yd
            positions.append((xtarget, ytarget))

        return positions

    def get_neighbors(self, x: int, y: int) -> list[str]:
        neighbors = []
        for cell in self.get_neighbors_positions(x, y):
            if neighbor := self.cell_at(*cell):
                neighbors.append(neighbor)

        return neighbors

    def is_part_number(self, x: int, y: int) -> bool:
        if not (cell := self.cell_at(x, y)) or not cell.isnumeric():
            return False

        for neighbor in self.get_neighbors(x, y):
            if neighbor != "." and not neighbor.isalnum():
                return True

        return False


with open("../inputs/day03.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


# Part 1

grid = Grid.from_lines(lines)


part_numbers = []
numbers = {}
in_number = False
current_digits = []
number_coordinates = []
for y in range(grid.height):
    for x in range(grid.width):
        if (cell := grid.cell_at(x, y)) and cell.isnumeric():
            number_coordinates.append((x, y))
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
    if any(grid.is_part_number(*coord) for coord in number_coordinates):
        part_numbers.append(number)

print(sum(part_numbers))
# Part 2

gear_coords = []
for y in range(grid.height):
    for x in range(grid.width):
        if (c := grid.cell_at(x, y)) == "*" and len(
            [neighbor for neighbor in grid.get_neighbors(x, y) if neighbor.isalnum()]
        ) > 1:
            gear_coords.append((x, y))

ratio = 0
for gear_coord in gear_coords:
    # find numbers
    gear_neighbors = grid.get_neighbors_positions(*gear_coord)
    matching_numbers = []
    for number_coords, number in numbers.items():
        if any(coord in gear_neighbors for coord in number_coords):
            matching_numbers.append(number)

    if len(matching_numbers) == 2:
        ratio += matching_numbers[0] * matching_numbers[1]

print(ratio)
