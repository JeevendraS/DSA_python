class Node:
    def __init__(self, item=None, next=None, prev=None):
      self.item = item
      self.next = next
      self.prev = prev

class DLL:
   def __init__(self):
     self.start= None
   def is_empty(self):
      return self.start==None  
   def insert_at_start(self, data):
      n = Node(data, self.start)
      if not self.is_empty():
         self.start.prev = n
      self.start = n  
   def insert_at_last(self, data):
      n = Node(data)
      if not self.is_empty():
         temp = self.start 
         while temp.next is not None:
            temp = temp.next 
         n.prev = temp 
         temp.next = n 
      else:
         self.start = n   
   def print_list(self):
      if not self.is_empty():
         temp = self.start 
         while temp is not None:
            print(temp.item, end=" ") 
            temp = temp.next 
   def search(self, data):
      if not self.is_empty():
         temp = self.start 
         while temp is not None:
            if temp.item == data:
               return temp
            temp = temp.next  
         raise IndexError("Item not in the list")     
      else:
         raise IndexError("list is empty") 
   def insert_after(self, data, temp):
      if temp is not None:
          n = Node(data, temp.next, temp)
          if temp.next is not None:
             temp.next.prev = n
          temp.next = n  
   def delete_first(self):
      if not self.is_empty():
         if self.start.next is None:
            self.start = None
         else:
            self.start = self.start.next
            self.start.prev = None
      else:
         raise IndexError("Empty list")      
   def delete_last(self):
      if not self.is_empty():
         if self.start.next is None:
            self.start = None
         else:
            temp = self.start 
            while temp.next is not None:
               temp = temp.next
            temp.prev.next =  None   
      else:
         raise IndexError("Empty list")      
   def delete_item(self, data):
      if not self.is_empty():
         if self.start.next is None:
            if self.start.item == data:
               self.start = None
            else:
               raise IndexError("Item not found")   
         else:
            temp = self.start 
            while temp is not None:
               if temp.item==data:
                  temp.prev.next = temp.next
                  break 
               temp = temp.next
      else:
         raise IndexError("Empty list")    
   def __iter__(self):
      return DLLIterator(self.start)    



class DLLIterator:
   def __init__(self, start):
     self.current = start
   def __iter__(self):
     return self  
   def __next__(self):
     if not self.current:
        raise StopIteration
     data = self.current.item 
     self.current = self.current.next 
     return data
         
a = DLL()
a.insert_at_start(30)
a.insert_at_start(20)
a.insert_at_start(10)
a.insert_at_last(40)
a.insert_at_last(200)
a.insert_at_last(20)
# a.insert_after(55, a.search(500))
# print(a.search(20))
# a.delete_first()
# a.delete_last()
a.delete_item(20)
a.print_list() 

li = [item for item in a]


 