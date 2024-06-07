class Node:
    def __init__(self, data, preority=None, next=None):
      self.item = data
      self.preority = preority
      self.next = next 

class PreorityQueue:
   def __init__(self):
     self.start = None
     self.item_count = 0
   def is_empty(self):
      return self.item_count==0
   def size(self):
      return self.item_count
   def push(self, data, preority):
      n = Node(data,preority)
      if self.is_empty() or preority<self.start.preority:
         n.next = self.start 
         self.start = n 
      else:
         temp = self.start 
         while temp.next and temp.next.preority<=preority:
            temp = temp.next 
         n.next = temp.next 
         temp.next = n 
      self.item_count+=1 
   def pop(self):
      if self.is_empty():
         return IndexError("preority queue is empty")  
      else:
         data = self.start.item 
         self.start = self.start.next 
         self.item_count-=1 
         return data 
   def __iter__(self):
     return PQueueIterator(self.start) 

class PQueueIterator:
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

l = PreorityQueue()                
l.push(10, 5)
l.push(20, 3)
l.push(80, 1)
l.push(90, 4)
l.push(0, 0)
l.pop()

print(l.size())
for i in l:
   print(i)
              