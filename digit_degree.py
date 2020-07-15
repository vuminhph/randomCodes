def get_degree(num):
    degree = 0
    while True:
        if num < 10:
            break

        cur_num = num
        sum_digit = 0

        while cur_num > 0:
            cur_digit = cur_num % 10 
            sum += cur_digit
            cur_num //= 10
        
        num = sum_digit
        degree += 1

    print(degree)    

get_degree(91)    