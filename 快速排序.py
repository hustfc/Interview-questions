def QuickSort(nums, start, end):
    if start > end:
        return
    low, high = start, end
    pivot = nums[low]
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] <= pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    QuickSort(nums, start, low - 1)
    QuickSort(nums, low + 1, end)
    return nums
nums = [1,6,5,3,2,11,43,65,9,7,2]
print(QuickSort(nums, 0, len(nums) - 1))