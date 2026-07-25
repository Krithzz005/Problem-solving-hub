def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    """Use Union-Find with path compression to find cycle-creating edge."""
    parent = list(range(len(edges) + 1))
    rank = [1] * (len(edges) + 1)

    def find(i: int) -> int:
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(a: int, b: int) -> bool:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] > rank[rb]:
            parent[rb] = ra
        elif rank[ra] < rank[rb]:
            parent[ra] = rb
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]
    return []
