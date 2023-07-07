class Solution:
    def maxProfit(self, prices):
        mp = 0
        cheap_price = prices[0]
        for i in range(len(prices)):
            if cheap_price < prices[i] and mp <= prices[i] - cheap_price:
                mp = prices[i] - cheap_price

            if cheap_price > prices[i]:
                cheap_price = prices[i]

        return mp


num = [7, 1, 5, 3, 6, 4]
sol = Solution()
sol.maxProfit(num)
