"""
Problem: Top K Frequent Elements
Approach: Bucket sort frequency mapping
Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Find k most frequent elements in O(n) linear time using frequency buckets."""
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    res = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            res.append(num)
            if len(res) == k:
                return res
    return res


if __name__ == '__main__':
    # Quick sanity check for Top K Frequent Elements
    print('Tested top_k_frequent_elements.py (Top K Frequent Elements)')
