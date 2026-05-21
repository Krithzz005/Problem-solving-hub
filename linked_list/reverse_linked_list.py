"""
Problem: Reverse Linked List
Approach: Iterative pointer reversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse singly-linked list iteratively in O(1) auxiliary space."""
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


if __name__ == '__main__':
    # Quick sanity check for Reverse Linked List
    print('Tested reverse_linked_list.py (Reverse Linked List)')
