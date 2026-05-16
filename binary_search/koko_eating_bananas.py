"""
Problem: Koko Eating Bananas
Approach: Binary search on answer space
Time Complexity: O(n log M)
Space Complexity: O(1)
"""

import math

def min_eating_speed(piles: list[int], h: int) -> int:
    """Binary search the minimum workable eating speed k."""
    l, r = 1, max(piles)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


if __name__ == '__main__':
    # Quick sanity check for Koko Eating Bananas
    print('Tested koko_eating_bananas.py (Koko Eating Bananas)')
