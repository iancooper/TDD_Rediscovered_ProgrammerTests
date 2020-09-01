"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""
from typing import Tuple, List

class Reader:
    def __init__(self, file_name:str) -> None:
        self._file_name = file_name

    def read_seed_file(self) -> Tuple[int, Tuple[int, int], List[List[str]]]:
        """ Read the seed file => fail fast"""
        seed = ""
        with open(self._file_name, 'r') as file:
            seed = file.read()

        args = seed.split('\n')
        generation = int(args[0][11:])
        size = (int(args[1][0:1]), int(args[1][2:3]))
        cells = []
        rows = args[2:]
        for r in range(len(rows)):
            new_row = []
            cells.append(new_row)
            for c in range(len(rows[r])):
                new_row.append(rows[r][c])

        return generation, size, cells
