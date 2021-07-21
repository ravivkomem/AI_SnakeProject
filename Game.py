from SnakeAgent import SnakeAgent

class Game:

    def __init__(self, rows=14, cols=13):
        self.board = [[' '] * cols for _ in range(rows)]
        self.agent1 = SnakeAgent(self.board, strategy=None, symbol='A')
        self.agent2 = SnakeAgent(self.board, strategy=None, symbol='B')
        self.enemy1 = SnakeAgent(self.board, strategy=None, symbol='C')
        self.enemy2 = SnakeAgent(self.board, strategy=None, symbol='D')


    def print_board(self):
        print('-' * len(self.board[0]))
        for row in self.board:
            print(''.join(row))
        print('-' * len(self.board[0]))
        
    def play(self):
        game_on = True
        while game_on:
            self.agent1.single_step()
            self.agent2.single_step()
            self.enemy1.single_step()
            self.enemy2.single_step()
            self.update_board()
            self.evaluate_board()