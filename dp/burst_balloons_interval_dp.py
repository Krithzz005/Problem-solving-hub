"""
Problem: Burst Balloons
Approach: Bottom-up interval DP choosing the last balloon to burst in (left, right)
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""


def max_coins(nums: list[int]) -> int:
    arr = [1] + [x for x in nums if x > 0] + [1]
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    arr[left] * arr[k] * arr[right] + dp[left][k] + dp[k][right],
                )
    return dp[0][n - 1]


if __name__ == "__main__":
    assert max_coins([3, 1, 5, 8]) == 167
