class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)
        for i in range(n):
            compliment = target - nums[i]
            if compliment in numMap:
                return [numMap[compliment], i]
            else:
                numMap[nums[i]] = i
        return []


no = [3, 3]
t = 6
sol = Solution()
print(sol.twoSum(no, t))
