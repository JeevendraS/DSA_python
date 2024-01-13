class Queue:
    def __init__(self):
        self.queue = []
        self.rear = None
        self.front = None
        self.count = 0
    def is_empty(self):
        return len(self.queue)==0 
    def enqueue(self,data):
        self.queue.append(data)
        self.front = self.queue[0]
        self.rear = data
        self.count +=1
    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0) 
            self.front = self.queue[0]
            self.count-=1
        else:
            raise IndexError("Queue is empty")  
    def get_front(self):
        if not self.is_empty():
            return self.front
        else:
            raise IndexError("Queue underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.rear
        else:
            raise IndexError("Queue  underflow")
    def size(self):
        return self.count      

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.dequeue()
q.enqueue(77)
q.dequeue()
print(q.size())
print("front is-",q.get_front(),", rear is-" ,q.get_rear())
 