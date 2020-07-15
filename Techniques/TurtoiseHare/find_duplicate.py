# find duplicate number in an array with elemements in range(1,n)
# array has length n -1

def find_duplicate(arr):
    turtoise = arr[0]
    hare = arr[0]

    while turtoise != hare:
        turtoise = arr[turtoise]
        hare = arr[arr[hare]]

    ptr1 = arr[0]
    ptr2 = turtoise

    while ptr1 != ptr2:
        ptr1 = arr[ptr1]
        ptr2 = arr[ptr2]

    return ptr1


arr = [1,4,3,5,6,1,2]
print(find_duplicate(arr))