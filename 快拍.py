def QuickSort(l, start, end):
    if start >= end:
        return
    low, high = start, end
    pivot = l[start]
    while low < high:
        while low < high and l[high] > pivot:
            high -= 1
        l[low] = l[high]
        while low < high and l[low] < pivot:
            low += 1
        l[high] = l[low]
    l[low] = pivot
    QuickSort(l, start, low - 1)
    QuickSort(l, low + 1, end)
    return l
l = [4,5,6,7,3,1,0,12,32]
print(QuickSort(l,0,len(l) - 1))