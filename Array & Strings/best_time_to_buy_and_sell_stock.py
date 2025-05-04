# My answer
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # Goal: find the max profit
    # Intuition keep a max until a new max is found

    highestProfit = 0 # Default for edge case

    lowest = prices[0]

    for i in range(len(prices)):
        profit = prices[i] - lowest
        highestProfit = max(highestProfit, profit)
        if prices[i] < lowest:
            lowest = prices[i]

    return highestProfit

# Time: O(n)
# Space: O(1)

# Optimal Solution for Bootcamp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            profit = price - min_price

            min_price = min(price, min_price)
            max_profit = max(profit, max_profit)

        return max_profit

# L, R pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Goal: Find max
        # Use l, r pointers

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # Profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            # Not profitable
            else:
                l = r

            r += 1 # We test every one

        return maxP

        # Time: O(n)
        # Space: O(1)
