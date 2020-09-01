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
        self._rows = self._size[0]
        self._cols = self._size[1]
        self._cells = cells

    def __eq__(self, other):
        if isinstance(other, Board):
            return (self._size == other._size) and (self._cells == other._cells)

    def __repr__(self):
        return f'Board({self._generation!r}, {self._size!r}, {self._cells!r}'

    def tick(self) -> 'Board':
        next_board = []
        for row in range(self._rows):
            next_board.append([])
            for col in range(self._cols):
                cell = self._cells[row][col]
                if cell == '*':
                    next_board[row].append('.')
                    live_neighbour_count = _Neighbours(row, col, self._size).get_count(self._cells)
                    if live_neighbour_count == 2 or live_neighbour_count == 3:
                        next_board[row][col] = '*'

                else:
                    next_board[row].append('.')
                    live_neighbour_count = _Neighbours(row, col, self._size).get_count(self._cells)
                    if live_neighbour_count == 3:
                        next_board[row][col] = '*'

        return Board(self._generation + 1, self._size, next_board)


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

    def get_count(self, cells: List[List[str]]) -> int:
        live_neighbour_count = self.row_count(self._prior_row, cells)

        live_neighbour_count += self.row_count(self._same_row, cells, True)

        live_neighbour_count += self.row_count(self._next_row, cells)

        return live_neighbour_count

    def row_count(self, row: int, cells: List[List[str]], exclude: bool = False):
        live_neighbour_count = 0
        if row >= 0 and row <= self._last_row:
            if (self._prior_column >= 0) and (cells[row][self._prior_column] == '*'):
                live_neighbour_count += 1

            if not exclude and cells[row][self._same_column] == '*':
                live_neighbour_count += 1

            if (self._next_column <= self._last_column) and (cells[row][self._next_column] == '*'):
                live_neighbour_count += 1
        return live_neighbour_count

