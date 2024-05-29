class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self, data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop() 
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]   
        else:
            raise IndexError("Stack is Empty")  
    def size(self):
        return len(self)
    def insert(self, index, value):
        return AttributeError("No attribute 'insert' in stack")
    def remove(self, value):
        return AttributeError("No attribute 'remove' in stack")


s = Stack()  
s.push(1)       
s.push(2)       
s.push(3)       
s.push(4)

s.pop()             
print(s)