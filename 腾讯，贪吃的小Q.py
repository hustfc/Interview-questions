n, m = map(int, input().split())
max = m - (n - 1)  #第一天吃最多巧克力的个数
def EatNum(firstNum):
    sum = 0
    for i in range(n):
        sum += firstNum
        j = int(firstNum >> 1)
        while j << 1 < firstNum:    #不少于前一天的一半，并且需要是整数
            j += 1
        firstNum = j
        if firstNum < 1:
            firstNum = 1
    #eatNum[firstNum] = sum
    return sum
def MaxEat():
    low, high = 0, max
    while low <= high:
        mid = (low + high) >> 1
        if EatNum(mid) <= m and EatNum(mid + 1) > m:
            return mid
        if EatNum(mid) <= m:
            low  = mid + 1
        else:
            high = mid - 1
print(MaxEat())