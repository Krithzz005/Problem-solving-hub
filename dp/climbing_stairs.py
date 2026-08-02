"""
Problem: Climbing Stairs
Approach: Space-optimized bottom-up dp
Time Complexity: O(n)
Space Complexity: O(1)
"""

def climb_stairs(n: int) -> int:
    """Calculate distinct ways to climb to the top using Fibonacci state transition."""
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
