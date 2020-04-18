def build_matrix(size, matrix_list):
    matrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = matrix_list[i * 4 + j]
    return matrix

def build_solution(size, path):
    solution_matrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if (i, j) in path:
                solution_matrix[i][j] = 1
    return solution_matrix

def generate_possible_moves(location, matrix):
    possible_moves = []

    x_loc = location[0]
    y_loc = location[1]
    
    if x_loc + 1 in range(size) and matrix[x_loc + 1][y_loc] == 1:
        possible_moves.append( (x_loc + 1, y_loc) )
    if y_loc + 1 in range(size) and matrix[x_loc][y_loc + 1] == 1:
        possible_moves.append( (x_loc, y_loc + 1) )
    if y_loc - 1 in range(size) and matrix[x_loc][y_loc - 1] == 1:
        possible_moves.append( (x_loc, y_loc - 1) )
    if x_loc - 1 in range(size) and matrix[x_loc - 1][y_loc] == 1:
        possible_moves.append( (x_loc - 1, y_loc) )
    return possible_moves

def find_path(start, desination, matrix):
    if start == desination:
        return [start]
    
    possible_moves = generate_possible_moves(start, matrix)

    if len(possible_moves) == 0:
        return None
    
    for move in possible_moves:
        path = find_path(move, desination, matrix)
        if path is not None:
            return [start] + path

def ratInAMaze_recursive(size, matrix_list):
    start = (0, 0)
    desination = (size - 1, size - 1)
    matrix = build_matrix(size, matrix_list)

    path =  find_path(start, desination, matrix)
    
    solution = build_solution(size, path)
    if solution == None:
        print("Solution doesn't exist")
        return
    print(solution)

size = 4
# matrix_list = [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
matrix_list = [1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1]
matrix = build_matrix(size, matrix_list)
# print(build_matrix(size, matrix))
# print(generate_possible_moves((3, 1), matrix))

ratInAMaze_recursive(size, matrix_list)