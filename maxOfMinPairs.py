def max_of_min_pairs(nums):
    nums = sorted(nums)
    sum = 0
    for i in range(len(nums) - 2, -1, -2):
        sum += nums[i]

    return sum

# print(max_of_min_pairs([1, 3, 2, 6, 5, 4]));
