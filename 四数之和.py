class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for i in range(len(nums) - 3):
            j = i + 1
            while j <= len(nums) - 3:
                if nums[j] == nums[i]:
                    j += 1
                low, high = j + 1, len(nums) - 1
                while low < high:
                    fourSum = nums[i] + nums[j] + nums[low] + nums[high]
                    if fourSum == target:
                        result = [nums[i], nums[j], nums[low], nums[high]]
                        #result.sort()
                        if result not in results:
                            results.append(result)
                        while low < high and nums[low + 1] == nums[low]:
                            low += 1
                        low += 1
                        while low < high and nums[high - 1] == nums[high]:
                            high -= 1
                        high -= 1
                    elif fourSum < target:
                        while low < high and nums[low + 1] == nums[low]:
                            low += 1
                        low += 1
                    else:
                        while low < high and nums[high - 1] == nums[high]:
                            high -= 1
                        high -= 1
                j += 1
        return results
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))