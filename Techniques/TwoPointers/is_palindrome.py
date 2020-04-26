def is_palindrome(s):
    s = s.replace(' ', '')
    if len(s) % 2 == 0:
        return False
    if len(s) < 3:
        return True

    mid_ptr = len(s) // 2
    left_ptr = mid_ptr - 1
    right_ptr = mid_ptr + 1

    while True:
        if s[left_ptr].lower() != s[right_ptr].lower():
            # print(f'{s[left_ptr].lower()} - {s[right_ptr].lower()}')
            return False
        left_ptr -= 1
        right_ptr += 1
        if left_ptr == 0:
            return True

print(is_palindrome('A Santa Lived As a Devil At NASA'));

