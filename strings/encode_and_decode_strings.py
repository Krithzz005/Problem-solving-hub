"""
Problem: Encode and Decode Strings
Approach: Length-prefixed framing
Time Complexity: O(n)
Space Complexity: O(n)
"""

def encode(strs: list[str]) -> str:
    """Serialize list of strings using length-prefix delimiter framing."""
    return "".join(f"{len(s)}#{s}" for s in strs)

def decode(s: str) -> list[str]:
    """Deserialize length-prefixed string back into list of strings."""
    res, i = [], 0
    while i < len(s):
        j = s.find("#", i)
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res
