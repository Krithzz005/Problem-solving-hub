from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=Counter(s)
        for i,char in enumerate(s):
            if(n[char]==1):
                return i
        return -1
