def two_sum(nums: list[int], target: int) -> list[int]:
    """Find indices of two numbers such that they add up to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
