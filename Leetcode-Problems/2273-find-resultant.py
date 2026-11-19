from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        for i in range(1,len(words)):
            if(Counter(words[i])!=Counter(res[-1])):
                res.append(words[i])
        return res
