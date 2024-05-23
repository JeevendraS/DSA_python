
# ****************************************************************************************************************


class Heap:
    def __init__(self):
        self.heap = []

    def createHeap(self, lst): 
        for e in lst:
            self.insert(e)

    def insert(self, e):
        index = len(self.heap)
        parentIndex = (index - 1) // 2
        while index > 0 and self.heap[parentIndex] < e:
            if index == len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index] = self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index - 1) // 2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index] = e

    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]

    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        temp = self.heap.pop()
        index = 0
        leftChildIndex = (2 * index) + 1
        rightChildIndex = (2 * index) + 2
        while leftChildIndex < len(self.heap):
            if rightChildIndex < len(self.heap):
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex] > temp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index = leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex] > temp:
                        self.heap[index] = self.heap[rightChildIndex]
                        index = rightChildIndex
                    else:
                        break
            else:
                if self.heap[leftChildIndex] > temp:
                    self.heap[index] = self.heap[leftChildIndex]
                    index = leftChildIndex
                else:
                    break
            leftChildIndex = (2 * index) + 1
            rightChildIndex = (2 * index) + 2
        self.heap[index] = temp
        return max_value

    def heapSort(self, lst):
        self.createHeap(lst)
        result = []
        try:
            while True:
                result.insert(0, self.delete())
        except EmptyHeapException as e:
            print(e)
        return result


class EmptyHeapException(Exception):
    def __init__(self, msg='empty heap'):
        self.msg = msg

    def __str__(self):
        return self.msg


le = [34, 23, 21, 3, 45, 67, 78, 34]
h = Heap()
print("Original Heap:", h.heap)
print("Heap Sort:", h.heapSort(le))
