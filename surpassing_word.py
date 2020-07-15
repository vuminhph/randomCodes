
def check_surpassing_word(word):
    word_size = len(word)
    last_gap = 0

    for i in range(word_size -  2):
        cur_gap = ord(word[i + 1]) - ord(word[i])
        if cur_gap < 0:
            cur_gap = -cur_gap

        if i != 0:
            if cur_gap < last_gap:
                return False
        last_gap = cur_gap

    return True

print(check_surpassing_word('superb'))