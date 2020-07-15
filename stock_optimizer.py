def	stockOptimizer(prices):
    buy_price = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - buy_price)
        if prices[i] < buy_price:
            buy_price = prices[i]

    return max_profit

print(stockOptimizer([ 14,3,16,8,9,7,8,18,15,10,9 ]))
        