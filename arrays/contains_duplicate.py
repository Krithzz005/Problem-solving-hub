"""
Problem: Contains Duplicate
Approach: Hash set
Time Complexity: O(n)
Space Complexity: O(n)
"""

def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears at least twice."""
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == '__main__':
    # Quick sanity check for Contains Duplicate
    print('Tested contains_duplicate.py (Contains Duplicate)')
