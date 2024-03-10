"""1492. The kth Factor of n"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        curk = 0
        for i in range(n, 0, -1):
            div = n / i
            if div.is_integer():
                curk += 1
                print(div, n, i, curk)
                if curk == k:
                    return int(div)

        return -1


TEST = [((12, 3), 3), ((7, 2), 7), ((4, 4), -1)]
