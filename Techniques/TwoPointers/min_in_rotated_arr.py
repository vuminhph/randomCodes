def get_minimum(nums):
    left = 0
    right = len(nums) - 1
    return get_minimum_utils(nums, left, right)

def get_minimum_utils(nums, left, right):
    mid_ptr = (right + left + 1) // 2
    bef_mid = mid_ptr - 1
    aft_mid = mid_ptr + 1

    if nums[bef_mid] != nums[mid_ptr] - 1:
        return nums[mid_ptr]
    if nums[aft_mid] != nums[mid_ptr] + 1:
        return nums[aft_mid]

    if left == right - 2:
        return False
        
    left_min = get_minimum_utils(nums, left, mid_ptr)
    right_min = get_minimum_utils(nums, mid_ptr, right)

    return left_min if left_min is not False else right_min

        