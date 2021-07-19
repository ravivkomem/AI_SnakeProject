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

        b_height = len(self.board)
        b_width = len(self.board[0])

        # Get Starting Position
        snake_valid = False

        while not snake_valid:
            self.body = deque()
            curr_size = 0
            head_x = random.randrange(0, b_height)
            head_y = random.randrange(0, b_width)

            if self.board[head_x][head_y] != ' ':
                continue

            curr_size += 1
            self.body.append([head_x, head_y])

            last_x = head_x
            last_y = head_y
            while curr_size < self.size:
                next_x = last_x + 1
                next_y = last_y
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
        pass

    def get_score(self):
        pass