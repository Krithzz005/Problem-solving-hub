"""
Problem: Number of Islands
Approach: Grid dfs flood fill
Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""

def num_islands(grid: list[list[str]]) -> int:
    """Count connected components of '1's in 2D grid."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count


if __name__ == '__main__':
    # Quick sanity check for Number of Islands
    print('Tested number_of_islands.py (Number of Islands)')
