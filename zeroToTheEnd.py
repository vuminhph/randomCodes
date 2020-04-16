def zeroToTheEnd(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.append(0)
            arr.pop(i)
    return arr

arr = [0,2,41,5,0,15,2]
print(zeroToTheEnd(arr))