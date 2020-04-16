
#out of nickles

def min_coins(cents):
    coins = [25, 10, 1]
    num_coins = 0

    while True:
        if cents <= 0:
            break
        if cents in coins:
            num_coins += 1
            break
        min_remainder = [1000, 0]
        for i, coin in enumerate(coins[:-1]):
            if min_remainder[0] >= cents % coin:
                min_remainder = [cents % coin, i]
        num_coins += int(cents / coins[min_remainder[1]])
        cents = cents % coins[min_remainder[1]]
    
    return num_coins


print(min_coins(31))
