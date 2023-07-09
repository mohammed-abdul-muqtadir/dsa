class Solution:

    def findDuplicates(self, nums):
        a = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num) - 1] = -nums[abs(num)-1]
            else:
                a.append(abs(num))


nu = [1,2,3,2]

sol = Solution()
print(sol.findDuplicates(nu))
