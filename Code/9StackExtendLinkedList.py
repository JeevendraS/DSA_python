from a1SLL import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack Underflow")    
    def peek(self):
        if not self.is_empty():
            return self.start.item 
        else:
            raise IndexError("Stack Underflow")
    def size(self):
        return self.item_count    
                
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print("before deletion", s.peek(),s.size())
s.pop()
s.pop()
s.pop()
s.pop()
print("after deletion", s.peek(),s.size())