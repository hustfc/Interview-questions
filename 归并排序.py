def MergeSort(nums, start, end, temp):
    if start < end:
        mid = (start + end) >> 1
        MergeSort(nums, start, mid, temp)
        MergeSort(nums, mid + 1, end, temp)
        mergeArray(nums, start, mid, end, temp)
        del temp
def mergeArray(nums, start, mid, end, temp):
    i, j, k = start, mid + 1, start
    while i <= mid and j <= end:
        if nums[i] >= nums[j]:
            temp[k] = nums[j]
            k += 1
            j += 1
        else:
            temp[k] = nums[i]
            k += 1
            i += 1
    while i <= mid:
        temp[k] = nums[i]
        k += 1
        i += 1
    while j <= end:
        temp[k] = nums[j]
        k += 1
        j += 1
    nums[start:end+1] = temp[start:end+1]
    ####重要步骤，nums一定要等于temp
nums = [5,4,3,2,7,8,9,1,2,43,21]
temp = [0] * len(nums)
MergeSort(nums, 0, len(nums) - 1, temp)
print(nums)