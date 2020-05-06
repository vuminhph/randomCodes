
def main():
    val = [10, 40, 30, 50]
    wt = [5, 4, 6, 3]
    items = dict(zip(wt, val))
    weight = 10
    lookup = [[-1 for i in range(weight + 1)] for j in range(len(items))]

    print(solve_knapsack(len(items) - 1, items, weight, lookup)[0])

def solve_knapsack(index, items, capacity, lookup):
    if index == 0:
        first_item = list(items.keys())[0]
        if capacity >= first_item:
            return ( [first_item], items[first_item] )
        else:
            return ( [], 0 )

    if lookup[index][capacity] == -1:
        cur_item = list(items.keys())[index]
        capacity_if_incl = capacity - cur_item

        if capacity_if_incl >= 0:
            last_incl = solve_knapsack(index - 1, items, capacity_if_incl, lookup)
            incl_combination = last_incl[0]
            incl_value = last_incl[1]
            
            incl_combination.append(cur_item)
            incl_value += items[cur_item]
        else:
            incl_combination = []
            incl_value = 0

        last_not_incl = solve_knapsack(index - 1, items, capacity, lookup)
        not_incl_combination = last_not_incl[0]
        not_incl_value = last_not_incl[1]

        max_value = max(incl_value, not_incl_value)
        opt_combination = incl_combination if max_value == incl_value else not_incl_combination

        lookup[index][capacity] = (opt_combination, max_value)

    return lookup[index][capacity]

if __name__ == '__main__':
    main()