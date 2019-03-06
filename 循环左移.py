class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        l = list(s)
        left = list(reversed(l[0:n]))
        right = l[len(l)-1:n-1:-1]
        return ''.join((left + right)[::-1])
import sys
try:
    while True:
        line1 = sys.stdin.readline().strip()
        if line1 == '':
            break
        s = line1
        line2 = sys.stdin.readline().strip()
        n = int(line2)
        print(Solution().LeftRotateString(s, n))
except:
    pass