class Solution:
    def numberEqualSubscript(self, numbers):
        if numbers == []:
            return -1
        low, high = 0, len(numbers) - 1
        while low <= high:
            middle = (low + high) >> 1
            if numbers[middle] == middle:
                return middle
            elif numbers[middle] < middle:
                low = middle + 1
            else:
                high = middle - 1
        return - 1
numbers = [-3,-1,1,3,5]
print(Solution().numberEqualSubscript(numbers))
cols, rows = 3, 4
matrix = [([0] * cols) for i in range(rows)]
print(matrix)