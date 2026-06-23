from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        tot=Counter(chars)
        tot_len=0
        for w in words:
            word=Counter(w)
            if not word-tot:
                tot_len+=len(w)
        return tot_len            
