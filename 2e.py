class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if num[fast] != 0 and num[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            if nums[slow] != 0:
                slow += 1
        print(nums)

num = [0,0,0,2,3,42,0,3,3,40,3,0,0]


sol = Solution()
sol.moveZeroes(num)