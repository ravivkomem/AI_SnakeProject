from SnakeAgent import SnakeAgent
from Strategy import always_right
import time

class Game:
    
    def __init__(self, rows=20, cols=20):
        self.board = [[' '] * cols for _ in range(rows)]
        self.agent1 = SnakeAgent(self.board, strategy=always_right, symbol='A')
        self.agent2 = SnakeAgent(self.board, strategy=None, symbol='B')
        self.enemy1 = SnakeAgent(self.board, strategy=None, symbol='C')
        self.enemy2 = SnakeAgent(self.board, strategy=None, symbol='D')

    def print_board(self):
        print('    ', end='')
        for i in range(len(self.board[0])):
            print('{0} '.format(i % 10), end='')
        print()
        print('  ', end='')
        print('* ' * (len(self.board[0]) + 2))
        for j,row in enumerate(self.board):
            print('{0} '.format(j % 10), end='')
            print('* ', end='')
            print(' '.join(row), end='')
            print(' * ')
        print('  ', end='')
        print('* ' * (len(self.board[0]) + 2))
        
    def play(self):
        game_on = True
        while game_on:
            time.sleep(1)
            game_on = self.agent1.single_step()
            self.print_board()
            #self.agent2.single_step()
            #self.enemy1.single_step()
            #self.enemy2.single_step()
            #self.update_board()
            #if not self.evaluate_board():
            #    game_on = False
            