def power_of_three(num):
    if num % 3 != 0:
        return False

    while num != 0:
        if num == 1:
            return True
        if num % 3 != 0:
            return False
        num //= 3

print(power_of_three(9))
