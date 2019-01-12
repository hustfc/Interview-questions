class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def BackTrace(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                BackTrace(s + '(', left + 1, right)
            if right < left:
                BackTrace(s + ')', left, right + 1)
        BackTrace()
        return result
print(Solution().generateParenthesis(3))