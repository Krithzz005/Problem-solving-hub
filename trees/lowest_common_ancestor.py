"""
Problem: Lowest Common Ancestor of a Binary Tree
Approach: Post-order traversal
Time Complexity: O(n)
Space Complexity: O(h)
"""

def lowest_common_ancestor(root, p, q):
    """Find LCA of two nodes in a binary tree."""
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right
