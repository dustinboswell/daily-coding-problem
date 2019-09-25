'''
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

def max_profit(prices):
    # mins[x] = min(prices[0:x+1])
    mins = [prices[0]]
    for p in prices[1:]:
        mins.append(min(mins[-1], p))
    return max(prices[i] - mins[i] for i in range(len(prices)))

assert max_profit([1]) == 0
assert max_profit([2, 1]) == 0
assert max_profit([1, 2]) == 1
assert max_profit([9, 11, 8, 5, 7, 10]) == 5
