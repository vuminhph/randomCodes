def missingInUnsorted(arr, lowerBound, upperBound):
    checkList = {i : 0 for i in range(lowerBound, upperBound + 1)}
    for num in arr:
        if checkList[num] == 0:
            checkList[num] = 1

    for key in checkList.keys():
        if checkList[key] == 0:
            return key
