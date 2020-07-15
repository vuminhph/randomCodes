# O(kn)

def detectSubstring(txt, subStr):
    for i in range(len(txt) - len(subStr) + 1):
        found_subStr = True
        for j in range(len(subStr)):
            if txt[i + j] != subStr[j]:
                found_subStr = False
                break
        if found_subStr:
            return i
    return - 1

print(detectSubstring('home is where your cat is', 'cat'))
        
