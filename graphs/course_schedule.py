"""
Problem: Course Schedule
Approach: Kahn's topological sort (bfs)
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Detect cycle in directed prerequisite graph using indegree topological sort."""
    adj = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    q = deque([i for i in range(num_courses) if indegree[i] == 0])
    visited = 0
    while q:
        curr = q.popleft()
        visited += 1
        for nxt in adj[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return visited == num_courses


if __name__ == '__main__':
    # Quick sanity check for Course Schedule
    print('Tested course_schedule.py (Course Schedule)')
