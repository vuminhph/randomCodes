def get_bell_number(n):
    lookup = [{} for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i:
                lookup[i][j] = 1
            else:
                lookup[i][j] = lookup[i - 1][j] * j + lookup[i - 1][j - 1]

    return sum(lookup[n].values())

print(get_bell_number(6))    