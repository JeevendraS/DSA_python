class Node:
    def __init__(self, item=None, next=None, prev=None):
      self.item = item 
      self.next = next 
      self.prev = prev 

class Dequeue:
   def __init__(self):
     self.pipe = None
     self.front = None
     self.rear = None
     self.item_count = 0 
   def is_empty(self):
      return self.item_count==0
   def size(self):
      return self.item_count
   def insert_front(self, data):
      n = Node(data)
      if not self.is_empty():
         self.pipe.prev = n 
         n.next = self.pipe
      self.pipe = n 
      self.item_count+=1  
   def insert_rear(self, data):
      n = Node(data)
      if self.is_empty():
         self.pipe = n 
      else:   
         temp = self.pipe 
         while temp.next is not None:
            temp = temp.next 
         n.prev = temp 
         temp.next = n 
      self.item_count += 1    
   def delete_front(self):
      if not self.is_empty():
         if self.pipe.next is None:
            self.pipe = None
         else:
            self.pipe = self.pipe.next 
            self.pipe.prev  = None
         self.item_count-=1
   def delete_rear(self):
      if not self.is_empty():
         if self.pipe.next is None:
            self.pipe = None
         else:
            temp = self.pipe 
            while temp.next is not None:
               temp = temp.next 
            temp.prev.next = None
         self.item_count-=1
   def get_front(self):
      if not self.is_empty():
         return self.pipe.item 
   def get_rear(self):
      if not self.is_empty():
         temp = self.pipe
         while temp.next is not None:
            temp = temp.next 
         return temp.item


a = Dequeue()                                                     
a.insert_front(23)
a.insert_front(22)
a.insert_front(21)
a.insert_front(20)
a.insert_front(10)
a.insert_front(5)
a.insert_front(1)
a.insert_rear(30)
a.insert_rear(40)
a.insert_rear(50)
a.delete_front()
a.delete_rear()
a.delete_rear()
a.delete_rear()
print("size", a.size(), "front:-", a.get_front(), "rear:-", a.get_rear())
           
         