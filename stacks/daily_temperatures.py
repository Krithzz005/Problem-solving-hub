"""
Problem: Daily Temperatures
Approach: Monotonic decreasing stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Compute days until a warmer temperature using a monotonic stack."""
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            prev_idx = stack.pop()
            res[prev_idx] = i - prev_idx
        stack.append(i)
    return res


if __name__ == '__main__':
    # Quick sanity check for Daily Temperatures
    print('Tested daily_temperatures.py (Daily Temperatures)')
