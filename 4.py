class Solution:
    def maximumChocolates(self, aaa, m):
        avg = max(aaa)
        aaa.sort()
        for i in range(len(aaa) - m + 1):
            print(i+m-1,i)
            if aaa[i + m - 1] - aaa[i] < avg:
                avg = aaa[i + m - 1] - aaa[i]
        print(avg)


cp = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
sol = Solution()
sol.maximumChocolates(cp, m)
