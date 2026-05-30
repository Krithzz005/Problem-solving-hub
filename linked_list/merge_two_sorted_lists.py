"""
Problem: Merge Two Sorted Lists
Approach: Dummy head iterative merge
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Splice together nodes of two sorted linked lists."""
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


if __name__ == '__main__':
    # Quick sanity check for Merge Two Sorted Lists
    print('Tested merge_two_sorted_lists.py (Merge Two Sorted Lists)')
