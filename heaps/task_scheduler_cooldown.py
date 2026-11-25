"""
Problem: Task Scheduler
Approach: Greedy max-frequency idle-slot calculation
Time Complexity: O(N)
Space Complexity: O(1)
"""

from collections import Counter


def least_interval(tasks: list[str], n: int) -> int:
    """Compute minimum CPU intervals needed to execute all tasks with cooldown n."""
    counts = list(Counter(tasks).values())
    max_freq = max(counts)
    max_count = counts.count(max_freq)
    intervals = (max_freq - 1) * (n + 1) + max_count
    return max(len(tasks), intervals)


if __name__ == "__main__":
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
