def invert_tree(root):
    """Mirror a binary tree by recursively swapping left and right children."""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
