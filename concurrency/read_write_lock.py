"""
Problem: Readers-Writer Lock (Write-Preferring)
Approach: Condition variable synchronization preventing writer starvation
Time Complexity: O(1)
Space Complexity: O(1)
"""

import threading


class ReadWriteLock:
    """Thread-safe write-preferring Readers-Writer lock."""

    def __init__(self):
        self._cond = threading.Condition()
        self._readers = 0
        self._writers_waiting = 0
        self._writer_active = False

    def acquire_read(self) -> None:
        with self._cond:
            while self._writer_active or self._writers_waiting > 0:
                self._cond.wait()
            self._readers += 1

    def release_read(self) -> None:
        with self._cond:
            self._readers -= 1
            if self._readers == 0:
                self._cond.notify_all()

    def acquire_write(self) -> None:
        with self._cond:
            self._writers_waiting += 1
            try:
                while self._writer_active or self._readers > 0:
                    self._cond.wait()
                self._writer_active = True
            finally:
                self._writers_waiting -= 1

    def release_write(self) -> None:
        with self._cond:
            self._writer_active = False
            self._cond.notify_all()


if __name__ == "__main__":
    rw = ReadWriteLock()
    rw.acquire_read()
    rw.release_read()
    rw.acquire_write()
    rw.release_write()
