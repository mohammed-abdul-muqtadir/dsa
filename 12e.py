class Solution:
    def maxArea(self, height):
        fa = 0
        i = 0
        j = len(height) - 1
        while i < j:
            
            if min(height[j], height[i]) * (j - i) > fa:
                fa = min(height[j], height[i]) * (j - i)

            elif height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return fa

n = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
print(sol.maxArea(n))
