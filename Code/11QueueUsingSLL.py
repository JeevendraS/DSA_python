class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n 
        self.rear = n
        self.item_count+=1 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")  
        elif self.rear == self.front:
            self.rear = None
            self.front = None
        else:
            self.front = self.front.next 
        self.item_count-=1
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Empty Queue")         
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item 
        else:
            raise IndexError("Empty Queue") 
    def size(self):
        return self.item_count            


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print("the front value is =",q.get_front(), "the rear value is =",q.get_rear())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
try:
  q.dequeue()
except:
  print("failed")
# print("the front value is =",q.get_front(), "the rear value is =",q.get_rear())
print(q.size())