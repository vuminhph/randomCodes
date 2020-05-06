def sorted_two_sum(nums, goal):
    begin_ptr = 0
    end_ptr = len(nums) - 1
    output = []
    
    while begin_ptr < end_ptr:
        sum = nums[begin_ptr] + nums[end_ptr]
        if sum > goal:
            end_ptr -= 1
        elif sum < goal:
            begin_ptr += 1
        else:
            output += [begin_ptr, end_ptr]
            begin_ptr += 1
        
    return output

nums = [3,6,13,14]
goal = 16
print(sorted_two_sum(nums, goal))