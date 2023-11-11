import heapq
from typing import List


def find_k_smallest_elements(arr: List[int], k: int) -> List[int]:
    heapq.heapify(arr)

    return heapq.nsmallest(3, arr)


if __name__ == "__main__":
    arr = [2, 1, 4, 5, 7, 10, 3, 6]
    print(find_k_smallest_elements(arr, 3))