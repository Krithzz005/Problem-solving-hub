def rob(nums: list[int]) -> int:
    """Maximize loot without robbing two adjacent houses."""
    rob1, rob2 = 0, 0
    for n in nums:
        rob1, rob2 = rob2, max(rob1 + n, rob2)
    return rob2
