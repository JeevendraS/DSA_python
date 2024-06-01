from d1_SLL import *
class Stack:
    def __init__(self):
      self.container = SLL()
      self.item_count = 0
    def is_empty(self):
       return self.item_count==0
    def size(self):
       return self.item_count
    def push(self, data):
       self.container.insert_at_start(data)
       self.item_count+=1
    def pop(self):
       self.container.delete_first()
       self.item_count-=1
    def peek(self):
       if not self.is_empty():
          return self.container.start.item
b = Stack()  
b.push(10)     
b.push(20)     
b.push(30)     
b.push(40)   
b.pop()  
print(b.peek())
print(b.size())
               