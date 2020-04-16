import re

def reverse_only_alpha(s):
    head_index = 0
    tail_index = len(s) - 1
    output = [char for char in s]
    
    def find_next_alpha_indices(head_index, tail_index):
        while not s[head_index].isalpha():
            head_index += 1
        while not s[tail_index].isalpha():
            tail_index -= 1
        return (head_index, tail_index)

    head_index, tail_index = find_next_alpha_indices(head_index, tail_index)

    while head_index < tail_index:
        output[head_index] = s[tail_index]
        output[tail_index] = s[head_index]
        head_index += 1
        tail_index -= 1
        head_index, tail_index = find_next_alpha_indices(head_index, tail_index)

    return ''.join(output)

def reverse_array(arr):
    return arr[::-1]

print(reverse_only_alpha("sea!$hells3"))


