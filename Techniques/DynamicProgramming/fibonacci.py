from time import process_time as time

def main():
    num = int(input("Enter the location of fibonacci number: "))
    lookup = [None for i in range(num + 1)]

    start1 = time()
    fib_number = fibonacci_topdown(num, lookup)
    end1 = time()
    print(f'{fib_number} - {end1 - start1}')

    start2 = time()
    fib_number = fibonacci_bottomup(num)
    end2 = time()
    print(f'{fib_number} - {end2 - start2}')

#  find fibonacci number using dynamic programming top down method
def fibonacci_topdown(num, lookup):
    if num == 0 or num == 1:
        lookup[num] = num

    if lookup[num] is None:
        lookup[num] = fibonacci_topdown(num - 1, lookup) + fibonacci_topdown(num - 2, lookup)
    
    return lookup[num]

def fibonacci_bottomup(num):
    fib = [0 for i in range(num + 1)]
    fib[1] = 1

    for i in range(2, num + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[-1]


if __name__ == '__main__':
    main()