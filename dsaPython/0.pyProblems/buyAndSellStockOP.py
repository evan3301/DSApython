'''
Proposed solution:
Sliding window:

    Two pointers:
        Left pointer on day 1
        Right pointer on day 2

        for i in range(len(profits)):
            if left pointer > right pointer:
                # Negative profit
                Move whole pointer system 1 index to right
            else:
                store profit in list
                move right pointer 1 index to right

Time complexity: Two Ptr solution -> O(n)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1    # Initialize pointers
        max_profit = 0        # Initialize profit

        # While right has not exited bounds of list
        while right < len(prices):
            # If profitable
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                # Compare to max_profit value; if more profitable, update max_profit
                max_profit = max(max_profit, profit)
            else:
                # If not profitable, move left pointer to right pointer
                l = r
            # For every iteration, increment right pointer 1 index to right
            r += 1

            return max_profit