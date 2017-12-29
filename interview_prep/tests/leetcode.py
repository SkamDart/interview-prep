from unittest import TestCase
from pylearn.leetcode import Solution
from pylearn.leetcode import ListNode
import pylearn.linkedlist as ll

class TestLeetCode(TestCase):

    def setUp(self):
        self.s = Solution()

    def test_addTwoNumbers(self):
        one = ListNode(1)
        one.next = ListNode(2)
        one.next.next = ListNode(3)

        two = ListNode(4)
        two.next = ListNode(5)
        two.next.next = ListNode(6)

        self.assertTrue(self.s.addTwoNumbers(one, two))

    def test_romanToInt(self):
        s = self.s.romanToInt
        self.assertTrue(s('I') == 1)
        self.assertTrue(s('II') == 2)
        self.assertTrue(s('III') == 3)
        self.assertTrue(s('IV') == 4)
        self.assertTrue(s("DCXXI") == 621)