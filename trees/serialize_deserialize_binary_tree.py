"""
Problem: Serialize and Deserialize Binary Tree
Approach: Preorder DFS traversal with null sentinel markers
Time Complexity: O(n)
Space Complexity: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        vals = []

        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> TreeNode | None:
        it = iter(data.split(","))

        def dfs():
            val = next(it)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


if __name__ == "__main__":
    codec = Codec()
    sample = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    encoded = codec.serialize(sample)
    assert codec.serialize(codec.deserialize(encoded)) == encoded
