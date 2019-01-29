import copy
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == '' or words == []:
            return []
        lenWord = len(words[0])
        times = {}
        results = []
        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1
        for i in range(len(s) - len(words) * lenWord + 1):  #遍历匹配
            j = 0
            times1 = copy.deepcopy(times)   #字典的深拷贝
            while j < len(words):   #在words中匹配
                print(i, j)
                startWord = i + j * lenWord   #单词开始
                word = s[startWord:startWord+lenWord]
                print(word)
                if word not in times1:   #不匹配
                    break
                times1[word] -= 1
                if times1[word] < 0:
                    break
                if j == len(words) - 1:
                    results.append(i)
                j += 1
        return results
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(Solution().findSubstring(s, words))