class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = len(matrix[0])
        row = len(matrix)
        print(col)
        a = []
        b = []
        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == 0:
                    a.append(i)
                    b.append(j)
        for i in a:
            matrix[i] = [0] * col

        for i in b:
            for j in range(0, row):
                matrix[j][i] = 0

        print(matrix)


mat = [[1,1,1],
       [1,0,1],
       [1,1,1]]
sol = Solution()
sol.setZeroes(mat)
for i in range(0,3):
    print(i)