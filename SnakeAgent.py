import sys
import random
from collections import deque

class SnakeAgent:

    def __init__(self, board, strategy, symbol, size=5):
        self.board = board
        self.strategy = strategy
        self.body = None
        self.size = size
        self.score = 0
        self.symbol = symbol

        self.init_body()

    def init_body(self):

        rows_num = len(self.board)
        cols_num = len(self.board[0])

        # Get Starting Position (x = row, y = col)
        snake_valid = False

        while not snake_valid:
            self.body = deque()
            curr_size = 0
            head_x = random.randrange(0, rows_num)
            head_y = random.randrange(0, cols_num)

            if self.board[head_x][head_y] != ' ':
                continue

            curr_size += 1
            self.body.append([head_x, head_y])

            last_x = head_x
            last_y = head_y
            failed_attempts = 0
            while curr_size < self.size:
                direction = random.randrange(1, 5)
                (next_x, next_y) = self.change_location(last_x, last_y, direction)
                
                if (not 0 <= next_x < rows_num) or (not 0 <= next_y < cols_num) or (self.board[next_x][next_y] != ' ') or ([next_x, next_y] in self.body):
                    failed_attempts += 1
                    if failed_attempts == 10:
                        print('something is wrong')
                        sys.exit()
                    continue
                curr_size += 1

                self.body.append([next_x, next_y])

                last_x = next_x
                last_y = next_y

            snake_valid = True

        #self.body = deque([[6, 5], [6, 4], [6, 3]])
        for section in self.body:
            x = section[0]
            y = section[1]

            self.board[x][y] = self.symbol

    def single_step(self):
        valid_step = False
        while not valid_step:
            if self.strategy == None:
                direction = random.randrange(1, 5)
                (next_x, next_y) = self.change_location(self.body[0][0], self.body[0][1], direction)
                
            if (not 0 <= next_x < len(self.board)) or (not 0 <= next_y < len(self.board[0])) ([next_x, next_y] in self.body):
                continue
            
            valid_step = True
        self.update_body(next_x, next_y)
        
    def update_body(self):
        pass
    
    def get_score(self):
        pass
    
    def get_score_point(self):
        self.score += 1
    
    def change_location(self, x, y, mode):
        if mode == 1:
            x = x + 1
        if mode == 2:
            x = x - 1
        if mode == 3:
            y = y + 1
        if mode == 4:
            y = y - 1
        return x, y