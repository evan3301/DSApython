# TODO: Given array Prices[i], pick [i] lowest number to buy and [i] subsequent highest number to sell
# Subtract buy[i] and sell[i] to return profit, sell[i] must come after buy[i]

'''
Proposed solution:
    Traverse array to find smallest value and corresponding index
        Traverse array past that index and find highest value
            Subtract values associated with each index

            return subtracted value
'''

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        for i in prices:
            if i < min:
                i = min

        max = prices[i:]
        for j in prices[i:]:
            if j > max:
                j = max

        profit = prices[max] - prices[min]

        return profit
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Min() function to find minimum value of the array
        smallest = min(prices) 
        # Max () fumction to find maximum value of the array
        # From index prices[smallest:] onward
        largest = max(prices[smallest:])

        # Edge case for smallest == last element of array
        if smallest == prices[-1]:
            profit = 0
        else:
            profit = largest - smallest
        return profit