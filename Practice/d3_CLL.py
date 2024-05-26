class Node:
    def __init__(self, item=None, next=None):
      self.item = item
      self.next = next 

class CLL:
   def __init__(self):
     self.last = None 
   def is_empty(self):
      return self.last==None
   def insert_at_start(self, data):
      n = Node(data)
      if self.is_empty():
         n.next = n 
         self.last = n 
      else:
         n.next = self.last.next 
         self.last.next = n  
   def insert_at_last(self, data):
      n = Node(data)        
      if self.is_empty():
         n.next = n
         self.last = n 
      else:
         n.next = self.last.next 
         self.last.next = n  
         self.last = n 
   def search(self, data):
      if not self.is_empty():
         if self.last.item==data:
            return self.last 
         else:
            temp = self.last.next 
            while temp!=self.last:
               if temp.item==data:
                  return temp 
               temp = temp.next
            return f"{data} not in the list" 
   def insert_after(self, data, temp):
      if temp is not None:
         n = Node(data, temp.next)
         temp.next = n 
         if temp==self.last:
            self.last = n        
   def printList(self):
      if self.is_empty():
         return IndexError("list is empty")
      else:
         temp = self.last.next 
         while temp!=self.last:
            print(temp.item, end=", ") 
            temp = temp.next 
         print(temp.item)   
   def delete_first(self):
      if self.is_empty():
         return IndexError("List is Empty")
      else:
         if self.last.next==self.last:
            self.last = None
         else:   
            self.last.next = self.last.next.next 
   def delete_last(self):
      if self.is_empty():
         return IndexError("List is empty")         
      else:
         if self.last==self.last.next:
            self.last = None
         else:
            temp = self.last.next 
            while temp.next!=self.last:
               temp = temp.next
            temp.next = self.last.next
            self.last = temp     
   def delete_item(self, data):
      if self.is_empty():
         return IndexError("List is empty")
      else:
        if self.last==self.last.next:
           if self.lsat.item==data:
              self.last=None
        else:
           if self.last.item==data:
              self.delete_last()
           else:
              temp = self.last.next 
              while temp!=self.last:
                 if temp==self.last.next:
                     if temp.item==data:
                        self.delete_first()
                        break
                 if temp.next.item==data:
                    temp.next=temp.next.next 
                    break  
                 temp = temp.next 
   def __iter__(self):
     return CLLIterator(self.last.next)

class CLLIterator:
   def __init__(self, start):
     self.current = start
     self.start = start 
     self.count = 0 
   def __iter__(self):
     return self  
   def __next__(self):
      if self.current==self.start and self.count==1:
         raise StopIteration
      else:
         self.count=1
      data = self.current.item
      self.current = self.current.next 
      return data 
            

a = CLL()
a.insert_at_start(50)
a.insert_at_start(40)
a.insert_at_start(30)
a.insert_at_last(60)
a.insert_at_last(70)
a.insert_at_last(80)
a.insert_at_last(90)
a.insert_after(65, a.search(60))
a.insert_after(68, a.search(65))
# a.delete_last()
# a.delete_first()
a.delete_item(65)
a.printList()
# print(a.search(90).item)
# a.printList()

print([item for item in a])





                