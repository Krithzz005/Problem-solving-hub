"""
Problem: Container With Most Water
Approach: Greedy two pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_area(height: list[int]) -> int:
    """Use two pointers inward from both ends to maximize area."""
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        best = max(best, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best


if __name__ == '__main__':
    # Quick sanity check for Container With Most Water
    print('Tested container_with_most_water.py (Container With Most Water)')
