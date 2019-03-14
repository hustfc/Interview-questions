class Solution:
    def matrixRotation(self, matrix):
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().matrixRotation(matrix)
for item in matrix:
    print(item)