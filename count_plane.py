def num_of_planes(grid):
    plane_count = 0
    plane_tail_loc = []

    rows_size = len(grid)
    if rows_size == 0:
        return 0
    cols_size = len(grid[0])

    for i in range(rows_size):
        for j in range(cols_size):
            if grid[i][j] == 'P':
                if i != 0 and grid[i - 1][j] == 'P':
                    if (i - 1, j) not in plane_tail_loc:
                        plane_count += 1
                        plane_tail_loc.append((i, j))
                    else:
                        plane_tail_loc[plane_tail_loc.index((i - 1, j))] = (i, j)

                if j != 0 and grid[i][j - 1] == 'P':
                    if (i, j - 1) not in plane_tail_loc:
                        plane_count += 1
                        plane_tail_loc.append((i, j))
                    else:
                        plane_tail_loc[plane_tail_loc.index((i, j - 1))] = (i, j)
    return plane_count


grid = [ [ '.', '.', '.', 'P' ], [ '.', '.', '.', 'P' ], [ 'P', 'P', '.', 'P' ], [ '.', '.', '.', 'P' ] ]
print(num_of_planes(grid))
