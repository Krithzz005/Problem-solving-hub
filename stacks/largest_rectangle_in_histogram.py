"""
Problem: Largest Rectangle in Histogram
Approach: Monotonic increasing stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

def largest_rectangle_area(heights: list[int]) -> int:
    """Find largest rectangular area in histogram in O(n) single pass."""
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    return max_area
