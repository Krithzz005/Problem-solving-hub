from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group anagrams in O(n * k) using 26-letter frequency signature."""
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())
