arr = [9,7,0,3,9,8,6,5,7,6]
Sum = 2

def main():
    lookup = [{} for i in range(len(arr))]
    print(targetSum(len(arr) - 1, Sum, lookup))

def targetSum(index, sum, lookup):
    if index == 0:
        if arr[index] == sum and -arr[index] == sum:
            return 2
        elif arr[index] == sum or -arr[index] == sum:
            return 1
        return 0
    if lookup[index].get(sum) is None:
            lookup[index][sum] = targetSum(index - 1, sum - arr[index], lookup) + targetSum(index - 1, sum + arr[index], lookup)
    return lookup[index][sum]

if __name__ == '__main__':
    main()