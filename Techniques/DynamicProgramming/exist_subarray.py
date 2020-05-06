def main():
    arr = [1,2,3]
    sum = 3
    print(subarray_sum(arr, sum))

def subarray_sum(arr, sum):
    if len(arr) == 0:
        return False
        
    lookup = [{} for i in range(len(arr))]
    return find_subarray(len(arr) - 1, arr, sum, lookup)

def find_subarray(index, arr, sum, lookup):
    if index == 0:
        if arr[index] == sum or sum == 0:
            return True
        else:
            return False

    if lookup[index].get(sum) is None:
        lookup[index][sum] = find_subarray(index - 1, arr, sum ,lookup) or find_subarray(index - 1, arr, sum - arr[index], lookup)
    
    return lookup[index][sum]

if __name__ == '__main__':
    main()