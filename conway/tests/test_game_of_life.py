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


def test_single_cell_with_no_neighbours_dies():
    """ Just one cell is live, and it has no neighbours, so must die"""

    seed = Board(0, (3, 3), [
        ['.', '.', '.'],
        ['.', '*', '.'],
        ['.', '.', '.']
    ])

    expected_generation_one = Board(1, (3, 3), [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ])

    generation_one = seed.tick()

    assert generation_one == expected_generation_one


def test_two_adjacent_cells_with_insufficient_neighbours_die():
    """ Just one cell is live, and it has no neighbours, so must die"""

    seed = Board(0, (3, 3), [
        ['.', '*', '.'],
        ['.', '*', '.'],
        ['.', '.', '.']
    ])

    expected_generation_one = Board(1, (3, 3), [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ])

    generation_one = seed.tick()

    assert generation_one == expected_generation_one


def test_an_adjacent_cell_with_sufficient_neighbours_lives():
    """ Just one cell is live, and it has no neighbours, so must die"""

    seed = Board(0, (3, 3), [
        ['.', '*', '.'],
        ['.', '*', '.'],
        ['.', '*', '.']
    ])

    expected_generation_one = Board(1, (3, 3), [
        ['.', '.', '.'],
        ['.', '*', '.'],
        ['.', '.', '.']
    ])

    generation_one = seed.tick()

    assert generation_one == expected_generation_one


def test_three_live_neighbours_live_four_live_neighbours_die():
    seed = Board(0, (3, 3), [
        ['.', '*', '.'],
        ['*', '*', '*'],
        ['.', '*', '.']
    ])

    expected_generation_one = Board(1, (3, 3), [
        ['*', '*', '*'],
        ['*', '.', '*'],
        ['*', '*', '*']
    ])

    generation_one = seed.tick()

    assert generation_one == expected_generation_one


def test_cells_positioned_at_the_edge():
    seed = Board(0, (3, 3), [
        ['*', '*', '*'],
        ['*', '.', '*'],
        ['*', '*', '*']
    ])

    expected_generation_one = Board(1, (3, 3), [
        ['*', '.', '*'],
        ['.', '.', '.'],
        ['*', '.', '*']
    ])

    generation_one = seed.tick()

    assert generation_one == expected_generation_one
