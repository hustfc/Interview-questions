n, m = map(int, input().split())
max = m - (n - 1)  #第一天吃巧克力最多
def EatNum(firstNum):
    sum = 0
    for i in range(n):
        sum