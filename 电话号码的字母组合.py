class Solution:
    def getA(self, x):
        x = int(x)
        if x == 1:
            return
        elif x >= 2 and x <= 6:
            return [chr(ord('a') + (x - 2) * 3), chr(ord('a') + (x - 2) * 3 + 1), chr(ord('a') + (x - 2) * 3 + 2)]
        elif x == 7:
            return ['p', 'q', 'r', 's']
        elif x == 8:
            return ['t', 'u', 'v']
        elif x == 9:
            return ['w', 'x', 'y', 'z']

    def recursionComb(self, digitsList):
        if len(digitsList) == 1:
            return self.getA(digitsList[0])
        ans = []
        addAns = self.getA(digitsList.pop())  # 最后一个元素
        preAns = self.recursionComb(digitsList)  # 之前的所有元素
        for i in preAns:
            for j in addAns:
                ans.append(i + j)
        return ans

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]t
        """
        if digits == '':
            return []
        digitsList = list(digits)
        return self.recursionComb(digitsList)
