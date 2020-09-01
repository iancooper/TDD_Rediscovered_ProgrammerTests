"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""

import fire


def play(seed="seed.txt", runs=1):
    print(f"Reading {seed} and running {runs} iterations of Conway's game of Life")


def cli():
    fire.Fire(play)
