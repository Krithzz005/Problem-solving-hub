"""
Problem: Implement Trie (Prefix Tree)
Approach: Nested dictionary nodes
Time Complexity: O(L)
Space Complexity: O(N * L)
"""

class Trie:
    """Prefix tree supporting insert, exact search, and prefix matching."""
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return bool(node and "#" in node)

    def starts_with(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node


if __name__ == '__main__':
    # Quick sanity check for Implement Trie (Prefix Tree)
    print('Tested implement_trie.py (Implement Trie (Prefix Tree))')
