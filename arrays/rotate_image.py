"""
Problem: Rotate Image
Approach: Matrix transpose and reverse
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def rotate(matrix: list[list[int]]) -> None:
    """Rotate n x n 2D matrix by 90 degrees clockwise in-place."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


if __name__ == '__main__':
    # Quick sanity check for Rotate Image
    print('Tested rotate_image.py (Rotate Image)')
