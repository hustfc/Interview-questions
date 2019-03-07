class Solution:
    def __init__(self):
        self.results = []
    def Recursion(self, nums, index, target, total, result):
        if index >= len(nums):
            return
        if nums[index] + total == target:
            result.append(nums[index])
            if result not in self.results:
                self.results.append(result)
        elif nums[index] + total < target:
            temp = result[:]
            result.append(nums[index])
            self.Recursion(nums, index + 1, target, total + nums[index], result)
            result = temp[:]
            self.Recursion(nums, index + 1, target, total, result)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        nums = sorted(candidates)
        self.Recursion(nums, 0, target, 0, [])
        return self.results