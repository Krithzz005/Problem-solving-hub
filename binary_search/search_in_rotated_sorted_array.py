"""
Problem: Search in Rotated Sorted Array
Approach: One-pass binary search
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search_rotated(nums: list[int], target: int) -> int:
    """Search target in rotated sorted array in O(log n) time."""
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
