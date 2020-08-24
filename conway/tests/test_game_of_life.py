"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""

from conway import Board


def test_all_cells_dead():
    """ All the cells are dead, no change """
    seed = Board(0, (3, 3), [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ])

    expected_generation_one = Board(1, (3, 3), [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ])

    generation_one = seed.tick()

    assert generation_one == expected_generation_one


