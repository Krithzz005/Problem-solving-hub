"""
Problem: Token Bucket Rate Limiter
Approach: Thread-safe token replenishment
Time Complexity: O(1)
Space Complexity: O(1)
"""

import time
import threading

class TokenBucketRateLimiter:
    """Thread-safe Token Bucket algorithm for API rate limiting."""
    def __init__(self, capacity: float, refill_rate_per_sec: float):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate_per_sec
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def allow_request(self, tokens_needed: float = 1.0) -> bool:
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.last_refill
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_refill = now
            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            return False
