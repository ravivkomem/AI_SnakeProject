import random
from collections import deque

from SnakeAgent import SnakeAgent


class Game:

    def __init__(self, rows=13, cols=13):
        self.board = [[' '] * cols for _ in range(rows)]
        self.agent1 = SnakeAgent(self.board, strategy=None, symbol='A')
        self.agent2 = SnakeAgent(self.board, strategy=None, symbol='B')
        self.snake1 = SnakeAgent(self.board, strategy=None, symbol='C')
        self.snake2 = SnakeAgent(self.board, strategy=None, symbol='D')


    def print_board(self):
        for row in self.board:
            print(' '.join(row))


