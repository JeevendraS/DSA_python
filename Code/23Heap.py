class Heap:
    def __init__(self):
        self.heap = []
    def createHeap(self,list):
        for e in list:
            self.insert(e)
            