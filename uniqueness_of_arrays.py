def uniques(arr):
    uniq_arr = []
    record = {}

    for num in arr:
        if record.get(num) is None:
            uniq_arr.append(num)
            record[num] = 0
    
    return uniq_arr

print(uniques([3, 5, 6, 9, 9, 4, 3, 12]))

