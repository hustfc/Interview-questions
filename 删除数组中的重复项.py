class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        i, j = 1, 2
        num = nums[1]
        while j < len(nums):
            if nums[j] != num:
                num = nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i
nums = [1,2,3]
print(Solution().removeDuplicates(nums))
print(nums)