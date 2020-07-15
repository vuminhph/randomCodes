def get_nth_catalan(n):
    lookup = [-1 for i in range(n + 1)]
    print(find_nth_catalan(n, lookup))

def find_nth_catalan(n, lookup):
    if n < 2:
        return 1
    if lookup[n] == -1:
        n_catalan = 0
        for i in range(n):
            n_catalan += find_nth_catalan(i, lookup) * find_nth_catalan(n - 1 - i, lookup)
        lookup[n] = n_catalan
    return lookup[n]

get_nth_catalan(9)