def insertionSort(A):
    if len(A) <= 1:
        return A

    sort_ptr = 1

    while sort_ptr != len(A):
        for i in range(sort_ptr, 0, -1):
            if A[i - 1] > A[i]:
                A[i], A[i - 1] = A[i - 1], A[i]
        sort_ptr += 1
    
    return A

A = [2,54,-2,3,1,5,123,-5,-22]
print(insertionSort(A))