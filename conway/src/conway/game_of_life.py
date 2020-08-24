"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""

from typing import List, Tuple

class Board():
    """ A game board for the game of life, should be immutable"""

    def __init__(self, generation: int, size: Tuple[int, int], cells: List[str]):
        self._generation = generation
        self._size = size
        self._cells = cells

    def __eq__(self, other):
        if isinstance(other, Board):
            return (self._size == other._size) and (self._cells == other._cells)

    def __repr__(self):
        return f'Board({self._generation!r}, {self._size!r}, {self._cells!r}'


    def tick(board):
        return Board(1, (3, 3), [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ])
