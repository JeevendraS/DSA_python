class Queue:
    def __init__(self):
      self.pipe = []
      self.rear = None
      self.front = None
      self.item_count = 0 
    def is_empty(self):
       return self.item_count==0
    def size(self):
       return self.item_count 
    def enqueue(self, data):
       self.pipe.insert(0, data)
       self.front = self.pipe[0] 
       self.rear = self.pipe[-1]
       self.item_count +=1 
    def dequeue(self):
       if not self.is_empty():
          self.pipe.pop()
          self.item_count-=1
       else:
          raise IndexError("queue is empty")   
    def get_front(self):
       if not self.is_empty():
          return self.pipe[-1] 
       else:
          raise IndexError("queue is empty")      
    def get_rear(self):
       if not self.is_empty():
          return self.pipe[0] 
       else:
          raise IndexError("queue is empty")      
             

             
q = Queue()    
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.is_empty())
print("front", q.get_front(), "rear", q.get_rear(), q.size())
