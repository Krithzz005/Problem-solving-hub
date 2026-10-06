"""
Problem: Valid Parentheses
Approach: Stack bracket matching
Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid_parentheses(s: str) -> bool:
    """Validate balanced bracket ordering using a LIFO stack."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
