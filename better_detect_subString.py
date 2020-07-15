# O(n)

def detectSubstring(txt, subStr):
    prefix = [-1 for i in range(len(txt))]
    count = -1

    for i in range(len(txt)):
        if txt[i] == subStr[0]:
            count = 0
            prefix[i] = count
        elif count != -1:
            count += 1
            prefix[i] = count

            if count == len(subStr) - 1:
                count = -1

    found_Substr = False

    for i in range(len(txt)):
        if prefix[i] == -1:
            continue

        if txt[i] == subStr[prefix[i]]:
            if prefix[i] == 0:
                found_Substr = True
            if found_Substr == False:
                continue

            if prefix[i] == len(subStr) - 1:
                return i - prefix[i]

        else:
            found_Substr = False
    
    return -1

print(detectSubstring('thepigflewwow','flew'))