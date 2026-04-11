"""
Problem: Merge Intervals
Approach: Interval sorting
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge all overlapping intervals after sorting by start time."""
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == '__main__':
    # Quick sanity check for Merge Intervals
    print('Tested merge_intervals.py (Merge Intervals)')
