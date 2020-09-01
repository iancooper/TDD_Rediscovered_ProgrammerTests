"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""
from typing import List, Tuple
from conway import write_board, Reader, Board
from conway.game import Game
from mock import Mock


def test_game_of_life():
    """run an iteration of game of life"""

    # We are going to mock the boundaries/adapters - this is fine
    def board_values() -> Tuple[int, Tuple[int, int], List[List[str]]]:
        return (0, (3, 3), [
            ['.', '*', '.'],
            ['*', '*', '*'],
            ['.', '*', '.']
        ])

    reader = Mock(Reader)
    reader.read_seed_file = Mock()
    reader.read_seed_file.side_effect = board_values

    writer = Mock(write_board)

    cmd = Game(reader, writer)

    cmd.Play()

    writer.assert_called_with(Board(0, (3, 3), [['.', '*', '.'], ['*', '*', '*'], ['.', '*', '.']]))
