def maxProfit(prices: list[int]) -> int:
    min_num = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        profit = max(profit, prices[i]-min_num)
        min_num = min(min_num, prices[i])