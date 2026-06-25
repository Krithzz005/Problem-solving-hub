"""
Problem: Binary Tree Level Order Traversal
Approach: Bfs queue
Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque

def level_order(root) -> list[list[int]]:
    """Return level-by-level node values using breadth-first search."""
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
