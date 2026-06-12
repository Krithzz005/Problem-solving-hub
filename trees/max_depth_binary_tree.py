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


if __name__ == '__main__':
    # Quick sanity check for Maximum Depth of Binary Tree
    print('Tested max_depth_binary_tree.py (Maximum Depth of Binary Tree)')
