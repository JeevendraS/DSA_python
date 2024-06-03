from d1_SLL import *

class Queue:
    def __init__(self):
      self.pipe = SLL()
      self.front = None
      self.rear = None 
      self.item_count = 0 
    def size(self):
       return self.item_count
    def is_empty(self):
        return self.item_count==0
    def enqueue(self, data):
       self.pipe.insert_at_start(data)
       self.item_count += 1 
    def dequeue(self):
       if not self.is_empty():
          self.pipe.delete_last()
          self.item_count -= 1
       else:
          raise IndexError("Queue is Empty")  
    def get_front(self):
       if not self.is_empty():
          return self.pipe.start.item 
       else:
          raise IndexError("Queue is empty")  
    def get_rear(self):
       if not self.is_empty():
          temp = self.pipe.start 
          while temp.next is not None:
             temp = temp.next 
          return temp.item 
    def printList(self):
       return self.pipe.print_list()           
                
a = Queue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.enqueue(40)
# a.dequeue()
# a.dequeue()
a.printList()
print("front", a.get_front())
print("rear", a.get_rear())
print(a.size())