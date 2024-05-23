class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
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
            raise IndexError("Stack is empty")     
    def size(self):
        return len(self) 
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in stack" )
    def remove(self, value):
        raise AttributeError("No attribute 'insert' in stack" )

stack = Stack()
# stack.insert(0,11)  
stack.push(12)
stack.push(13)
stack.push(14)
stack.push(15)
stack.push(16)
print(stack) 
stack.remove(15)
print(stack)
