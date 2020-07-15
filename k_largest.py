def k_largest(nums, k):
    nums.sort()
    print(nums)
    return nums[len(nums) - k:]

nums = [5, 16, 7, 9, -1, 4, 3, 11, 2]
print(k_largest(nums, 3))