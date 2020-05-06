from subsets_of_sum import find_subsets_of_sum

def main():
    val = [10, 40, 30, 50]
    wt = [5, 4, 6, 3]
    items = dict(zip(wt, val))
    weight = 10

    lookup = [-1 for i in range(weight + 1)]
    print(solve_knapsack(items, weight, lookup))


def solve_knapsack(items, weight, lookup):
    if weight in items.keys():
        return [weight for weight in items.keys() if items[weight] == max(items.values())]
    if lookup[weight] == -1:
        num_of_items = len(items)
        wt_lookup = [{} for i in range(num_of_items)]
        opt_weight_combinations = find_subsets_of_sum(list(items.keys()), num_of_items - 1, weight, wt_lookup)

        if opt_weight_combinations != [[]]:
            all_combinations = opt_weight_combinations + [solve_knapsack(items, weight - 1, lookup)]
            lookup[weight] = find_best_combination(items, all_combinations)
        else:
            lookup[weight] = solve_knapsack(items, weight - 1, lookup)
    
    return lookup[weight]

def find_best_combination(items, combinations):
    max_value = 0
    for combination in combinations:
        value = sum([items[wt] for wt in combination])
        if value > max_value:
            max_value = value
            best_combination = combination
    
    return best_combination

if __name__ == '__main__':
    main()