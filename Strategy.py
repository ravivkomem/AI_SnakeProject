

def always_right(board, head, valid_steps):
    if [head[0],head[1]+1] in valid_steps:
        return [head[0],head[1]+1]
    return None

