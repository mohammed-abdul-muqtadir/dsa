class Solution:
    def findDuplicate(self, nums):
        a = nums[0]
        b = nums[0]
        while True:
            a = nums[a]
            b = nums[nums[b]]
            if a == b:
                break
        a = nums[0]
        while a != b:
            a = nums[a]
            b = nums[b]
        return a




num = [2,5,9,6,9,3,8,9,7,1]
sol = Solution()
print(sol.findDuplicate(num))
