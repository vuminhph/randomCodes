def main():
    # graph = [[0,1,1,1], 
    #         [1,0,1,0],
    #         [1,1,0,1],
    #         [1,0,1,0]]
    graph = [[0,1,1,1,0,0,0,0,0,0],
            [1,0,0,0,1,0,0,0,1,0],
            [1,0,0,0,1,1,1,1,0,0],
            [1,0,0,0,0,1,0,0,0,1],
            [0,1,1,0,0,1,0,1,0,0],
            [0,0,1,1,1,0,1,0,0,0],
            [0,0,1,0,0,1,0,0,1,0],
            [0,0,1,0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1,0,0,1],
            [0,0,0,1,0,0,0,1,1,0]]
    m = 3
    color = [-1 for i in range(len(graph))]
    print(m_coloring(m, 0, graph, color))

def get_neighbors(vertex, graph):
    neighbors = []
    for v in range(len(graph)):
        if graph[vertex][v] == 1:
            neighbors.append(v)
    return neighbors

def get_available_colors(neighbors, color, m):
    available_colors = [i for i in range(1, m + 1)]
    for neighbor in neighbors:
        if color[neighbor] in available_colors and color[neighbor] != -1:
            available_colors.remove(color[neighbor])
    return available_colors

def vertex_is_colored(vertex, color):
    return color[vertex] != -1

def m_coloring(m, vertex, graph, color):
    neighbors = get_neighbors(vertex, graph)
    available_colors = get_available_colors(neighbors, color, m)
    if len(available_colors) == 0:
        return False
    color[vertex] = available_colors[0]

    for neighbor in neighbors:
        if vertex_is_colored(neighbor, color):
            continue
        if m_coloring(m, neighbor, graph, color) == False:
            return False
    return color

if __name__ == '__main__':
    main()
