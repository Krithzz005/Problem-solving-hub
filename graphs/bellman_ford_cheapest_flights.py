"""
Problem: Cheapest Flights Within K Stops
Approach: Bellman-Ford bounded relaxation over at most K + 1 edges
Time Complexity: O(K * E)
Space Complexity: O(V)
"""


def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    """Find cheapest flight cost from src to dst with at most k stops."""
    prices = [float("inf")] * n
    prices[src] = 0
    for _ in range(k + 1):
        tmp = prices.copy()
        for u, v, w in flights:
            if prices[u] != float("inf") and prices[u] + w < tmp[v]:
                tmp[v] = prices[u] + w
        prices = tmp
    return -1 if prices[dst] == float("inf") else int(prices[dst])


if __name__ == "__main__":
    assert find_cheapest_price(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700
