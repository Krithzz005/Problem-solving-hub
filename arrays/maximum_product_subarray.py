def max_product(nums: list[int]) -> int:
    """Track both max and min product ending at current index due to negatives."""
    cur_max = cur_min = ans = nums[0]
    for n in nums[1:]:
        if n < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(n, cur_max * n)
        cur_min = min(n, cur_min * n)
        ans = max(ans, cur_max)
    return ans
