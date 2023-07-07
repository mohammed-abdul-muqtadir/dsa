class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums
        else:
            leftList = [x for x in nums if x < nums[0]]
            rightlist = [x for x in nums if x > nums[0]]
            self.nums = self.sortColors(leftList) + [nums[0]] + self.sortColors(rightlist)



num = [5, 4, 3, 2, 1]
sol = Solution()
print(sol.sortColors(num))
