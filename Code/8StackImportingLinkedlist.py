from a1SLL import *
class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0
    def is_empty(self): 
        return self.mylist.is_empty() 
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item 
        else:
            raise IndexError("Stack is empty")            
    def size(self):
        return self.item_count        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("before deletion", s.peek(),s.size())
s.pop()
s.pop()
s.pop()
s.pop()
print("after deletion", s.peek(),s.size())
