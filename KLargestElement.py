import heapq
def kLargest(lst, k):
    # Convert the list into a max-heap
    if k <= 0:
        return []

    if k >= len(lst):
        return lst

    # Convert the first k elements into a min-heap
    max_heap = lst[:k]
    heapq.heapify(max_heap)

    # Iterate through the remaining elements
    for num in lst[k:]:
        if num > max_heap[0]:
            # If the current element is larger than the smallest element in the heap, replace the smallest element with the current element
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, num)

    # The max_heap now contains the k largest elements in ascending order. To get them in descending order, you can reverse the result.
    return sorted(max_heap, reverse=True)
