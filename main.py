from Game import Game
import matplotlib.pyplot as plt

avg_agent_scoreA = [[0] * 5 for _ in range(5)]
avg_agent_scoreB = [[0] * 5 for _ in range(5)]

board_size = 4
while board_size <= 6:
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::', board_size)
    
    s = 0
    while s < 5:
        avg_scoreA = 0
        avg_scoreB = 0
        grid_size = board_size**2
        
        n = 100
        for i in range(100):
            try:
                game = Game(strategy=s, rows=grid_size, cols=grid_size)
            except Exception:
                n -= 1
                continue
            scoreA, scoreB = game.play()
            avg_scoreA += scoreA
            avg_scoreB += scoreB
        
        avg_scoreA /= n
        avg_scoreB /= n
        
        if s == 0:
            print("-----Always Right-----")
        elif s == 1:
            print("-----Manhattan Distance-----")
        elif s == 2:
            print("-----Euclidian Distance-----")
        elif s == 3:
            print("-----Manhattan Minimax Search Tree-----")
        elif s == 4:
            print("-----Euclidian Minimax Search Tree-----")
        
        print("Score A: ", end='')
        print(avg_scoreA)
        print("Score B: ", end='')
        print(avg_scoreB)
        
        avg_agent_scoreA[board_size-4][s] = avg_scoreA
        avg_agent_scoreB[board_size-4][s] = avg_scoreB
        
        s += 1
    
    board_size += 1
    
x_ticks = [16, 25, 36]
l1,l2,l3,l4,l5 = plt.plot(x_ticks, avg_agent_scoreA[:][0], 'r',
                          x_ticks, avg_agent_scoreA[:][1], 'g',
                          x_ticks, avg_agent_scoreA[:][2], 'b',
                          x_ticks, avg_agent_scoreA[:][3], 'c',
                          x_ticks, avg_agent_scoreA[:][4], 'k')
plt.legend([l1, l2, l3, l4, l5], ['Always Right', 'Manhattan Distance', 'Euclidian Distance', 'Manhattan Minimax Search Tree', 'Euclidian Minimax Search Tree'])
plt.xlabel('grid_size')
plt.ylabel('average agent score A')
plt.show()

x_ticks = [16, 25, 36]
l1,l2,l3,l4,l5 = plt.plot(x_ticks, avg_agent_scoreB[:][0], 'r',
                          x_ticks, avg_agent_scoreB[:][1], 'g',
                          x_ticks, avg_agent_scoreB[:][2], 'b',
                          x_ticks, avg_agent_scoreB[:][3], 'c',
                          x_ticks, avg_agent_scoreB[:][4], 'k')
plt.legend([l1, l2, l3, l4, l5], ['Always Right', 'Manhattan Distance', 'Euclidian Distance', 'Manhattan Minimax Search Tree', 'Euclidian Minimax Search Tree'])
plt.xlabel('grid_size')
plt.ylabel('average agent score B')
plt.show()