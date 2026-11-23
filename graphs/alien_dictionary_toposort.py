"""
Problem: Alien Dictionary
Approach: Character precedence graph + Kahn's BFS topological sort
Time Complexity: O(C) where C is total characters across all words
Space Complexity: O(1) for fixed alphabet
"""

from collections import deque


def alien_order(words: list[str]) -> str:
    adj = {ch: set() for w in words for ch in w}
    indegree = {ch: 0 for ch in adj}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    q = deque([c for c, d in indegree.items() if d == 0])
    order = []
    while q:
        curr = q.popleft()
        order.append(curr)
        for nxt in adj[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return "".join(order) if len(order) == len(indegree) else ""


if __name__ == "__main__":
    assert alien_order(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
