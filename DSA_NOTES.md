# Problem Solving & Algorithm Notes

Implementations of data structures, algorithms, and concurrency patterns with time/space complexity analysis.

## Solved Problems

- **Two Sum** (`arrays/two_sum.py`): hash map lookup — Time `O(n)`, Space `O(n)`
- **Best Time to Buy and Sell Stock** (`arrays/best_time_to_buy_sell_stock.py`): single pass min tracking — Time `O(n)`, Space `O(1)`
- **Contains Duplicate** (`arrays/contains_duplicate.py`): hash set — Time `O(n)`, Space `O(n)`
- **Product of Array Except Self** (`arrays/product_except_self.py`): prefix and suffix products — Time `O(n)`, Space `O(1)`
- **Maximum Subarray** (`arrays/maximum_subarray.py`): Kadane's algorithm — Time `O(n)`, Space `O(1)`
- **Maximum Product Subarray** (`arrays/maximum_product_subarray.py`): dynamic min/max tracking — Time `O(n)`, Space `O(1)`
- **3Sum** (`arrays/three_sum.py`): sorting + two pointers — Time `O(n^2)`, Space `O(1)`
- **Container With Most Water** (`arrays/container_with_most_water.py`): greedy two pointers — Time `O(n)`, Space `O(1)`
- **Merge Intervals** (`arrays/merge_intervals.py`): interval sorting — Time `O(n log n)`, Space `O(n)`
- **Rotate Image** (`arrays/rotate_image.py`): matrix transpose and reverse — Time `O(n^2)`, Space `O(1)`
- **Longest Substring Without Repeating Characters** (`sliding_window/longest_substring_without_repeating.py`): sliding window + index map — Time `O(n)`, Space `O(min(m, n))`
- **Minimum Window Substring** (`sliding_window/minimum_window_substring.py`): two pointers + frequency map — Time `O(n)`, Space `O(k)`
- **Longest Repeating Character Replacement** (`sliding_window/longest_repeating_character_replacement.py`): sliding window max freq — Time `O(n)`, Space `O(1)`
- **Sliding Window Maximum** (`sliding_window/sliding_window_maximum.py`): monotonic decreasing deque — Time `O(n)`, Space `O(k)`
- **Find Minimum in Rotated Sorted Array** (`binary_search/find_min_in_rotated_sorted_array.py`): modified binary search — Time `O(log n)`, Space `O(1)`
- **Search in Rotated Sorted Array** (`binary_search/search_in_rotated_sorted_array.py`): one-pass binary search — Time `O(log n)`, Space `O(1)`
- **Koko Eating Bananas** (`binary_search/koko_eating_bananas.py`): binary search on answer space — Time `O(n log M)`, Space `O(1)`
- **Reverse Linked List** (`linked_list/reverse_linked_list.py`): iterative pointer reversal — Time `O(n)`, Space `O(1)`
- **Linked List Cycle** (`linked_list/linked_list_cycle.py`): Floyd's tortoise and hare — Time `O(n)`, Space `O(1)`
- **Merge Two Sorted Lists** (`linked_list/merge_two_sorted_lists.py`): dummy head iterative merge — Time `O(n + m)`, Space `O(1)`
- **LRU Cache** (`linked_list/lru_cache.py`): hash map + doubly linked list — Time `O(1)`, Space `O(capacity)`
- **Invert Binary Tree** (`trees/invert_binary_tree.py`): recursive DFS swap — Time `O(n)`, Space `O(h)`
- **Maximum Depth of Binary Tree** (`trees/max_depth_binary_tree.py`): bottom-up recursion — Time `O(n)`, Space `O(h)`
- **Validate Binary Search Tree** (`trees/validate_bst.py`): range-bounded DFS — Time `O(n)`, Space `O(h)`
- **Lowest Common Ancestor of a Binary Tree** (`trees/lowest_common_ancestor.py`): post-order traversal — Time `O(n)`, Space `O(h)`
- **Binary Tree Level Order Traversal** (`trees/binary_tree_level_order.py`): BFS queue — Time `O(n)`, Space `O(n)`
- **Implement Trie (Prefix Tree)** (`trees/implement_trie.py`): nested dictionary nodes — Time `O(L)`, Space `O(N * L)`
- **Number of Islands** (`graphs/number_of_islands.py`): grid DFS flood fill — Time `O(R * C)`, Space `O(R * C)`
- **Course Schedule** (`graphs/course_schedule.py`): Kahn's topological sort (BFS) — Time `O(V + E)`, Space `O(V + E)`
- **Clone Graph** (`graphs/clone_graph.py`): DFS with hash map memoization — Time `O(V + E)`, Space `O(V)`
- **Network Delay Time (Dijkstra)** (`graphs/dijkstra_shortest_path.py`): min-heap priority queue — Time `O(E log V)`, Space `O(V + E)`
- **Redundant Connection** (`graphs/union_find_redundant_connection.py`): Disjoint Set Union (path compression + rank) — Time `O(n alpha(n))`, Space `O(n)`
