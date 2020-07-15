def max_leaps(nums):
    return if_completable(0, nums)

def if_completable(index, arr):
    if index == len(arr) - 1:
        return True
    if index > len(arr) - 1:
        return False
    
    possible_hops = [index + i + 1 for i in range(arr[index])]
    for hop in possible_hops:
        if if_completable(hop, arr):
            return True
    return False

arr = [1, 3, 2, 2, 1]
print(max_leaps(arr))
