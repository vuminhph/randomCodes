def missing_numbers(num_arr):
    if len(num_arr) <= 1:
        return None
    missing = []
    for i in range(1, len(num_arr)):
        if num_arr[i] != num_arr[i - 1] + 1:
            missing += [i for i in range(num_arr[i -1] + 1, num_arr[i])]
    return missing
  
print(missing_numbers([10, 11, 14, 17]))