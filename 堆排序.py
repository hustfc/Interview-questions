#建立最大堆，始终保持nums[i] > nums[2i+1] and nums[i] > nums[2i+2]
def heapify(nums, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and nums[l] > nums[largest]:
        largest = l
    if r < n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def heapSort(nums):
    i = len(nums) // 2
    #建立堆，使得nums[i] > nums[2i+1] and nums[i] > nums[2i+2]
    while i >= 0:
        heapify(nums, len(nums), i)
        i -= 1
    for i in range(len(nums) - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        #最大的换到末尾，然后对换到0的数字继续构造堆，这个时候末尾的元素就不考虑了
        heapify(nums, i, 0)
nums = [5,6,4,1,8]
heapSort(nums)
print(nums)