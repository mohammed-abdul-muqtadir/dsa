class Solution:
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(len(nums)-1):
            if nums[fast] != nums[fast+1]:
                nums[slow+1] = nums[fast+1]
                slow += 1
        return slow +1


n = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
sol = Solution()
sol.removeDuplicates(n)
