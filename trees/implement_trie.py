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
