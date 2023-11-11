from typing import List
from queue import PriorityQueue


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    if k == n:
        return arr

    mp = {}
    #  Build map where the key is element
    # and value is how often this element appears in 'ARR'.

    for ele in arr:
        if ele not in mp:
            mp[ele] = 0
        mp[ele] += 1

    # Elements in heap will be sorted in descending order
    # according to the frequency of the element.
    heap = PriorityQueue()

    # Build heap of maximum size 'K'.
    for x in mp:
        heap.put([-mp[x], -x])

    ans = [0 for i in range(k)]

    # Build output array.
    for i in range(k):
        ans[i] = -heap.get()[1]

    ans.sort()
    return ans    
    # write your code here
