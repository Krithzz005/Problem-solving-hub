"""
Problem: Longest Increasing Subsequence
Approach: Patience sorting + binary search
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import bisect

def length_of_lis(nums: list[int]) -> int:
    """Compute LIS length in O(n log n) time using tails array."""
    tails = []
    for x in nums:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)


if __name__ == '__main__':
    # Quick sanity check for Longest Increasing Subsequence
    print('Tested longest_increasing_subsequence.py (Longest Increasing Subsequence)')
