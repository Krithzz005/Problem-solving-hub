"""
Problem: Validate Binary Search Tree
Approach: Range-bounded dfs
Time Complexity: O(n)
Space Complexity: O(h)
"""

def is_valid_bst(root) -> bool:
    """Verify strict BST invariant using (low, high) interval bounds."""
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root, float('-inf'), float('inf'))
