#!/usr/bin/env python3
import unittest as ut
from itertools import product
from typing import List


def valid(s: str) -> bool:
    count = 0

    for c in s:
        count += 1 if c == '(' else -1
        if count < 0:
            return False

    if count != 0:
        return False

    return True


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ps = {''.join(s) for s in product('()', repeat=n * 2)}
        return [p for p in ps if valid(p)]


class Test(ut.TestCase):
    def test_valid(self):
        pairs = {
            '(())': True,
            '((())(((())(())))())': True,
            '(()()(())((())))': True,
            '(((()()()))()(())(((()': False,
            '(((((((((((((((()())((()': False,
            '(()()()': False,
        }
        for k, v in pairs.items():
            self.assertEqual(valid(k), v)

    def test_gen(self):
        for k, v in {
            2: ['()()', '(())'],
            3: ["((()))", "(()())", "(())()", "()(())", "()()()"],
            1: ['()'],
        }.items():

            self.assertEqual(set(Solution().generateParenthesis(k)), set(v))


ut.main()
