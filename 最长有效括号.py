class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        flag = [0] * len(s)
        stack = []
        stackIndex = []
        for index, item in enumerate(s):
            if item == '(':
                stack.append(item)
                stackIndex.append(index)
            if item == ')':
                if len(stack) >= 1 and stack.pop() == '(':
                    flag[index], flag[stackIndex.pop()] = 1, 1
                else:
                    stack.append(item)
        maxLen, start = 0, 0
        while start < len(flag):
            while start < len(flag) and flag[start] == 0:
                start += 1
            end = start
            while end < len(flag) and flag[end] == 1:
                end += 1
            maxLen = max(maxLen, end - start)
            start = end + 1
        return maxLen
s = '()(())'
print(Solution().longestValidParentheses(s))
