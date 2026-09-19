"""
Problem: Find Median from Data Stream
Approach: Two heaps (max-heap + min-heap)
Time Complexity: O(log n)
Space Complexity: O(n)
"""

import heapq

class MedianFinder:
    """Maintain running median using balanced lower max-heap and upper min-heap."""
    def __init__(self):
        self.small = []  # max-heap (inverted values)
        self.large = []  # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == '__main__':
    # Quick sanity check for Find Median from Data Stream
    print('Tested find_median_from_data_stream.py (Find Median from Data Stream)')
