def max_depth(root) -> int:
    """Compute height of binary tree recursively."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
