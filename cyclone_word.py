def check_cyclone_word(word):
    word_size = len(word)
    if word_size < 2:
        return False

    char_arr = []
    head_ptr = 0
    tail_ptr = len(word) - 1

    while head_ptr < tail_ptr:
        char_arr += [word[head_ptr].lower(), word[tail_ptr].lower()]
        head_ptr += 1
        tail_ptr -= 1

    char_arr.append(word[head_ptr])
    
    for i in range(1, word_size):
        if char_arr[i] < char_arr[i - 1]:
            return False
    return True
    

print(check_cyclone_word('hmzni'))
