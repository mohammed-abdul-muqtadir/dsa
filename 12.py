class Solution:
    def maxArea(self, height):
        all = []
        for i in range(len(height)):
            for j in range(i, len(height)):
                if i < j:
                    all.append(min(height[j], height[i]) * (j - i))
        return max(all)


n = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
sol.maxArea(n)
