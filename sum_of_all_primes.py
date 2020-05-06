def sumOfPrimes(n):
    if n < 2:
        return 0
    
    prime_nums = []
    for i in range(2, n + 1):
        if check_if_prime(i):
        # if check_if_prime_optimized(i):
            prime_nums.append(i)
    
    print(prime_nums)
    return sum(prime_nums)

def check_if_prime(num):
    for j in range(2, num // 2 + 1):
        if num % j == 0:
            return False
    return True

# Doesn't work yet
def check_if_prime_optimized(num):
    if num % 2 == 0 or num % 3 == 0:
        if num == 2 or num == 3:
            return True
        return False
    if (num - 1) % 6 == 0 or (num + 1) % 6 == 0:
        if num != 5 and num % 5 == 0:
            return False
        return True
    return False

print(sumOfPrimes(100))
# print(check_if_prime_optimized(7))