"""2405. Optimal Partition of String"""

import os
from itertools import permutations, combinations
from logfunc import logf

os.environ['LOGF_USE_PRINT'] = 'True'


@logf()
def substrs(s):
    ss, s2 = set(), str(s)
    while s2:
        for i in range(len(s2)):
            curss = s2[:i]
            if char_repeat(curss) or curss == '':
                continue
            for s in s2:
                if curss not in s and s not in curss:
                    ss.add(curss)
        s2 = s2[1:]
    return list(ss)


def char_repeat(s):
    if len(s) == len(set(s)):
        return False
    return True


def find_pairs(substrs, target):
    curpair = None

    def rec(comb, rem, target):
        for r in rem:
            newrem = [x for x in rem if x != r]
            newcomb = comb + [r]
            newl = sum(len(x) for x in newcomb)
            if newl == target:
                # print(newcomb)
                return newcomb
            elif newl < target:
                return rec(newcomb, newrem, target)

    for ss in substrs:
        newpair = rec([ss], [x for x in substrs if x != ss], target)
        print(newpair)
    return curpair


class Solution:
    def partitionString(self, s: str) -> int:
        ss = substrs(s)
        find_pairs(ss, len(s))


tc = [
    ('abacaba', 4, ['ba', 'ca', 'ba', 'a']),
    ('yzubfsiypfrepcfftiov', 4),
    ('sssss', 5),
]


for t in tc:
    print(Solution().partitionString(t[0]))
