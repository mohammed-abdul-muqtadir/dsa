class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        m0 = nums.count(0)
        m1 = m0 + nums.count(1)
        m2 = m1 + nums.count(2)
        j = 0
        while j < len(nums):
            if m0 > j:
                nums[j] = 0
            elif m1 > j:
                nums[j] = 1
            elif m2 > j:
                nums[j] = 2
            j += 1


num = [2, 2, 2, 0, 0, 1, 1, 1]
sol = Solution()
print(sol.sortColors(num))
