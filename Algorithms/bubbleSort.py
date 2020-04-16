def bubbleSort(A):
    last_ptr = len(A) - 1
    while last_ptr != 0:
        for i in range(last_ptr):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
        last_ptr -= 1
    return A

A = [2,54,-2,3,1,5,123,-5,-22]
print(bubbleSort(A))