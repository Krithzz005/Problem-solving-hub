"""
Problem: Longest Substring Without Repeating Characters
Approach: Sliding window + index map
Time Complexity: O(n)
Space Complexity: O(min(m, n))
"""

def length_of_longest_substring(s: str) -> int:
    """Find longest substring without duplicate characters using sliding window."""
    last_seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == '__main__':
    # Quick sanity check for Longest Substring Without Repeating Characters
    print('Tested longest_substring_without_repeating.py (Longest Substring Without Repeating Characters)')
