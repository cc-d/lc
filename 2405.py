"""2405. Optimal Partition of String"""

import os
from itertools import permutations, combinations
from logfunc import logf

os.environ['LOGF_USE_PRINT'] = 'True'


@logf()
def find_pairs(s):
    parts = []
    parti = 0

    for c in s:
        if parts == []:
            parts.append(set(c))
        else:
            if c in parts[parti]:
                parts.append(set(c))
                parti += 1
            else:
                parts[parti].add(c)

    return len(parts)


class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == len(set(s)):
            return 1
        return find_pairs(s)


TEST = [
    (('abacaba',), 4),
    (('yzubfsiypfrepcfftiov',), 4),
    (('sssss',), 5),
    (('cuieokbs',), 1),
    (('oygwwncfgewspmqvbez',), 3),
    (('hdklqkcssgxlvehva',), 4),
]
