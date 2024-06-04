class Dequeue:
    def __init__(self):
      self.pipe = []
    def is_empty(self):
       return len(self.pipe)==0
    def size(self):
       return len(self.pipe)
    def insert_front(self,data):
       self.pipe.insert(0, data)
    def insert_rear(self,data):
       self.pipe.append(data)
    def delete_rear(self):
       if not self.is_empty():
          self.pipe.pop() 
       else:
          raise IndexError("Dequeue is empty")     
    def delete_front(self):
       if not self.is_empty():
          self.pipe.pop(0) 
       else:
          raise IndexError("Dequeue is empty") 
    def get_front(self):
       if not self.is_empty():
          return self.pipe[0]  
       else:
          return None
    def get_rear(self):
       if not self.is_empty():
          return self.pipe[-1]
       else:
          return None       


a = Dequeue()        
a.insert_front(10)
a.insert_front(20)
a.insert_front(30)
a.insert_front(40)
a.insert_rear(5)
a.delete_front()
print(a.pipe, "size:-", a.size(), "front:- ", a.get_front(), "rear:- ", a.get_rear())
