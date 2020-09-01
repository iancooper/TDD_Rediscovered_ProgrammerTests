"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""


def read_seed_file(filename: str) -> str:
    """ Read the seed file => fail fast"""
    with open(filename, 'r') as file:
        return file.read()
