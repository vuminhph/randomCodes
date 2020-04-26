def zeroToTheEnd(arr):
    insert_ptr = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_ptr] = arr[i]
            insert_ptr += 1
    for j in range(insert_ptr, len(arr)):
        arr[j] = 0
    return arr

arr = [0,2,41,5,0,15,2]
print(zeroToTheEnd(arr))