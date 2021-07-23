from SnakeAgent import SnakeAgent
import Strategy
import time
from blessed import Terminal

class Game:
    
    def __init__(self, rows=13, cols=13):
        self.board = [[' '] * cols for _ in range(rows)]
        self.agent1 = SnakeAgent(self.board, strategy=Strategy.max_manhattan_dist, symbol='A')
        self.agent2 = SnakeAgent(self.board, strategy=Strategy.max_manhattan_dist, symbol='B')
        self.enemy1 = SnakeAgent(self.board, strategy=Strategy.min_manhattan_dist, symbol='C', is_enemy=True)
        self.enemy2 = SnakeAgent(self.board, strategy=Strategy.min_euclidian_dist, symbol='D', is_enemy=True)
        self.term = Terminal()

    def print_board(self):
        # clear the screen
        print(self.term.home + self.term.clear)
        
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
        self.print_board()
        agent1_alive = True
        agent2_alive = True
        
        while agent1_alive or agent2_alive:
            
            time.sleep(0.2)
            self.enemy1.single_step()
            #self.print_board()
            
            #time.sleep(1)
            self.enemy2.single_step()
            #self.print_board()
            
            #time.sleep(0.5)
            agent1_alive = self.agent1.single_step()
            #self.print_board()
            
            #time.sleep(1)
            agent2_alive = self.agent2.single_step()
            self.print_board()
            
            #if not self.evaluate_board():
            #    game_on = False
            