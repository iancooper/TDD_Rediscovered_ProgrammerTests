"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""

from typing import List, Tuple


class Board():
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

    def tick(self):
        next_board = []
        for i in range(self._size[0]):
            next_board.append([])
            for j in range(self._size[1]):
                cell = self._cells[i][j]
                if cell == '*':
                    next_board[i].append('.')
                    live_neighbour_count = 0

                    if i - 1 >= 0:
                        if (j - 1 >= 0) and (self._cells[(i - 1)][(j - 1)] == '*'):
                            live_neighbour_count += 1

                        if self._cells[(i - 1)][j] == '*':
                            live_neighbour_count += 1

                        if (j + 1 <= self._size[1] - 1) and (self._cells[(i - 1)][(j + 1)] == '*'):
                            live_neighbour_count += 1

                    if i == i: # always true - readability
                        if (j - 1 >= 0) and (self._cells[i][(j - 1)] == '*'):
                            live_neighbour_count += 1

                        if (j + 1 <= self._size[1] - 1) and (self._cells[i][(j + 1)] == '*'):
                            live_neighbour_count += 1

                    if i + 1 <= self._size[0] - 1:
                        if (j - 1 <= 0) and (self._cells[(i + 1)][(j - 1)] == '*'):
                            live_neighbour_count += 1

                        if self._cells[(i + 1)][j] == '*':
                            live_neighbour_count += 1

                        if (j + 1 <= self._size[1] - 1) and (self._cells[(i + 1)][(j + 1)] == '*'):
                            live_neighbour_count += 1

                    if live_neighbour_count == 2:
                        next_board[i][j] = '*'

                else:
                    next_board[i].append('.')

        return Board(self._generation + 1, self._size, next_board)
