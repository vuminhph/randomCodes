def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    lookup = [-1 for i in range(len(arr))]
    global_max = ([], -1000)
    print(find_max_consecutive_subarray(len(arr) - 1, arr, lookup, global_max)[1])


def find_max_consecutive_subarray(index, arr, lookup, global_max):
    if index == 0:
        max_sub_arr = [arr[index]]
        max_sub_sum =  arr[index]

        init_max = (max_sub_arr, max_sub_sum)
        global_max = init_max
        return init_max, global_max
    
    if lookup[index] == -1:
        last_max_sub, global_max = find_max_consecutive_subarray(index - 1, arr, lookup, global_max)
        last_max_sub_arr = last_max_sub[0]
        last_max_sub_sum = last_max_sub[1]

        max_sub_sum = max(arr[index], last_max_sub_sum + arr[index])
        max_sub_arr = [arr[index]] if max_sub_sum == arr[index] else last_max_sub_arr + [arr[index]]

        lookup[index] = (max_sub_arr, max_sub_sum)
    
    if lookup[index][1] > global_max[1]:
            global_max = lookup[index]

    return lookup[index], global_max

if __name__ == '__main__':
    main()