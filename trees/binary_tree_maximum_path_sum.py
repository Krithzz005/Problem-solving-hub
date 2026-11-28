"""
Problem: Binary Tree Maximum Path Sum
Approach: Post-order DFS computing max downward gain while updating global split path max
Time Complexity: O(n)
Space Complexity: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode | None) -> int:
    best = float("-inf")

    def dfs(node: TreeNode | None) -> int:
        nonlocal best
        if not node:
            return 0
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)
        best = max(best, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return int(best)


if __name__ == "__main__":
    t = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(t) == 42
