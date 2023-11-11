import heapq
from collections import *
from math import *
from os import *
from sys import *


class Element:
    def __init__(self, value, index) -> None:
        self.value = value
        self.index = index

    def __lt__(self, o) -> bool:
        return self.value < o.value

    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value


def mergeKSortedArrays(kArrays, k: int):
    # Write your code here.
    # kArrays is a list of 'k' lists.
    # Return a list.
    h = [Element(kArrays[i][0], i) for i in range(k)]
    ptr = [0 for _ in range(k)]

    heapq.heapify(h)

    ans = []

    num_elements = 0
    for i in range(k):
        for j in range(len(kArrays[i])):
            num_elements += 1
    """
    TC: N * log k
    SC: k
    """
    for i in range(num_elements):
        top_ele = heapq.heappop(h)
        ans.append(top_ele.value)
        index = top_ele.index
        ptr[index] += 1
        if ptr[index] == len(kArrays[index]):
            continue
        else:
            heapq.heappush(h, Element(kArrays[index][ptr[index]], index))

    return ans


if __name__ == "__main__":
    print(mergeKSortedArrays([[2, 4, 5, 6], [1, 3], [1, 2, 7]], 3))