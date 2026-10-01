"""
Problem: N-Queens
Approach: Backtracking with bitmask/set constraints
Time Complexity: O(N!)
Space Complexity: O(N^2)
"""

def solve_n_queens(n: int) -> list[list[str]]:
    """Place N queens on an N x N chessboard so no two queens attack each other."""
    cols = set()
    pos_diag = set()
    neg_diag = set()
    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r: int):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res
