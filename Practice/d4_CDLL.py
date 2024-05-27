class Node:
    def __init__(self, item=None, next=None, prev=None):
      self.item = item
      self.next = next 
      self.prev = prev 

class CDLL:
   def __init__(self):
     self.start = None
   def is_empty(self):
      return self.start==None
   def insert_at_start(self, data):
      n = Node(data)
      if self.is_empty():
         n.next = n 
         n.prev = n 
      else:
         n.next = self.start 
         n.prev = self.start.prev
         self.start.prev.next = n 
         self.start.prev = n
      self.start = n  
   def insert_at_last(self, data):
      n = Node(data)
      if self.is_empty():
         n.next = n 
         n.prev = n 
         self.start = n 
      else:
         n.next = self.start
         n.prev = self.start.prev 
         self.start.prev.next = n 
         self.start.prev = n 
   def search(self, data):
      if self.is_empty():
         raise IndexError("List is empty")      
      else:
         temp = self.start 
         if temp.item==data:
            return temp  
         elif temp.prev.item==data:
            return temp.prev 
         while temp!=self.start.prev:
            if temp.item==data:
               return temp
            temp = temp.next 
         return "Data not in the list"   
   def insert_after(self, data, temp):
      if temp is None:
         return self 
      n = Node(data, temp.next, temp)  
      temp.next.prev = n 
      temp.next = n 
   def delete_first(self):
      if self.is_empty():
         return IndexError("List is empty")
      if self.start.next==self.start:
         self.start=None
      else:
         self.start.next.prev = self.start.prev 
         self.start.prev.next = self.start.next 
         self.start = self.start.next       
   def delete_last(self):
      if self.is_empty():
         return IndexError("List is empty")
      if self.start.next==self.start:
         self.start=None
      else:
         self.start.prev = self.start.prev.prev      
         self.start.prev.next = self.start 
   def delete_item(self, data):
      if self.is_empty():
         return "List is empty"      
      if self.start==self.start.next:
         if self.start.item==data:
            self.start=None
      else:
         temp = self.start
         if temp.item==data:
            self.delete_first() 
         while temp.next!=self.start:
            if temp.next.item==data:
               temp.next.next.prev = temp 
               temp.next = temp.next.next
               break
            temp = temp.next                 
      
   def __iter__(self):
     return CDLLiterator(self.start)
   
class CDLLiterator:
   def __init__(self, start):
     self.current = start 
     self.start = start 
     self.count = 0
   def __iter__(self):
     return self   
   def __next__(self):
     if self.current==None:
        raise StopIteration
     if self.current==self.start and self.count==1:
        raise StopIteration
     else:
        self.count = 1
     data = self.current.item 
     self.current = self.current.next 
     return data           

l = CDLL()            
l.insert_at_start(20)
l.insert_at_start(10)
l.insert_at_last(30)
l.insert_at_last(40)
print(l.search(41))
l.insert_after(35, l.search(40))
l.delete_last()
l.delete_item(10)
print([item for item in l])
       
            
            