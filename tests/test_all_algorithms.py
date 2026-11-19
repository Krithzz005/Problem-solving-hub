import threading
import unittest

from arrays.two_sum import two_sum
from arrays.best_time_to_buy_sell_stock import max_profit
from arrays.contains_duplicate import contains_duplicate
from arrays.product_except_self import product_except_self
from arrays.maximum_subarray import max_sub_array
from arrays.maximum_product_subarray import max_product
from arrays.three_sum import three_sum
from arrays.container_with_most_water import max_area
from arrays.merge_intervals import merge_intervals
from arrays.rotate_image import rotate

from sliding_window.longest_substring_without_repeating import length_of_longest_substring
from sliding_window.minimum_window_substring import min_window
from sliding_window.longest_repeating_character_replacement import character_replacement
from sliding_window.sliding_window_maximum import max_sliding_window

from binary_search.find_min_in_rotated_sorted_array import find_min
from binary_search.search_in_rotated_sorted_array import search_rotated
from binary_search.koko_eating_bananas import min_eating_speed

from linked_list.lru_cache import LRUCache
from trees.implement_trie import Trie

from graphs.number_of_islands import num_islands
from graphs.course_schedule import can_finish
from graphs.dijkstra_shortest_path import network_delay_time
from graphs.union_find_redundant_connection import find_redundant_connection

from dp.climbing_stairs import climb_stairs
from dp.house_robber import rob
from dp.coin_change import coin_change
from dp.longest_increasing_subsequence import length_of_lis
from dp.longest_common_subsequence import longest_common_subsequence
from dp.word_break import word_break
from dp.edit_distance import min_distance

from heaps.top_k_frequent_elements import top_k_frequent
from heaps.find_median_from_data_stream import MedianFinder

from backtracking.subsets import subsets
from backtracking.combination_sum import combination_sum
from backtracking.n_queens import solve_n_queens

from stacks.valid_parentheses import is_valid_parentheses
from stacks.daily_temperatures import daily_temperatures
from stacks.largest_rectangle_in_histogram import largest_rectangle_area

from concurrency.thread_safe_bounded_queue import BoundedBlockingQueue
from concurrency.rate_limiter_token_bucket import TokenBucketRateLimiter

from strings.longest_palindromic_substring import longest_palindrome
from strings.group_anagrams import group_anagrams
from strings.encode_and_decode_strings import encode, decode


class TestDSAAndConcurrency(unittest.TestCase):
    def test_arrays_and_hashing(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_product([2, 3, -2, 4]), 6)
        self.assertEqual(max_product([-2, 3, -4]), 24)
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        m = [[1, 2], [3, 4]]
        rotate(m)
        self.assertEqual(m, [[3, 1], [4, 2]])

    def test_sliding_window_and_binary_search(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        self.assertEqual(length_of_longest_substring(""), 0)
        self.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(character_replacement("AABABBA", 1), 4)
        self.assertEqual(
            max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]
        )
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)

    def test_lru_cache_and_trie(self):
        lru = LRUCache(2)
        lru.put(1, 10)
        lru.put(2, 20)
        self.assertEqual(lru.get(1), 10)
        lru.put(3, 30)  # Evicts key 2
        self.assertEqual(lru.get(2), -1)
        self.assertEqual(lru.get(3), 30)

        trie = Trie()
        trie.insert("kalvium")
        self.assertTrue(trie.search("kalvium"))
        self.assertFalse(trie.search("kalv"))
        self.assertTrue(trie.starts_with("kalv"))

    def test_graphs_and_dp(self):
        grid = [
            ["1", "1", "0", "0"],
            ["1", "0", "0", "1"],
            ["0", "0", "1", "1"],
        ]
        self.assertEqual(num_islands(grid), 2)
        self.assertTrue(can_finish(2, [[1, 0]]))
        self.assertFalse(can_finish(2, [[1, 0], [0, 1]]))
        self.assertEqual(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
        self.assertEqual(
            find_redundant_connection([[1, 2], [1, 3], [2, 3]]), [2, 3]
        )

        self.assertEqual(climb_stairs(5), 8)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(longest_common_subsequence("abcde", "ace"), 3)
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        self.assertEqual(min_distance("horse", "ros"), 3)

    def test_heaps_backtracking_stacks_strings(self):
        self.assertEqual(set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)), {1, 2})
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        self.assertEqual(mf.find_median(), 1.5)
        mf.add_num(3)
        self.assertEqual(mf.find_median(), 2.0)

        self.assertEqual(len(subsets([1, 2, 3])), 8)
        self.assertEqual(combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(len(solve_n_queens(4)), 2)

        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertFalse(is_valid_parentheses("(]"))
        self.assertEqual(
            daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)

        self.assertIn(longest_palindrome("babad"), ("bab", "aba"))
        self.assertEqual(len(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])), 3)
        raw = ["hello", "world#123", "", "kalvium"]
        self.assertEqual(decode(encode(raw)), raw)

    def test_concurrency_primitives_multithreaded(self):
        q = BoundedBlockingQueue(capacity=3)
        consumed = []

        def producer():
            for i in range(10):
                q.enqueue(i)

        def consumer():
            for _ in range(10):
                consumed.append(q.dequeue())

        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join(timeout=5)
        t2.join(timeout=5)
        self.assertEqual(sorted(consumed), list(range(10)))
        self.assertEqual(q.size(), 0)

        limiter = TokenBucketRateLimiter(capacity=2.0, refill_rate_per_sec=10.0)
        self.assertTrue(limiter.allow_request(1.0))
        self.assertTrue(limiter.allow_request(1.0))
        self.assertFalse(limiter.allow_request(1.0))


if __name__ == "__main__":
    unittest.main()
