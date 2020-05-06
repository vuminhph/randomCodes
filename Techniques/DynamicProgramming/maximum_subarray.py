def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    lookup = [-1 for i in range(len(arr))]
    print(find_max_subarray(len(arr) - 1, arr, lookup))

def find_max_subarray(index, arr, lookup):
    if index == 0:
        max_sub_arr = [arr[index]]
        max_sub_sum =  arr[index]
        return (max_sub_arr, max_sub_sum)
    
    if lookup[index] == -1:
        last_max_sub = find_max_subarray(index - 1, arr, lookup)
        last_max_sub_arr = last_max_sub[0]
        last_max_sub_sum = last_max_sub[1]

        max_sub_sum = max(last_max_sub_sum, last_max_sub_sum + arr[index])
        max_sub_arr = last_max_sub_arr if max_sub_sum == last_max_sub_sum else last_max_sub_arr + [arr[index]]
        lookup[index] = (max_sub_arr, max_sub_sum)

    return lookup[index]

if __name__ == '__main__':
    main()