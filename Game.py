from SnakeAgent import SnakeAgent
from Strategy import always_right
import time

class Game:
    
    def __init__(self, rows=20, cols=20):
        self.board = [[' '] * cols for _ in range(rows)]
        self.agent1 = SnakeAgent(self.board, strategy=always_right, symbol='A')
        self.agent2 = SnakeAgent(self.board, strategy=always_right, symbol='B')
        self.enemy1 = SnakeAgent(self.board, strategy=always_right, symbol='C', is_enemy=True)
        self.enemy2 = SnakeAgent(self.board, strategy=always_right, symbol='D', is_enemy=True)

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
        
        agent1_alive = True
        agent2_alive = True
        
        while agent1_alive or agent2_alive:
            
            time.sleep(1)
            self.enemy1.single_step()
            #self.print_board()
            
            #time.sleep(1)
            self.enemy2.single_step()
            #self.print_board()
            
            #time.sleep(1)
            agent1_alive = self.agent1.single_step()
            #self.print_board()
            
            #time.sleep(1)
            agent2_alive = self.agent2.single_step()
            self.print_board()
            
            #if not self.evaluate_board():
            #    game_on = False
            