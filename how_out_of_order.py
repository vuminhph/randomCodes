def inversions(arr):
    num_inversions = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                num_inversions += 1

    return num_inversions

print(inversions([5,4,3,2,1]))
