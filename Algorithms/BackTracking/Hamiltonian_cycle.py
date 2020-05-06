def main():
    # graph = [[0,1,0,1,0],
    #     [1,0,1,1,1],
    #     [0,1,0,0,1],
    #     [1,1,0,0,1],
    #     [0,1,1,1,0]]

    graph = [[0,1,1,1,0,0],
            [1,0,1,0,1,1],
            [1,1,0,1,1,0],
            [1,0,1,0,1,0],
            [0,1,1,1,0,1],
            [0,1,0,0,1,0]]
    path = []
    if found_cycle(0, graph, path):
        print(path)
    else:
        print("Hamiltonian Cycle doesn't exist")
    
def get_possible_moves(vertex, graph, path):
    possible_moves = []
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and i not in path:
            possible_moves.append(i)
    return possible_moves

def if_edge_exist(vertex1, vertex2, graph):
    return graph[vertex1][vertex2] == 1

def found_cycle(vertex, graph, path):
    path.append(vertex)
    if len(path) == len(graph):
        if if_edge_exist(vertex, path[0], graph):
            return True
        else:
            path.pop()
            return False
    
    moves = get_possible_moves(vertex, graph, path)
    if len(moves) == 0:
        path.pop()
        return False
    else:
        for move in moves:
            if found_cycle(move, graph, path) == True:
                return True
        path.pop()
        return False


if __name__ == '__main__':
    main()