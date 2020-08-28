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
        self._cells = cells

    def __eq__(self, other):
        if isinstance(other, Board):
            return (self._size == other._size) and (self._cells == other._cells)

    def __repr__(self):
        return f'Board({self._generation!r}, {self._size!r}, {self._cells!r}'

    def tick(self) -> 'Board':
        next_board = []
        for i in range(self._size[0]):
            next_board.append([])
            for j in range(self._size[1]):
                cell = self._cells[i][j]
                if cell == '*':
                    next_board[i].append('.')
                    live_neighbour_count = _Neighbours(i, j, self._size).get_count(self._cells)
                    if live_neighbour_count == 2 or live_neighbour_count == 3:
                        next_board[i][j] = '*'

                else:
                    next_board[i].append('.')
                    live_neighbour_count = _Neighbours(i, j, self._size).get_count(self._cells)
                    if live_neighbour_count == 3:
                        next_board[i][j] = '*'

        return Board(self._generation + 1, self._size, next_board)


class _Neighbours:
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
        live_neighbour_count = self.prior_row_count(cells)

        live_neighbour_count += self.same_row_count(cells)

        live_neighbour_count += self.next_row_count(cells)

        return live_neighbour_count

    def next_row_count(self, cells):
        live_neighbour_count = 0
        if self._next_row <= self._last_row:
            if (self._prior_column >= 0) and (cells[self._next_row][self._prior_column] == '*'):
                live_neighbour_count += 1

            if cells[self._next_row][self._same_column] == '*':
                live_neighbour_count += 1

            if (self._next_column <= self._last_column) and (cells[self._next_row][self._next_column] == '*'):
                live_neighbour_count += 1
        return live_neighbour_count

    def same_row_count(self, cells):
        live_neighbour_count = 0
        if (self._prior_column >= 0) and (cells[self._same_row][self._prior_column] == '*'):
            live_neighbour_count += 1
        if (self._next_column <= self._last_column) and (cells[self._same_row][self._next_column] == '*'):
            live_neighbour_count += 1
        return live_neighbour_count

    def prior_row_count(self, cells):
        live_neighbour_count = 0
        if self._prior_row >= 0:
            if (self._prior_column >= 0) and (cells[self._prior_row][(self._prior_column)] == '*'):
                live_neighbour_count += 1

            if cells[self._prior_row][self._same_column] == '*':
                live_neighbour_count += 1

            if (self._next_column <= self._last_column) and (cells[self._prior_row][self._next_column] == '*'):
                live_neighbour_count += 1
        return live_neighbour_count
