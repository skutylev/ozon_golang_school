from typing import List
import unittest


class Solution:
    @staticmethod
    def maxOnesAfterRemoveItem(input_lst: List) -> int:
        current_seq_len = 0
        previous_seq_len = 0
        seq_len_sum_max = 0
        zero_count = 0

        for i in input_lst:

            if i == 1:
                current_seq_len += 1
            else:
                previous_seq_len = current_seq_len
                current_seq_len = 0
                zero_count += 1

            seq_len_sum_current = previous_seq_len + current_seq_len

            if seq_len_sum_current > seq_len_sum_max:
                seq_len_sum_max = seq_len_sum_current
        return len(input_lst) - 1 if zero_count == 0 else seq_len_sum_max


class SolutionTestCase(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxOnesAfterRemoveItem([0, 0]), 0)
        self.assertEqual(solution.maxOnesAfterRemoveItem([0, 1]), 1)
        self.assertEqual(solution.maxOnesAfterRemoveItem([1, 0]), 1)
        self.assertEqual(solution.maxOnesAfterRemoveItem([1, 1]), 1)
        self.assertEqual(solution.maxOnesAfterRemoveItem([1, 1, 0, 1, 1]), 4)
        self.assertEqual(solution.maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 1, 1, 1]), 5)
        self.assertEqual(solution.maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 1, 1, 1, 0]), 5)
        self.assertEqual(solution.maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]), 4)
