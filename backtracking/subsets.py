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
