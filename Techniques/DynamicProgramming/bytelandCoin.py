
bl_coins = {}
def main():
    print(findMaxInDollar(144))

def findMaxInDollar(n):
    if n == 0 or n == 1:
        bl_coins[n] = n
    if bl_coins.get(n) == None:
        bl_coins[n] = max(n, findMaxInDollar(n // 2) + findMaxInDollar(n // 3) + findMaxInDollar(n // 4))
    return bl_coins[n]

if __name__ == '__main__':
    main()
