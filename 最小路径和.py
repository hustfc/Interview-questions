class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == []:
            return 0
        rows, cols = len(grid), len(grid[0])
        memory = [([0] * cols) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i - 1 >= 0 and j - 1 >= 0:
                    memory[i][j] = min(memory[i - 1][j], memory[i][j - 1]) + grid[i][j]
                elif i - 1 >= 0:
                    memory[i][j] = memory[i - 1][j] + grid[i][j]
                elif j - 1 >= 0:
                    memory[i][j] = memory[i][j - 1] + grid[i][j]
                else:
                    memory[i][j] = grid[i][j]
        return memory[rows - 1][cols - 1]