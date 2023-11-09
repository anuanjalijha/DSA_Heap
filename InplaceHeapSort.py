def heapify(arr, n, i):
    largest = i  # Initialize the largest element as the root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child exists and is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child exists and is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    ######################
    #PLEASE ADD CODE HERE#
    ######################

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')