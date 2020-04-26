def cycleSort(arr):
    for i in range(len(arr) - 1):
        cycle_start = i
        location = 0
        while True:
            for elem in arr:
                if elem < arr[cycle_start]:
                    location += 1
            if arr[cycle_start] == arr[location]:
                break
            while arr[location] == arr[cycle_start]:
                location += 1
            arr[cycle_start], arr[location] = arr[location], arr[cycle_start]
            location = 0
    return arr

A = [4,5,7,2,3,4,8,6]
print(cycleSort(A))