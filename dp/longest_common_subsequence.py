"""
Problem: Longest Common Subsequence
Approach: Space-optimized 2d dp
Time Complexity: O(m * n)
Space Complexity: O(min(m, n))
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    """Compute LCS between two strings using two rolling rows."""
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    prev = [0] * (len(text2) + 1)
    for ch1 in text1:
        curr = [0] * (len(text2) + 1)
        for j, ch2 in enumerate(text2, 1):
            if ch1 == ch2:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[-1]


if __name__ == '__main__':
    # Quick sanity check for Longest Common Subsequence
    print('Tested longest_common_subsequence.py (Longest Common Subsequence)')
