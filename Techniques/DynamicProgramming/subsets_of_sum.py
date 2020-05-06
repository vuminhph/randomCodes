def main():
    sum = 7
    arr = [5,4,6,3]

    lookup = [{} for i in range(len(arr))]
    print(find_subsets_of_sum(arr, len(arr) - 1, sum, lookup))

def find_subsets_of_sum(arr, index, sum, lookup):
    if index == 0:
        if arr[index] == sum:
            lookup[index][sum] =  [[arr[index]]]
        else:
            lookup[index][sum] = [[]]
        
        return lookup[index][sum]

    if lookup[index].get(sum) is None:
        arrs_incl_cur = []
        if sum - arr[index] >= 0:
            arrs_incl_cur = find_subsets_of_sum(arr, index - 1, sum - arr[index], lookup)
            
            if arrs_incl_cur == [[]]:
                if sum == arr[index]:
                    arrs_incl_cur = [[arr[index]]]
                else:
                    arrs_incl_cur = []
            else:
                arrs_incl_cur = [array + [arr[index]] for array in arrs_incl_cur]


        arrs_not_incl_cur = find_subsets_of_sum(arr, index - 1, sum, lookup)
        if arrs_not_incl_cur == [[]]:
            arrs_not_incl_cur = []
        
        if arrs_not_incl_cur == [] and arrs_incl_cur == []:
            lookup[index][sum] = [[]]
        else:
            lookup[index][sum] = arrs_not_incl_cur
            for array in arrs_incl_cur:
                if array not in arrs_not_incl_cur:
                    lookup[index][sum].append(array)

    return lookup[index][sum]

if __name__ == '__main__':
    main()