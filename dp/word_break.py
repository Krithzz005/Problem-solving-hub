"""
Problem: Word Break
Approach: Dp with hash set lookup
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def word_break(s: str, word_dict: list[str]) -> bool:
    """Determine if s can be segmented into space-separated dictionary words."""
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]
