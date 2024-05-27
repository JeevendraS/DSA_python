
class Stack:
    def __init__(self):
      self.array = []
    def is_empty(self):
       return len(self.array)==0
    def push(self, data):
       self.array.append(data)
    def pop(self):
       if not self.is_empty():
          self.array.pop() 
    def peek(self):
       if not self.is_empty():
          print(self.array[-1]) 
       else:
          return "Stack is Empty"  
    def size(self):
       return len(self.array)  

b = Stack()
b.push(10)
b.push(20)
b.push(30)
b.push(40)
b.push(50)
b.pop()
b.pop()
print(b.is_empty())
print(b.array)
b.peek()
