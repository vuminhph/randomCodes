SIZE = 9

def main():
    board = [[0,0,0,7,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [0,0,0,4,3,0,2,0,0],
            [0,0,0,0,0,0,0,0,6],
            [0,0,0,5,0,9,0,0,0],
            [0,0,0,0,0,0,4,1,8],
            [0,0,0,0,8,1,0,0,0],
            [0,0,2,0,0,0,0,5,0],
            [0,4,0,0,0,0,3,0,0]]
    if solve_board((0,0), board):
        print_board(board)
    else:
        print('No solution found')
    # print(get_possible_numbers((1,4), board))

def solve_board(position, board):
    pos_x = position[0]
    pos_y = position[1]  
    next_position = get_next_position(position)
    
    if board[pos_x][pos_y] != 0:
        return solve_board(next_position, board)

    possible_numbers = get_possible_numbers(position, board)
    if len(possible_numbers) == 0:
        return False

    if position == (SIZE - 1, SIZE - 1):
        board[pos_x][pos_y] = possible_numbers[0]
        return True

    for num in possible_numbers:
        board[pos_x][pos_y] = num
        if solve_board(next_position, board) == True:
            return True
    board[pos_x][pos_y] = 0
    return False

def get_possible_numbers(position, board):
    pos_x = position[0]
    pos_y = position[1]
    possible_numbers = [i + 1 for i in range(len(board))]
    
    # check rows, columns
    for i in range(len(board)):
        if board[pos_x][i] != 0 and board[pos_x][i] in possible_numbers:
            possible_numbers.remove(board[pos_x][i])
        if board[i][pos_y] != 0 and board[i][pos_y] in possible_numbers:
            possible_numbers.remove(board[i][pos_y])
    # check neighborhood
    col_x = pos_x // 3 * 3
    col_y = pos_y // 3 * 3
    for i in range(col_x, col_x + 3):
        for j in range(col_y, col_y + 3):
            if board[i][j] != 0 and board[i][j] in possible_numbers:
                possible_numbers.remove(board[i][j])
    
    return possible_numbers

def get_next_position(position):
    pos_x = position[0]
    pos_y = position[1]
    if pos_y == SIZE - 1:
        next_position = (pos_x + 1, 0)
    else:
        next_position = (pos_x, pos_y + 1)
    return next_position

def print_board(board):
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()

