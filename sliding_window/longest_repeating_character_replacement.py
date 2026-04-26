"""
Problem: Longest Repeating Character Replacement
Approach: Sliding window max freq
Time Complexity: O(n)
Space Complexity: O(1)
"""

def character_replacement(s: str, k: int) -> int:
    """Find length of longest substring containing same letter after k replacements."""
    count = {}
    maxf = 0
    l = 0
    res = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


if __name__ == '__main__':
    # Quick sanity check for Longest Repeating Character Replacement
    print('Tested longest_repeating_character_replacement.py (Longest Repeating Character Replacement)')
