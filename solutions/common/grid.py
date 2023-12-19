from dataclasses import dataclass
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass(frozen=True)
class Coord:
    x: int
    y: int


@dataclass
class Grid:
    width: int
    height: int
    cells: list[str]

    @classmethod
    def from_lines(cls, lines: list[str]) -> "Grid":
        width = len(lines[0])
        height = len(lines)
        cells = []
        for line in lines:
            for cell in line:
                cells.append(cell)

        return cls(width, height, cells)

    def __str__(self) -> str:
        s = ""
        for i, c in enumerate(self.cells):
            s += c
            if (i + 1) % self.width == 0:
                s += "\n"

        return s

    def cell_at(self, coord: Coord) -> str:
        if (
            coord.x < 0
            or coord.y < 0
            or coord.x >= self.width
            or coord.y >= self.height
        ):
            raise KeyError
        return self.cells[coord.y * self.width + coord.x]

    def get_neighbors_positions(self, coord: Coord) -> list[Coord]:
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
            xtarget, ytarget = coord.x + xd, coord.y + yd
            if (
                xtarget < 0
                or xtarget >= self.width
                or ytarget < 0
                or ytarget >= self.height
            ):
                continue
            positions.append(Coord(xtarget, ytarget))

        return positions

    def get_ortogonal_neighbors_with_direction(
        self,
        coord: Coord,
    ) -> list[tuple[Coord, Direction]]:
        neighbor_deltas = (
            ((0, -1), Direction.UP),
            ((-1, 0), Direction.LEFT),
            ((1, 0), Direction.RIGHT),
            ((0, 1), Direction.DOWN),
        )
        positions = []
        for (xd, yd), direction in neighbor_deltas:
            xtarget, ytarget = coord.x + xd, coord.y + yd
            if (
                xtarget < 0
                or xtarget >= self.width
                or ytarget < 0
                or ytarget >= self.height
            ):
                continue
            positions.append((Coord(xtarget, ytarget), direction))

        return positions

    def get_neighbors(self, coord: Coord) -> list[str]:
        neighbors = []
        for cell in self.get_neighbors_positions(coord):
            if neighbor := self.cell_at(cell):
                neighbors.append(neighbor)

        return neighbors

    def position_of(self, value: str) -> Coord:
        index = self.cells.index(value)
        x = index % self.height
        y = index // self.height
        return Coord(x, y)
