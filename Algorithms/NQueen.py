def print_solution(size, board):
    for i in range(size):
        for j in range(size):
            print(board[j][i],end=' ')
        print()

def if_attacks(size, board, location):
    x_loc = location[0]
    y_loc = location[1]

    for i in range(x_loc, -1, -1):
        if board[i][y_loc] == 1:
            return True

    for (diagonal_tl_x, diagonal_tl_y) in zip(range(x_loc, -1, -1), range(y_loc, -1, -1)):
        if board[diagonal_tl_x][diagonal_tl_y] == 1:
            return True

    for (diagonal_bl_x, diagonal_bl_y) in zip(range(x_loc, -1, -1), range(y_loc, size)):
       if board[diagonal_bl_x][diagonal_bl_y] == 1:
           return True

    return False

def NQueen():
    size = int(input("Enter board size: "))
    board = [[0 for i in range(size)] for j in range(size)]
    queens_placed = []

    # initialize queue, adding all possition in the first col to queue
    queens_queue = [(0, i) for i in range(size)]

    while len(queens_queue) != 0:
        current_queen = queens_queue.pop()
        if if_attacks(size, board, current_queen) == False:
            queens_placed.append(current_queen)
            current_queen_x = current_queen[0]
            current_queen_y = current_queen[1]
            board[current_queen_x][current_queen_y] = 1
            
            if current_queen[0] == size - 1:
                # return queens_placed
                print_solution(size, board)
                return 
            
            queens_queue += [(current_queen_x + 1, i) for i in range(size)]
        else:
            while len(queens_placed) != 0:
                last_queen = queens_placed[-1]
                keep_last_queen = False

                for i in range(len(queens_queue) - 1, -1, -1):
                    queen = queens_queue[i]
                    if queen[0] == last_queen[0] + 1:
                        keep_last_queen = True
                        break
                
                if keep_last_queen == False:
                    queens_placed.pop()
                    board[last_queen[0]][last_queen[1]] = 0
                else:
                    break
    
    print('No solution found')



# size = 4
# board = [[0 for i in range(size)] for j in range(size)]
# location = (2, 2)

# range = generate_range(size, location)
# # print(range)
# print(board)
# place_queen(board, range)
# print(board)
# remove_queen(board, range)
# print(board)
# print(if_attacks(size, board, (0, 3)))

NQueen()
        