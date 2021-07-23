import sys

def always_right(board, head, valid_steps):
    if [head[0],head[1]+1] in valid_steps:
        return [head[0],head[1]+1]
    return None

def max_manhattan_distance(board, head, valid_steps):
    # for Agents
    c_head = find_snake_head(board, 'C')
    d_head = find_snake_head(board, 'D')
    
    next_step = None
    max_distance = 0
    for step in valid_steps:
        cur_distance = min(calc_manhattan_distance(step, c_head), calc_manhattan_distance(step, d_head))
        if cur_distance > max_distance:
            max_distance = cur_distance
            next_step = step
    
    return next_step

def min_manhattan_distance(board, head, valid_steps):
    # for Enemies
    a_body = find_snake_body(board, 'A')
    b_body = find_snake_body(board, 'B')
    
    next_step = None
    min_dist = sys.maxsize
    for step in valid_steps:
        min_cur_dist = sys.maxsize
        for section in a_body:
            dist = calc_manhattan_distance(step, section)
            min_cur_dist = min(min_cur_dist, dist)
        for section in b_body:
            dist = calc_manhattan_distance(step, section)
            min_cur_dist = min(min_cur_dist, dist)
            
        if  min_cur_dist < min_dist:
            min_dist = min_cur_dist
            next_step = step
    
    return next_step

def calc_manhattan_distance(pos_src, pos_dst):
    if pos_dst is None:
        return sys.maxsize
    dist = abs(pos_src[0] - pos_dst[0]) + abs(pos_src[1] - pos_dst[1])
    return dist

def find_snake_head(board, symbol):
    snake_head_pos = None
    for r,row in enumerate(board):
        for c,cell in enumerate(row):
            if cell == symbol:
                snake_head_pos = [r,c]
    return snake_head_pos
    
def find_snake_body(board, symbol):
    snake_body = []
    for r,row in enumerate(board):
        for c,cell in enumerate(row):
            if cell == symbol.upper() or cell == symbol.lower():
                snake_body.append([r,c])
    return snake_body
    