class Node:
    def __init__(self, item=None, next=None):
      self.item = item 
      self.next = next 
class Stack:
   def __init__(self):
     self.start = None
     self.item_count = 0
   def is_empty(self):
      return self.item_count==0
   def size(self):
      return self.item_count
   def push(self, data):
      n = Node(data)
      if not self.is_empty():
         temp = self.start 
         while temp.next is not None:
            temp = temp.next 
         temp.next = n 
         self.item_count+=1
      else:
         self.start = n 
         self.item_count+=1
   def pop(self):
      if not self.is_empty():
         temp = self.start 
         if temp.next is None:
            self.start=None
         else:
            while temp.next.next is not None:
               temp = temp.next 
            temp.next = None
            self.item_count-=1
   def peek(self):
      if not self.is_empty():
         temp = self.start 
         while temp.next is not None:
            temp = temp.next 
         return temp.item    

a = Stack()            
a.push(10)
a.push(20)
a.push(30)
# a.pop()
print(a.size())
print(a.peek())
                                   