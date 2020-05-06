def main():
    Top = [1,-1,-1,2,1,-1]
    Left = [2,3,-1,-1,-1]
    Right = [-1,-1,-1,1,-1]
    Bottom = [2,-1,-1,2,-1,3]
    Rules = [["L","R","L","R","T","T" ], 
            [ "L","R","L","R","B","B" ], 
            [ "T","T","T","T","L","R" ], 
            [ "B","B","B","B","T","T" ], 
            [ "L","R","L","R","B","B" ]]
    constraints = {
        'T' : Top,
        'L' : Left,
        'R' : Right,
        'B' : Bottom,
        'rules' : Rules
    }
    board = [[' ' for j in range(len(constraints['T']))] for i in range(len(constraints['L']))]

    if solve_puzzle((0, 0), board, constraints):
        print_board(board, constraints)
    else:
        print('No solution found')
    # print(get_next_position((1, 3), constraints))

def solve_puzzle(position, board, constraints):
    possible_placement = get_possible_placement(position, board, constraints)
    if len(possible_placement) == 0:
        return False

    pos_x = position[0]
    pos_y = position[1]

    original_L = constraints['L'][pos_x]
    original_R = constraints['R'][pos_x]
    original_T = constraints['T'][pos_y]
    original_B = constraints['B'][pos_y]
    original_constraints = {
        'L': original_L,
        'R': original_R,
        'T': original_T,
        'B': original_B
    }

    for placement in possible_placement:
        board[pos_x][pos_y] = placement
        if placement == '+':
            if constraints['T'][pos_y] != -1:
                constraints['T'][pos_y] = max(0, constraints['T'][pos_y] - 1)
            if constraints['L'][pos_x] != -1:
                constraints['L'][pos_x] = max(0, constraints['L'][pos_x] - 1)
        elif placement == '-':
            if constraints['B'][pos_y] != -1:
                constraints['B'][pos_y] = max(0, constraints['B'][pos_y] - 1)
            if constraints['R'][pos_x] != -1:
                constraints['R'][pos_x] = max(0, constraints['R'][pos_x] - 1)
        if position == (len(constraints['L']) - 1, len(constraints['T']) - 1):
            if if_board_solved(constraints):
                return True
        elif solve_puzzle(get_next_position(position, constraints), board, constraints) == True:
            return True
        reset_constraints(position, constraints, original_constraints)
    board[pos_x][pos_y] = ''
    return False 

def get_possible_placement(position, board, constraints):
    pos_x = position[0]
    pos_y = position[1]

    possible_placement = []
    
    if constraints['T'][pos_y] != 0 and constraints['L'][pos_x] != 0:
        possible_placement.append('+')
    if constraints['B'][pos_y] != 0 and constraints['R'][pos_x] != 0:
        possible_placement.append('-')
    
    type = constraints['rules'][pos_x][pos_y]
    half_value = get_half_value(position, type, board)

    if half_value == 'X':
        return ['X']
    if type == 'R' or type == 'B':
        possible_placement = ['-'] if half_value == '+' else ['+']
    else:
        possible_placement.append('X')
    
    last_values = []
    if type == 'L' or type == 'T':
        if pos_y > 0:
            last_values.append(board[pos_x][pos_y - 1])
        if pos_x > 0:
            last_values.append(board[pos_x - 1][pos_y])
    
    if len(last_values) != 0:
        for value in last_values:
            if value != 'X' and value in possible_placement:
                possible_placement.remove(value)
    
    return possible_placement

def reset_constraints(position, constraints, original_constraints):
    pos_x = position[0]
    pos_y = position[1]
    
    constraints['L'][pos_x] = original_constraints['L']
    constraints['R'][pos_x] = original_constraints['R']
    constraints['T'][pos_y] = original_constraints['T']
    constraints['B'][pos_y] = original_constraints['B']

def get_half_value(position, type, board):
    pos_x = position[0]
    pos_y = position[1]

    if type == 'R':
        return board[pos_x][pos_y - 1]
    if type == 'B':
        return board[pos_x - 1][pos_y]

def if_board_solved(constraints):
    for i in constraints['T']:
        if i > 0:
            return False
    for i in constraints['B']:
        if i > 0:
            return False
    for i in constraints['L']:
        if i > 0:
            return False
    for i in constraints['R']:
        if i > 0:
            return False
    return True

def get_next_position(position, constraints):
    pos_x = position[0]
    pos_y = position[1]

    if pos_y == len(constraints['T']) - 1:
        return (pos_x + 1, 0)
    return (pos_x, pos_y + 1)

def print_board(board, constraints):
    for i in range(len(constraints['L'])):
        for j in range(len(constraints['T'])):
            print(board[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()