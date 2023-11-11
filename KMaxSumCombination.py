import heapq
from collections import *
from math import *
from os import *
from sys import *
from typing import List


class Combination:
    def __init__(self, val: int, id1: int, id2: int) -> None:
        self.value = val
        self.id1 = id1
        self.id2 = id2

    def __lt__(self, obj: object) -> bool:
        return self.value > obj.value

    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value


def kMaxSumCombination(a: List[int], b: List[int], n: int, k: int) -> List[int]:
    # Write your code here.
    a.sort(reverse=True)
    b.sort(reverse=True)

    ans = []
    heap = [Combination(a[0] + b[0], 0, 0)]
    for i in range(k):
        max_el = heapq.heappop(heap)
        ans.append(max_el.value)

        idx_a = max_el.id1
        idx_b = max_el.id2

        if (idx_a + 1) < n:
            # can have (idx_a + 1, idx_b)
            heapq.heappush(heap, Combination(
                a[idx_a + 1] + b[idx_b], idx_a + 1, idx_b))

        if (idx_b + 1) < n:
            # can have (idx_a, idx_b + 1)
            heapq.heappush(heap, Combination(
                a[idx_a] + b[idx_b + 1], idx_a, idx_b + 1))

    return ans


if __name__ == "__main__":
    a = [1, 3, 5]
    b = [6, 4, 2]

    print(kMaxSumCombination(a, b, 3, 2))