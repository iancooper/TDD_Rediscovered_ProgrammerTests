"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""
from typing import Callable

from conway import Board, Reader


class Game:
    def __init__(self, reader: Reader, writer: Callable[[Board], None]):
        self._reader = reader
        self._writer = writer

    def Play(self, runs:int = 1) -> None:
        values = self._reader.read_seed_file()
        board = Board(values[0], values[1], values[2])
        self._writer(board)
        for i in range(runs):
            board = board.tick()
            self._writer(board)
