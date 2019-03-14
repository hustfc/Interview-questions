class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '' or num2 == '':
            return ''
        n1, n2 = len(num1), len(num2)
        k = n1 + n2 - 2
        temp = [0] * (n1 + n2)
        for i in range(n1):
            for j in range(n2):
                temp[k - i - j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        carry = 0
        for i in range(n1 + n2):
            temp[i] += carry
            carry = temp[i] // 10
            temp[i] = temp[i] % 10
        i = n1 + n2 - 1
        while temp[i] == 0:
            i -= 1
        string = ''
        while i >= 0:
            string += str(temp[i])
            i -= 1
        return string

num1, num2 = '123', '456'
print(Solution().multiply(num1, num2))