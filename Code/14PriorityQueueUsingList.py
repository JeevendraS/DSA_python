class PriorityQueue:
    def __init__(self):
        self.items = []
    def push(self,data,priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0    
    def pop(self):
        if self.is_empty():
            raise IndexError("PriorityQueue is empty")  
        else:
            return self.items.pop(0)[0]  
    def size(self):
        return len(self.items) 

p = PriorityQueue()
p.push(10,2)               
p.push(130,8)               
p.push(100,3)               
p.push(70,1)               
p.push(90,20)
print("pop",p.pop())

for i in range(len(p.items)):
    print(p.pop())

            