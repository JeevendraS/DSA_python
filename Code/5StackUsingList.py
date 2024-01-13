class STACK:
    def __init__(self):
        self.container = []
    def is_empty(self):
        return len(self.container)==0
    def push(self,data):
        self.container.insert(0,data)
    def pop(self):
        if not self.is_empty():
            return self.container.pop(0)
        else:
            raise IndexError 
    def peek(self):
        if not self.is_empty():
            return print(self.container[0])
        else:
            raise IndexError("Stack is empty")
    def size(self):
        print(len(self.container))            

s = STACK()
s.push(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)
s.push(15)
s.pop()
s.peek()
s.size()


