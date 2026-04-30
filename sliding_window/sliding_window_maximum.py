"""
Problem: Sliding Window Maximum
Approach: Monotonic decreasing deque
Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Maintain monotonic decreasing deque of indices for O(n) window max."""
    dq = deque()
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
