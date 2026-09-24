def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Find all unique combinations where candidate numbers sum to target."""
    candidates.sort()
    res = []

    def dfs(start: int, rem: int, path: list[int]):
        if rem == 0:
            res.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if candidates[i] > rem:
                break
            path.append(candidates[i])
            dfs(i, rem - candidates[i], path)
            path.pop()

    dfs(0, target, [])
    return res
