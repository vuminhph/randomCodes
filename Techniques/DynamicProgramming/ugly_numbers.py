def main():
    n = 11
    ugly_numbers = get_ugly_numbers(n)
    print(ugly_numbers)

def get_ugly_numbers(n):
    for i in range(n):
        if i == 0:
            i2 = 0
            i3 = 0
            i5 = 0
            ugly_numbers = [1]
            continue
        
        last_mul_2 = ugly_numbers[i2] * 2
        last_mul_3 = ugly_numbers[i3] * 3
        last_mul_5 = ugly_numbers[i5] * 5

        last_num = min(last_mul_2, last_mul_3, last_mul_5)
        ugly_numbers.append(last_num)

        if last_num == last_mul_2:
            i2 += 1
        if last_num == last_mul_3:
            i3 += 1
        if last_num == last_mul_5:
            i5 += 1

    return ugly_numbers

if __name__ == '__main__':
    main()
        