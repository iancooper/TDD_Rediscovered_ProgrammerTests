"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""

from typing import List, Tuple


class Board:
    """ A game board for the game of life, should be immutable"""

    def __init__(self, generation: int, size: Tuple[int, int], cells: List[List[str]]):
        self._generation = generation
        self._size = size
        # self._rows = self._size[0]
        self._cols = self._size[1]
        # self._cells = cells
        self._rows = [_Row(r) for r in cells]

    def __eq__(self, other):
        if isinstance(other, Board):
            return (self._size == other._size) and (self._rows == other._rows)

    def __repr__(self):
        return f'Board({self._generation!r}, {self._size!r}, {self._rows!r}'

    def tick(self) -> 'Board':
        next_board = [_Row(["." for c in range(self._cols)]) for r in self._rows]
        for row in range(len(self._rows)):
            for col in range(self._cols):
                cell = self._rows[row][col]
                if cell == '*':
                    live_neighbour_count = _Neighbours(row, col, self._size).get_count(self._rows)
                    if live_neighbour_count == 2 or live_neighbour_count == 3:
                        next_board[row][col] = '*'

                else:
                    live_neighbour_count = _Neighbours(row, col, self._size).get_count(self._rows)
                    if live_neighbour_count == 3:
                        next_board[row][col] = '*'

        grid = []
        for i in range(len(next_board)):
            grid.append(next_board[i].get_cells())

        return Board(self._generation + 1, self._size, grid)


class _Neighbours:
    """A neighbour calculator for a cell in a grid
    * It finds neigbours north, north-east, east, south-east, south, south-west, west, and north-west
    * It counts the number of those nieghbours that are live
    * it does not count neighbours beyond the borders of the grid, effectively treating them as dead
    """

    def __init__(self, row: int, col: int, size: Tuple[int, int]):
        self._size = size
        self._same_column = col
        self._prior_column = col - 1
        self._next_column = col + 1
        self._last_column = self._size[1] - 1

        self._same_row = row
        self._prior_row = row - 1
        self._next_row = row + 1
        self._last_row = self._size[0] - 1

    def get_count(self, rows: List['_Row']) -> int:
        live_neighbour_count = self.row_count(self._prior_row, rows)

        live_neighbour_count += self.row_count(self._same_row, rows, True)

        live_neighbour_count += self.row_count(self._next_row, rows)

        return live_neighbour_count

    def row_count(self, row: int, rows: List['_Row'], exclude: bool = False):
        live_neighbour_count = 0
        if row >= 0 and row <= self._last_row:
            if (self._prior_column >= 0) and (rows[row][self._prior_column] == '*'):
                live_neighbour_count += 1

            if not exclude and rows[row][self._same_column] == '*':
                live_neighbour_count += 1

            if (self._next_column <= self._last_column) and (rows[row][self._next_column] == '*'):
                live_neighbour_count += 1
        return live_neighbour_count


class _Row:
    def __init__(self, row: List[str]):
        self._cells = [_Cell(s) for s in row]

    def __eq__(self, other):
        if isinstance(other, _Row):
            return self._cells == other._cells

    def __getitem__(self, key):
        return self._cells[key]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def __repr__(self):
        view = []
        for i in range(len(self._cells)):
            view.append(str(self._cells[i]))
        return "".join(view)

    def get_cells(self) -> List[str]:
        cells = []
        for i in range(len(self._cells)):
            cells.append(str(self._cells[i]))
        return cells


class _Cell:
    def __init__(self, val: str = "."):
        self._state = val

    def __str__(self):
        return self._state

    def __eq__(self, other):
        if isinstance(other, _Cell):
            return self._state == other._state
        elif isinstance(other, str):
            return self._state == other


