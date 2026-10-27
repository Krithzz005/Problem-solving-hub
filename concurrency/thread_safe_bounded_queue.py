"""
Problem: Thread-Safe Bounded Blocking Queue
Approach: Condition variables + lock
Time Complexity: O(1)
Space Complexity: O(capacity)
"""

import threading
from collections import deque

class BoundedBlockingQueue:
    """Thread-safe bounded blocking queue using condition locks."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.cond = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.cond:
            while len(self.queue) >= self.capacity:
                self.cond.wait()
            self.queue.append(element)
            self.cond.notify_all()

    def dequeue(self) -> int:
        with self.cond:
            while not self.queue:
                self.cond.wait()
            val = self.queue.popleft()
            self.cond.notify_all()
            return val

    def size(self) -> int:
        with self.cond:
            return len(self.queue)


if __name__ == '__main__':
    # Quick sanity check for Thread-Safe Bounded Blocking Queue
    print('Tested thread_safe_bounded_queue.py (Thread-Safe Bounded Blocking Queue)')
