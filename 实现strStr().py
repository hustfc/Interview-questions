class Solution:
    def strStr(self, haystack, needle):
        if haystack == '' or needle == '':
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and i + len(needle) <= len(haystack):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
haystack = "aaaaaaa"
needle = "bba"
print(Solution().strStr(haystack, needle))