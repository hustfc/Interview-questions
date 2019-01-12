class Solution:
    def Reverse(self, c):
        if c == ')':
            print(1)
            return '('
        elif c == '}':
            print(2)
            return '{'
        elif c == ']':
            print(3)
            return '['
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False
        stack = []
        for i in range(len(s)):
            #print(s[i],stack)
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                popC = stack.pop()
                print(popC)
                re = self.Reverse(popC)
                print(popC, re)
                if s[i] != re:
                    return False
        return True
s = '()'
print(Solution().isValid(s))