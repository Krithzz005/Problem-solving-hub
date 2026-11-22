"""
Problem: Target Sum
Approach: Subset-sum 1D dynamic programming reduction (P = (total + target) / 2)
Time Complexity: O(n * S)
Space Complexity: O(S)
"""


def find_target_sum_ways(nums: list[int], target: int) -> int:
    """Count ways to assign + and - signs so elements sum to target."""
    total = sum(nums)
    if abs(target) > total or (total + target) % 2 != 0:
        return 0
    pos_sum = (total + target) // 2
    dp = [0] * (pos_sum + 1)
    dp[0] = 1
    for n in nums:
        for s in range(pos_sum, n - 1, -1):
            dp[s] += dp[s - n]
    return dp[pos_sum]


if __name__ == "__main__":
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5
