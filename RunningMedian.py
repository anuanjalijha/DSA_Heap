import heapq


class MaxHeapElement:
    def __init__(self, value) -> None:
        self.value = value

    def __lt__(self, o) -> bool:
        return self.value > o.value

    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value


def balance(min_heap, max_heap) -> None:
    if len(min_heap) > len(max_heap):
        top_el = heapq.heappop(min_heap)
        heapq.heappush(max_heap, MaxHeapElement(top_el))

    if len(max_heap) - len(min_heap) > 1:
        top_el = heapq.heappop(max_heap)
        heapq.heappush(min_heap, top_el.value)


def findMedian(arr, n):
    # Write your code here
    min_heap = []
    max_heap = []

    ans = []

    heapq.heappush(max_heap, MaxHeapElement(arr[0]))

    ans.append(arr[0])

    for i in range(1, n):
        top_element = heapq.heappop(max_heap)

        if arr[i] < top_element.value:
            # it goes in L.H
            heapq.heappush(max_heap, top_element)
            heapq.heappush(max_heap, MaxHeapElement(arr[i]))
        else:
            # it goes in U.H
            heapq.heappush(max_heap, top_element)
            heapq.heappush(min_heap, arr[i])

        balance(min_heap, max_heap)

        if i % 2 == 1:
            # even
            top1 = heapq.heappop(max_heap)
            top2 = heapq.heappop(min_heap)

            median = (top1.value + top2) // 2
            ans.append(median)
            heapq.heappush(max_heap, top1)
            heapq.heappush(min_heap, top2)
        else:
            # odd
            top1 = heapq.heappop(max_heap)
            ans.append(top1.value)
            heapq.heappush(max_heap, top1)
    return ans


if __name__ == "__main__":
    print(findMedian([6, 2, 1, 3, 7, 5], 6))