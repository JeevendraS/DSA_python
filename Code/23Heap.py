class Heap:
    def __init__(self):
        self.heap = []
    def createHeap(self,list):
        for e in list:
            self.insert(e)
    def insert(self,e):
        index = len(self.heap)
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex]) 
            else:
                self.heap[index]=self.heap[parentIndex]           
            index = parentIndex
            parentIndex = (index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]  
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException
        if len(self.heap)==1:
            return self.heap.pop()    
        max_value = self.heap[0]    
        temp = self.heap.pop()
        index = 0
        leftChildIndex = (2*index)+1
        rightChildIndex = (2*index)+2
        

class EmptyHeapException:
    def __init__(self,msg='empty heap'):
        self.msg = msg
    def __str__(self):
        return self.msg        