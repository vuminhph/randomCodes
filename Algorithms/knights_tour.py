SIZE = 8

def generate_possible_moves(location):
    def is_valid_move(x, y):
        return x in range(SIZE) and y in range(SIZE)
    x_loc = location[0]
    y_loc = location[1]
    possible_moves = []
    for i in range(1, 3):
        for j in range(1,3):
            if i == j:
                continue
            x = x_loc + i
            y = y_loc + j
            if is_valid_move(x, y):
                possible_moves.append((x, y))
            x = x_loc + i
            y = y_loc - j
            if is_valid_move(x, y):
                possible_moves.append((x, y))
            x = x_loc - i
            y = y_loc + j
            if is_valid_move(x, y):
                possible_moves.append((x, y))
            x = x_loc - i
            y = y_loc - j
            if is_valid_move(x, y):
                possible_moves.append((x, y))
    return possible_moves

def is_board_cleared(board_visited):
    for row in board_visited:
        if False in row:
            return False
    return True

def print_path(path):
    for i in range(SIZE):
        for j in range(SIZE):
            order = path.index( (i, j) )
            print(order, end='\t')
        print()

def knightsTour():
    board_visited = [[False for i in range(SIZE)] for j in range(SIZE)]
    path = []

    board_visited[0][0] = True
    path_queue = [(0, 0)]
    while not is_board_cleared(board_visited):
        location = path_queue.pop()
        board_visited[location[0]][location[1]] = True
        path.append(location)
        for move in generate_possible_moves(location):
            if board_visited[move[0]][move[1]] == False:
                path_queue.append(move)
    print_path(path)

if __name__ == '__main__':
    # print(generate_possible_moves((2, 1)))
    knightsTour()