"""
Problem: Subsets
Approach: Backtracking decision tree
Time Complexity: O(n * 2^n)
Space Complexity: O(n)
"""

def subsets(nums: list[int]) -> list[list[int]]:
    """Generate power set of all possible subsets."""
    res = []
    path = []

    def backtrack(idx: int):
        if idx == len(nums):
            res.append(path.copy())
            return
        path.append(nums[idx])
        backtrack(idx + 1)
        path.pop()
        backtrack(idx + 1)

    backtrack(0)
    return res


if __name__ == '__main__':
    # Quick sanity check for Subsets
    print('Tested subsets.py (Subsets)')
