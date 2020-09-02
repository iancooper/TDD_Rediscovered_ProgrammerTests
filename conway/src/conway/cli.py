"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""

import fire
from conway import Reader, Board, write_board
from conway.game import Game


def play(seed: str = "seed.txt", runs: int = 1):
    print(f"Reading {seed} and running {runs} iterations of Conway's game of Life")
    game = Game(Reader(seed), write_board)
    game.Play(runs)


def cli():
    fire.Fire(play)


if __name__ == "__main__":
    play(runs=3)
