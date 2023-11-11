import heapq
class Heap:
    def __init__(self, max_size: int) -> None:
        self.heap = [0 for _ in range(max_size)]
        self.size = 0
    """
     a is current, b is target
     Returns true if b is to  be swapped with a
    """
    def compare(self, a, b) -> bool:
        return a > b
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
    """
     Inserts val into the heap
    """
    def insert(self, val: int) -> None:
        self.size += 1
        # Inserted value at end of heap
        self.heap[self.size] = val
        # Move the value to its actual place
        idx = self.size
        while idx > 1:
            parent = idx // 2
            if self.compare(self.heap[parent], self.heap[idx]):
                self.swap(parent, idx)
                idx = parent
            else:
                break
    def heapify(self, pos) -> None:
        idx = pos
        while 2*idx <= self.size:
            g = idx
            left = 2 * idx
            right = 2 * idx + 1
            if self.compare(self.heap[idx], self.heap[left]):
                g = left
            if right <= self.size and self.compare(self.heap[g], self.heap[right]):
                g = right
            if g == idx:
                break
            self.swap(g, idx)
            idx = g
    def remove(self) -> int:
        self.swap(1, self.size)
        self.size -= 1
        self.heapify(1)
        return self.heap[self.size + 1]
    def print(self) -> None:
        print("Heap is: ")
        for i in range(1, self.size+1):
            print(self.heap[i],)
        print("\n =============")
if __name__ == "__main__":
    # heap = Heap(10)
    # heap.insert(10)
    # heap.insert(20)
    # heap.insert(30)
    # heap.insert(25)
    # heap.insert(35)
    # print("Smallest element is: " + str(heap.remove()))
    # heap.print()
    a = [20, 10]
    heapq.heapify(a)
    heapq.heappush(a, 30)
    heapq.heappush(a, 35)
    heapq.heappush(a, 25)
    print("Smallest element is: " + str(a[0]))
    heapq.heappop(a)
    print("Second smallest: " + str(heapq.heappop(a)))
    print("Third smallest: " + str(heapq.heappop(a)))