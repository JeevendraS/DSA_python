from d1_SLL import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def isEmpty(self):
        return super().isEmpty()
    def size(self):
        return self.item_count 
    def push(self, data):
        self.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.isEmpty():
            self.delete_first() 
            self.item_count-=1
        else: 
            raise IndexError("Stack is empty")  
    def peek(self):
        if not self.isEmpty():
            return self.start.item 
        else:
            raise IndexError('Stack is empty') 
    def insert_after(self, data, temp):
        raise AttributeError("No attribute name 'insert_after' ")   

s = Stack()  
s.push(10) 
s.push(20) 
s.push(30)                   
print(s.size())
print(s.peek())
print(s.isEmpty())
      