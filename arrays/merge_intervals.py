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
