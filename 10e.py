

class Solution:
    def subarraysDivByK(self, nums, k):
        count = [0]*k
        sum = 0
        for num in nums:
            sum += num
            count[sum%k] += 1

        result = count[0]
        for c in count:
            result += (c*(c-1))//2
        return result

no = [4, 5, 0, -2, -3, 1]
h = 5
sol = Solution()
print(sol.subarraysDivByK(no, h))
