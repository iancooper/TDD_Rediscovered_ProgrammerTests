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

        return None
