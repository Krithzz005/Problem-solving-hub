"""
Problem: Subarray Sum Equals K
Approach: Prefix sum frequency hash map
Time Complexity: O(n)
Space Complexity: O(n)
"""


def subarray_sum(nums: list[int], k: int) -> int:
    """Return total number of continuous subarrays whose sum equals k."""
    counts = {0: 1}
    prefix = 0
    total = 0
    for n in nums:
        prefix += n
        total += counts.get(prefix - k, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return total


if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
