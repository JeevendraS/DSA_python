class PreorityQueue:
    def __init__(self):
      self.list = []
    def size(self):
       return len(self.list)  
    def is_empty(self):
       return len(self.list)==0
    def push(self, data, preority):
       if self.is_empty():
          self.list.insert(0,[data, preority])
       else:
          index = 0
          for item in self.list:
             if item[1]>preority:
                break
             index+=1
          self.list.insert(index, [data, preority])
    def pop(self):
       if self.is_empty():
          return IndexError("Preority queue is empty")
       else:
          self.list.pop(0)[0]      
            
             

l = PreorityQueue()
l.push(50, 1)
l.push(60, 5)
l.push(50, 8)
l.push(30,2)
l.push(30,7)
l.pop()

for i in l.list:
   print(i)
list = [[10,1], [20,2], [80, 4], [50, 3]]
         