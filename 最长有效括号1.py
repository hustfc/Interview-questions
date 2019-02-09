class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        stack = []
        maxLen, start = 0, 0
        for index, item in enumerate(s):
            if item == '(':
                stack.append(index)
            if item == ')':
                if len(stack) == 0:
                    start = index + 1
                else:
                    stack.pop()
                    maxLen = max(maxLen, index - start + 1) \
                        if len(stack) == 0 else max(maxLen, index - stack[len(stack) - 1])
        return maxLen
s = "()(()"
s = "()(())"
print(Solution().longestValidParentheses(s))
