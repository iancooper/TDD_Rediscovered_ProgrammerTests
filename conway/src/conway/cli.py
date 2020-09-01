"""
Author: Ian Cooper
Date: 23 August 2020
Notes:
"""

import fire


def play(seed:str="seed.txt", runs:int=1):
    print(f"Reading {seed} and running {runs} iterations of Conway's game of Life")


def cli():
    fire.Fire(play)
