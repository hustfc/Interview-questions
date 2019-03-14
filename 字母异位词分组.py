class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if List == []:
            return []
        dic = {}
        for item in strs:
            a = ''.join(sorted(item))
            if a in dic:
                dic[a].append(item)
            else:
                dic[a] = []
                dic[a].append(item)
        results = []
        for word in dic:
            results.append(dic[word])
        return results