def product_except_self(nums):
    product = 1
    for num in nums:
        product *= num
    for i in range(len(nums)):
        nums[i] = int(product / nums[i])
    return nums

def product_except_self_no_division(nums):
    product_left = [1 for i in nums]
    product_right = [1 for i in nums]
    
    product = 1
    for i in range(len(nums)):
        product_left[i] = product
        product *= nums[i]
    product = 1
    for j in range(len(nums) - 1, -1, -1):
        product_right[j] = product
        product *= nums[j]

    for k in range(len(nums)):
        nums[k] = product_left[k] * product_right[k]
    
    return nums

nums = [1,2,4,16]
# print(product_except_self(nums))
print(product_except_self_no_division(nums))

