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

                    same_column = j
                    prior_column = same_column - 1
                    next_column = same_column + 1
                    last_column = self._size[1] - 1

                    same_row = i
                    prior_row = same_row - 1
                    next_row = same_row + 1
                    last_row = self._size[0] - 1

                    if prior_row >= 0:
                        if (prior_column >= 0) and (self._cells[(prior_row)][(prior_column)] == '*'):
                            live_neighbour_count += 1

                        if self._cells[(prior_row)][same_column] == '*':
                            live_neighbour_count += 1

                        if (next_column <= last_column) and (self._cells[(prior_row)][(next_column)] == '*'):
                            live_neighbour_count += 1

                    if i == i: # always true - readability
                        if (prior_column >= 0) and (self._cells[i][(prior_column)] == '*'):
                            live_neighbour_count += 1

                        if (next_column <= last_column) and (self._cells[i][(next_column)] == '*'):
                            live_neighbour_count += 1

                    if next_row <= last_row:
                        if (prior_column <= 0) and (self._cells[(next_row)][(prior_column)] == '*'):
                            live_neighbour_count += 1

                        if self._cells[(next_row)][same_column] == '*':
                            live_neighbour_count += 1

                        if (next_column <= last_column) and (self._cells[(next_row)][(next_column)] == '*'):
                            live_neighbour_count += 1

                    if live_neighbour_count == 2:
                        next_board[i][j] = '*'

                else:
                    next_board[i].append('.')

        return Board(self._generation + 1, self._size, next_board)
