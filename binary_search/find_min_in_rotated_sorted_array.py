"""
Problem: Find Minimum in Rotated Sorted Array
Approach: Modified binary search
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def find_min(nums: list[int]) -> int:
    """Locate inflection point in rotated sorted array."""
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]
