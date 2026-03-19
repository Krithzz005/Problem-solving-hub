"""
Problem: Maximum Subarray
Approach: Kadane's algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_sub_array(nums: list[int]) -> int:
    """Find contiguous subarray with the largest sum using Kadane's algorithm."""
    cur_sum = max_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum
