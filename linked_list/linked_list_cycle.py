"""
Problem: Linked List Cycle
Approach: Floyd's tortoise and hare
Time Complexity: O(n)
Space Complexity: O(1)
"""

def has_cycle(head) -> bool:
    """Detect cycle in linked list using fast and slow pointers."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
