class Solution:
    def maxProfit(self, prices):
        mp = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] >= mp:
                    mp = prices[j] - prices[i]
        return mp





lis = [7,6,4,3,1]
sol = Solution()
sol.maxProfit(lis)