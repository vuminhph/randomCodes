# find least possitive number from range(min, max + 1) of array

from math import inf

def least_missing_pos(nums):
    low_bound = inf
    high_bound = -1

    for num in nums:
        if num >= 0 and num < low_bound:
            low_bound = num
        if num > high_bound:
            high_bound = num

    if low_bound == inf:
        low_bound = 0

    range_check = {i : False for i in range(low_bound + 1, high_bound)}

    for num in nums:
        if range_check.get(num) == False:
            range_check[num] = True

    for key, value in range_check.items():
        if value == False:
            return key

    return low_bound - 1 if low_bound != 0 else high_bound + 1

nums = [0,3,1,2]
print(least_missing_pos(nums))