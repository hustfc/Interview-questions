def MergeSort(nums, start, end):
    if start < end:
        mid = (start + end) >> 1
        MergeSort(nums, start, mid)
        MergeSort(nums, mid + 1, end)
        mergeArray(nums, start, mid, end)
def mergeArray(nums, start, mid, end):
    temp = [0] * (end - start + 1)
    i, j = start, mid + 1
    k = 0
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            i += 1
            k += 1
        else:
            temp[k] = nums[j]
            j += 1
            k += 1
    while i <= mid:
        temp[k] = nums[i]
        i += 1
        k += 1
    while j <= end:
        temp[k] = nums[j]
        j += 1
        k += 1
    nums[start:end+1] = temp
    del temp
nums = [6,2,1,8,9,12,54,13]
MergeSort(nums, 0, len(nums) - 1)
print(nums)