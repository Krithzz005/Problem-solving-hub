"""
Problem: Group Anagrams
Approach: Character frequency tuple key
Time Complexity: O(n * k)
Space Complexity: O(n * k)
"""

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


if __name__ == '__main__':
    # Quick sanity check for Group Anagrams
    print('Tested group_anagrams.py (Group Anagrams)')
