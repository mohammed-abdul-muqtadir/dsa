class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        while j != i and i < len(nums):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
            elif j == i+1:
                j = len(nums) - 1
                i += 1
            else:
                j -= 1


n = [3, 2, 4, 4, 4, 4, 4, 4, 5, 7, 6, 7, 6, 5, 5, 4, 5, 55, 6, 4]
t = 60
sol = Solution()
print(sol.twoSum(n, t))
