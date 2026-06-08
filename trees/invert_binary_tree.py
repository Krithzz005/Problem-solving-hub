"""
Problem: Invert Binary Tree
Approach: Recursive dfs swap
Time Complexity: O(n)
Space Complexity: O(h)
"""

def invert_tree(root):
    """Mirror a binary tree by recursively swapping left and right children."""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == '__main__':
    # Quick sanity check for Invert Binary Tree
    print('Tested invert_binary_tree.py (Invert Binary Tree)')
