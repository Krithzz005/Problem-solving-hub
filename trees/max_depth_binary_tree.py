"""
Problem: Maximum Depth of Binary Tree
Approach: Bottom-up recursion
Time Complexity: O(n)
Space Complexity: O(h)
"""

def max_depth(root) -> int:
    """Compute height of binary tree recursively."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
