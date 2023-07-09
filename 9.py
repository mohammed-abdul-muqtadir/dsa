class Solution:
    def maxProfit(self, prices):
        minP = 0
        fp = 0
        for maxP in range(1, len(prices)):
            if prices[maxP] > prices[minP]:
                fp += prices[maxP] - prices[minP]
                minP = maxP
            if prices[minP] > prices[maxP]:
                minP = maxP

        return fp


n = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(n))
