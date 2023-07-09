class Solution:
    def subarraysDivByK(self, nums, k):
        fa = 0
        length = len(nums)
        for i in range(1, length + 1):
            for j in range(length - i + 1):
                if sum(nums[j:j + i]) % k == 0 and len(nums[j:j + i]) == i:
                    print(nums[j:j + i])
                    fa += 1
        return fa


no = [4, 5, 0, -2, -3, 1]
h = 5
sol = Solution()
print(sol.subarraysDivByK(no, h))
