from SnakeAgent import SnakeAgent
import Strategy
import time
from blessed import Terminal

class Game:
    
    def __init__(self, rows=13, cols=13):
        self.board = [[' '] * cols for _ in range(rows)]
        self.agent1 = SnakeAgent(self.board, strategy=Strategy.mini_max, symbol='A')
        self.agent2 = SnakeAgent(self.board, strategy=Strategy.max_manhattan_dist, symbol='B')
        self.enemy1 = SnakeAgent(self.board, strategy=Strategy.min_manhattan_dist, symbol='C', is_enemy=True)
        self.enemy2 = SnakeAgent(self.board, strategy=Strategy.min_euclidian_dist, symbol='D', is_enemy=True)
        self.term = Terminal()
        
        self.notify_all_agents('A', self.agent1.get_body())
        self.notify_all_agents('B', self.agent2.get_body())
        self.notify_all_agents('C', self.enemy1.get_body())
        self.notify_all_agents('D', self.enemy2.get_body())

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
            #time.sleep(0.2)
            
            self.enemy1.single_step()
            self.notify_all_agents('C', self.enemy1.get_body())
            
            self.enemy2.single_step()
            self.notify_all_agents('D', self.enemy2.get_body())
            
            agent1_alive = self.agent1.single_step()
            self.notify_all_agents('A', self.agent1.get_body())
            
            agent2_alive = self.agent2.single_step()
            self.notify_all_agents('B', self.agent2.get_body())
            
            self.print_board()
            #if not self.evaluate_board():
            #    game_on = False
            
    def notify_all_agents(self, symbol, body):
        self.agent1.notify(symbol, body)
        self.agent2.notify(symbol, body)
        self.enemy1.notify(symbol, body)
        self.enemy2.notify(symbol, body)