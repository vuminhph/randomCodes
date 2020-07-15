def sortString(s):
    char_info = {}

    for char in s:
        if char_info.get(ord(char)) is None:
            char_info[ord(char)] = [char, 1]
        else:
            char_info[ord(char)][1] += 1
            
    char_order = sorted(list(char_info.keys()))
    result_str = []

    while True:
        if len(char_order) == 0:
            return ''.join(result_str)


        for i in range(len(char_order)):
            result_str.append(char_info[char_order[i]][0])

            char_info[char_order[i]][1] -= 1
            if char_info[char_order[i]][1] == 0:
                char_order[i] = -1

        char_order = [char for char in char_order if char != -1]
        
        for i in range(len(char_order) - 1, -1, -1):
            result_str.append(char_info[char_order[i]][0])

            char_info[char_order[i]][1] -= 1
            if char_info[char_order[i]][1] == 0:
                char_order[i] = -1

        char_order = [char for char in char_order if char != -1]

print(sortString('spo'))