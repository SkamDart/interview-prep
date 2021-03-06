import sys
from operator import mul, add, sub, truediv
from collections import deque

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("")

class Solution:
    def maxPoints(self, points):
        """
        https://leetcode.com/problems/max-points-on-a-line/description/
        :type points: List[Point]
        :rtype: interview
        """
        if len(points) <= 2:
            return len(points)

        from collections import defaultdict
        N = len(points)
        slope_count = defaultdict(int)
        max_points = 0

        for i in range(N):
            
            slope_count.clear()
            cur_max = 0
            duplicates = 0
            base_pt = points[i]
            x0, y0 = base_pt

            for j in range(i + 1, N):
                next_pt = points[j]
                if next_pt == base_pt:
                    duplicates += 1
                else:
                    x, y = next_pt
                    slope = None if x - x0 == 0 else (y - y0) / (x - x0)
                    slope_count[slope] += 1

            max_points = max(max_points, max(slope_count, key=lambda x: x[1]), duplicates)
        
        return max_points
    
    def is_valid_time(self, time):
        return True
        lhs, rhs = time.split(":")
        if int(lhs) > 23 or int(rhs) > 59:
            return False
        return True

    def nextClosestTime(self, time):
        """
        https://leetcode.com/explore/interview/card/google/67/sql-2/471/
        :type time: str
        :rtype: str
        """
       # from itertools import combinations_with_replacement
        from itertools import permutations
        # get all numbers
        nums = list(map(str, filter(lambda x: x != ':', list(time))))
        # list of 4! permutations
        # filter list
        # calculate closest "time" difference
        closest_time = None
        for time in permutations(nums):
            if self.is_valid_time(time):
                time.insert()
                print(time)
        return closest_time

    def climbStairs(self, n):
        """
        https://leetcode.com/problems/climbing-stairs/description/
        :type n: int
        :rtype: int
        0 -> 0
        1 -> 1 (1 step)
        2 -> 2 (1 + 1 step or 2 step)
        3 -> 3 (1 + 1 + 1 step, 1 + 2 step, or 2 + 1 step)
        
        4 ->   (1 + 1 + 1 + 1   step 
                2 + 1 + 1       step
                1 + 2 + 1       step
                1 + 1 + 2       step
                2 + 2           step)

        5 -> 4 + 1
             1 + 4
             1 + 1 + 1 + 1 + 1
        """
        if n < 3:
            return n
        N = n + 1
        steps = [0 for i in range(N)]
        steps[1] = 1
        steps[2] = 2
        for i in range(3, N):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]

    def lengthOfLIS(self, nums):
        """
        https://leetcode.com/problems/longest-increasing-subsequence/description/
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        nums.insert(0, -sys.maxsize)
        n = len(nums)
        LIS = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            LIS[i] = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i] and 1 + LIS[j] > LIS[i]:
                    LIS[i] = 1 + LIS[j]
        return LIS[0] - 1

    def isSameTree(self, p, q):
        """
        https://leetcode.com/problems/same-tree/description/
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def mergeTrees(self, t1, t2):
        """
        https://leetcode.com/problems/merge-two-binary-trees/description/
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root_val = (t1.val if t1 else 0) + (t2.val if t2 else 0)
            root = TreeNode(root_val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right , t2.right)
            return root
        return t1 or t2

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pass

    def removeElement(self, nums, val):
        """
        https://leetcode.com/problems/remove-element/description/
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        not_dupes = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[not_dupes] = nums[i]
                not_dupes += 1
        return not_dupes

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.find_path(root, p, [])
        q_path = self.find_path(root, q, [])
        last_same = root

        node_idx_map = {}
        for i, node in enumerate(p_path):
            node_idx_map[repr(node)] == i

        return last_same

    def find_path(self, root, p, path):
        if root == p:
            return path

        if root.left == None and root.left == None:
            return None


    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]

    def maxSubarray(self, nums):
        """
        https://leetcode.com/problems/maximum-subarray/description/
        :type nums: List[int]
        :rtype: int
        """
        from sys import maxsize
        max_ = -maxsize
        max_here = 0
        for num in nums:
            max_here += num
            max_here = max(max_here, num)
            max_ = max(max_, max_here)
        return max_ if max_ >= 0 else max(nums)

    def rotate(self, nums, k):
        """
        https://leetcode.com/problems/rotate-array/description/
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            val = nums.pop(0)
            nums.append(val)

    def hammingWeight(self, n):
        """
        https://leetcode.com/problems/number-of-1-bits/description/
        :type n: int
        :rtype: int
        """
        return bin(n)[2:].count('1')

    def getSum(self, a, b):
        """
        https://leetcode.com/problems/sum-of-two-integers/description/
        :type a: int
        :type b: int
        :rtype: int
        """
        s = a

        while b:
            s = a ^ b
            b = (a & b) << 1
            a = s
        return s

    def isValid(self, s):
        """
        https://leetcode.com/problems/valid-parentheses/description/
        :type s: str
        :rtype: bool
        """
        from collections import deque

        stack = deque()
        left = {'(', '{', '['}

        for char in s:
            if char in left:
                stack.append(char)
                continue

            if len(stack) == 0:
                return False

            delimiter = stack.pop()
            if not self.is_matching_delimiter(delimiter, char):
                return False

        return len(stack) == 0

    def is_matching_delimiter(self, s, t):
        if s == '(' and t == ')':
            return True
        elif s == '{' and t == '}':
            return True
        elif s == '[' and t == ']':
            return True
        else:
            return False

    def invertTree(self, root):
        """
        https://leetcode.com/problems/invert-binary-tree/description/
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def reverseWords(self, s):
        """
        https://leetcode.com/problems/reverse-words-in-a-string/description/
        :type s: str
        :rtype: str
        """
        # remove whitespace
        t = ' '.join(s.split())
        return ' '.join([word for word in t.split(" ")][::-1])

    def convert(self, s, numRows):
        """
        https://leetcode.com/problems/zigzag-conversion/
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s

        row_format = [ [c] for c in s[:numRows]]
        magic = 2 * (numRows - 1)

        for i, c in enumerate(s[numRows:], numRows):
            mod_magic = i % magic
            if mod_magic < numRows:
                row_format[i % magic].append(c)
            else:
                row_format[magic - mod_magic].append(c)

        return ''.join(map(''.join, row_format))

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicates = 0
        prev = None

        for i, num in enumerate(nums):

            if prev == num:
                duplicates += 1

            prev = num
            nums[i - duplicates] = nums[i]

        return len(nums) - duplicates

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from collections import deque
        new_sum = deque(digits)
        new_sum[-1] += 1
        carry_over = 0

        for i, num in enumerate(reversed(new_sum)):
            num += carry_over
            if num >= 10:
                num = num % 10

        if new_sum[0] == 10:
            new_sum[0] = 0
            new_sum.appendleft(1)

        print(new_sum)
        return list(new_sum)

    def addDigits(self, num):
        """
        https://leetcode.com/problems/add-digits/description/
        :type num: int
        :rtype: int
        """
        while True:
            s = str(num)
            if len(s) == num:
                return num
            else:
                num = sum(list(num))

    def findMedianSortedArrays(self, nums1, nums2):
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/description/
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        pass

    def canWinNim(self, n):
        """
        https://leetcode.com/problems/nim-game/description/
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

    def romanToInt(self, s):
        """
        https://leetcode.com/problems/roman-to-integer/description/
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        roman = {
            'I': 1,
            'II': 2,
            'III': 3,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        nums = list(map(lambda x: roman[x], list(s)))

        int_repr = []
        n = len(nums)
        should_skip = False

        for i in range(n):

            # subtractive notation
            if i < n - 1 and nums[i] < nums[i + 1]:
                int_repr.append(nums[i + 1] - nums[i])
                should_skip = True

            elif not should_skip:
                int_repr.append(nums[i])

            else:
                should_skip = not should_skip

        return sum(int_repr)

    def addTwoNumbers(self, l1, l2):
        """
        https://leetcode.com/problems/add-two-numbers/description/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        from collections import deque
        l1_iter = l1
        l2_iter = l2
        l1_val = deque([])
        l2_val = deque([])

        while True:

            if l1_iter is None and l2_iter is None:
                break

            if l1_iter is not None:
                l1_val.appendleft(str(l1_iter.val))
                l1_iter = l1_iter.next

            if l2_iter is not None:
                l2_val.appendleft(str(l2_iter.val))
                l2_iter = l2_iter.next

        l1_val = int(''.join(l1_val))
        l2_val = int(''.join(l2_val))

        #print("{} + {} = {}".format(l1_val, l2_val, l1_val + l2_val))

        sum_val = str(l1_val +  l2_val)[::-1]
        head = None
        cur = None

        for digit in sum_val:

            if head is None:
                head = ListNode(int(digit))
                cur = head
                continue

            cur.next = ListNode(int(digit))
            cur = cur.next

        return head

    def spiral_order(self, matrix):
        """
        :param matrix:
        :return:
        """
        if not matrix:
            return []

        spiral = []

        while matrix:

            spiral += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    spiral.append(row.pop())

            if matrix:
                spiral += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spiral.append(row.pop(0))

        return spiral

    def generate_matrix(self, n):
        """
        :param n:
        :return:
        """
        pass

    def find_second_min_val(self, root, mins):
        if root is None:
            return mins[1]

    def find_second_minimum_value(self, root):
        return self.find_second_min_val(root, (sys.maxsize, sys.maxsize))


    def is_perfect_square(self, n):
        """

        :param n:
        :return:
        """
        sqrt = n ** .5
        return sqrt ** 2 == n

    def is_prime(self, n):
        for i in range(3, n):
            if n % i == 0:
                return False

        if n != 1:
            return True
        else:
            return False

    def num_squares(self, n):
        """

        :param n:
        :return:
        """
        from math import sqrt

        sqrt_n = sqrt(n)
        is_perfect_square = sqrt_n ** 2 == n

        if is_perfect_square:
            """
            Obvious
            It's sum is itself if it's a perfect square
            """
            return 1

        elif self.is_prime(n):
            """
            Not so obvious
            Fermat's Theorem
            All primes are the sum of two perfect squares
            p = x ** 2 + y ** 2
            """
            return 2

        else:
            """
            Legendre's 4 Prime Theorem
            """
            num_squares = int(sqrt_n) + 1
            perfect_squares = [i ** 2 for i in range(1, num_squares)]
            N = n + 1

            factors = self.factorize(n)

            print('factors ', factors)

            length = len(perfect_squares)

            for i, factor in enumerate(reversed(factors)):
                print('factor ', factor)
                if factor in perfect_squares:
                    return factors[length - i + 1]

            # not sure if it will hit here or not
            return -1

    def factorize(self, n):
        N = n + 1

        factors = []

        for i in range(1, N):
            if n % i == 0:
                factors.append(i)

        return factors

    def subarraySum(self, nums, k):
        n = len(nums)
        k_sum_count = 0

        for i in range(n):
            if nums[i] == k:
                k_sum_count += 1
            for j in range(i + 1, n):
                if sum(nums[i:(j+1)]) == k:
                    k_sum_count += 1

        return k_sum_count

    def findRestaurant(self, list1, list2):
        #l1 = { v: k for k, v in enumerate(list1) }
        l2 = { v: k for k, v in enumerate(list2) }
        min_indices = [(1000000, 1000000)]

        for l1_idx, li in enumerate(list1):
            if li in l2:
                l2_idx = l2[li]
                idx_sum = l1_idx + l2_idx
                min_sum = sum(min_indices[0])

                if idx_sum <  min_sum:
                    min_indices = [(l1_idx, l2_idx)]
                elif idx_sum == min_sum:
                    min_indices.append((l1_idx, l2_idx))
                else:
                    continue

        return [list1[tuple[0]] for tuple in min_indices]

    def levelOrder(self, root):
        if not root:
            return [[]]

        level_begin = 0
        level_end = 1
        tree = []

        while True:

            if level_begin > len(root):
                break

            level_slice = slice(level_begin, level_end)
            level = [ x for x in root[level_slice] if isinstance(x, int)]
            tree.append(level)
            level_begin = level_end
            level_end = 2 ** (level_begin + 1) - 1

        return tree

    def height(self, root):

        if root is None:
            return 1

        return 1 + max(self.height(root.left), self.height(root.right))

    def levelOrder(self, root):
        from collections import deque
        if not root:
            return [[]]

        queue = deque([root])
        seen = { root }

    @staticmethod
    def str_math(a, b, op):
        if op == '-':
            return a - b
        elif op == '+':
            return a + b
        elif op == '*':
            return a * b
        else:
            return None

    @staticmethod
    def is_op(exp):
        return exp in "+-*"

    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]

        ways = []
        for i, ci in enumerate(input):
            if Solution.is_op(ci):
                start = self.diffWaysToCompute(input[:i])
                end  = self.diffWaysToCompute(input[i+1:])
                for j in start :
                    for k in end:
                        ways.append(Solution.str_math(j, k, ci))
        return ways

    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

    def findTheDifference(self, s, t):
        """
        https://leetcode.com/problems/find-the-difference/description/
        :type s: str
        :type t: str
        :rtype: str
        """
        from string import ascii_lowercase
        from operator import mul
        from functools import reduce

        if s == '' or t == '':
            return ''

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        char_prime = { k: v for k, v in zip(ascii_lowercase, primes) }
        prime_char = { k: v for k, v in zip(primes, ascii_lowercase) }

        s_num = reduce(mul, list(map(lambda x: char_prime[x], s)), 1)
        t_num = reduce(mul, list(map(lambda x: char_prime[x], t)), 1)

        if t_num > s_num:
            return prime_char[t_num / s_num]
        else:
            return prime_char[s_num / t_num]

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for letter in ransom:
            if ransom.get(letter, 0) > mag.get(letter, -1):
                return False

        return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        for i in range(left, right + 1):
            if i % 10 == 0:
                continue

            should_add = True
            num = str(i)

            for digit in num:
                if i % int(digit) != 0:
                    should_add = False

            if should_add:
                nums.append(i)

        return nums

    def reversePairsI(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    pairs += 1
        return pairs

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        from sys import maxsize
        n = len(nums) - k + 1
        greatest_average = -maxsize

        for i in range(n):
            greatest_average = max(float(sum(nums[i: i + k])) / k, greatest_average)

        return greatest_average

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        from string import ascii_uppercase
        from collections import deque

        num_to_char = lambda x: ascii_uppercase[x - 1]
        num = deque([])
        ascii_len = len(ascii_uppercase)

        while True:

            if n <= ascii_len:
                num.appendleft(num_to_char(n % ascii_len))
                break

            num.appendleft(num_to_char(n % ascii_len))
            n //= ascii_len

        return ''.join(num)



    def evalRPN(self, tokens):
        """
        https://leetcode.com/problems/evaluate-reverse-polish-notation/
        :type tokens: List[str]
        :rtype
        """
        ops = {
            '*': mul,
            '+': add,
            '-': sub,
            '/': truediv
        }

        stack = deque()

        for token in tokens:
            if token in ops:
                y = int(stack.pop())
                x = int(stack.pop())
                op = ops[token]
                stack.append(op(x, y))
            else:
                stack.append(token)

        return stack.pop()

    def findPeakElement(self, nums):
        """
        https://leetcode.com/problems/find-peak-element/description/
        :type nums: List[int]
        :rtype: int
        """
        from sys import maxsize
        nums.append(-maxsize)
        nums.insert(0, -maxsize)
        n = len(nums)

        for j in range(1, n - 1):
            ni = nums[j - 1]
            nj = nums[j]
            nk = nums[j + 1]

            if ni < nj and nj > nk:
                return j - 1

        return None

    def updateMatrix(self, matrix):
        """
        https://leetcode.com/problems/01-matrix/description/
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

s = Solution()
s.nextClosestTime("12:34")

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class NumArray:
    """
    https://leetcode.com/problems/range-sum-query-mutable/description/
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.vals = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.vals[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.vals[i: j + 1])
