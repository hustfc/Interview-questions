class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            raise Exception('input error')
        nums.sort()
        threeNums = nums[0] + nums[1] + nums[2]
        differ = abs(threeNums - target)
        ans = threeNums
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            while (low < high):
                threeNums = nums[i] + nums[low] + nums[high]
                if abs(threeNums - target) < differ:
                    differ = abs(threeNums - target)
                    ans = threeNums
                if threeNums == target:
                    return target
                elif threeNums < target:
                    while low < high and nums[low + 1] == nums[low]:
                        low += 1
                    low += 1
                else:
                    while low < high and nums[high - 1] == nums[high]:
                        high -= 1
                    high -= 1
        return ans
nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))
