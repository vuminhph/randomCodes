def getSubsetSum(subset, arr):
    sum = 0
    for index in subset:
        sum += arr[index]
    return sum


def findNumOfSubset():
    arr = [1,2,3,3]
    sum = 6
    count = 0
    for i in range(0, len(arr)):
        if i + 1 != len(arr):
            count += findSubSet(i + 1, arr, [i], sum)
    print(count)

#  Test every subset, time complexity 0(2^n)
def findSubSet(index, arr, subset, sum):
        if getSubsetSum(subset, arr) + arr[index] == sum:
            print(subset + [index])
            return 1
        if getSubsetSum(subset, arr) + arr[index] > sum:
            return 0
        subset.append(index)
        count = 0
        for i in range(index + 1, len(arr)):
            count += findSubSet(i, arr, subset, sum)
        subset.pop()
        return count

# findNumOfSubset()

# Using dynamic programming
def main():
    sum = 6
    arr = [1,2,3,3]
    index_to_sum = [{} for i in range(len(arr))]
    subset_num = findNumOfSubsets(3, arr, sum, index_to_sum)
    print(index_to_sum)
    print(subset_num)

def findNumOfSubsets(index, arr, num, index_to_sum):
    if index == 0:
        if arr[index] == num:
            return 1
        else:
            return 0
    if index_to_sum[index].get(num) is None:
        if num - arr[index] < 1:
            index_to_sum[index][num] = findNumOfSubsets(index - 1, arr, num , index_to_sum)
            if arr[index] == num:
                index_to_sum[index][num] += 1
        else:
            index_to_sum[index][num] = findNumOfSubsets(index - 1, arr, num, index_to_sum) + findNumOfSubsets(index - 1, arr, num - arr[index], index_to_sum)
    return index_to_sum[index][num]


main()