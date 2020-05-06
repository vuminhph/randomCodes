def main():
    arr = [5,7,21,9]
    print(has_equal_subsets(arr))

def has_equal_subsets(arr):
    total_sum = sum(arr)
    if total_sum % 2 == 1:
        return False
    
    goal = total_sum // 2
    lookup = [{} for i in range(len(arr))]
    return if_subset_exist(arr, len(arr) - 1, goal, lookup)

def if_subset_exist(arr, index, sum, lookup):
    if index == 0:
        return arr[index] == sum
    if lookup[index].get(sum) is None:
        lookup[index][sum] = if_subset_exist(arr, index - 1, sum, lookup) or if_subset_exist(arr, index - 1, sum - arr[index], lookup)
    return lookup[index][sum]

if __name__ == '__main__':
    main()