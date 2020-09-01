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

    def Play(self) -> None:
        values = self._reader.read_seed_file()
        self._writer(Board(values[0], values[1], values[2]))

