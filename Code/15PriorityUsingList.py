class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def is_empty(self):
        return self.item_count==0
    def push(self,data,priority):
        n = Node(data,priority) 
        if not self.start or priority< self.start.priority:
            print("yes")
            n.next = self.start 
            self.start = n
        else:
            print("no")
            temp = self.start 
            while temp.next and temp.next.priority<=priority:
                temp = temp.next 
            n.next = temp.next
            temp.next = n   
        self.item_count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")             
        data = self.start.item 
        self.start = self.start.next
        self.item_count-=1 
        return data 
    def size(self):
        return self.item_count


p = PriorityQueue()
p.push(10,23)        
p.push(20,3)        
p.push(40,33)        
# p.push(90,1)        
# p.push(50,22)  
while not p.is_empty():
    print(p.pop())      

# a = Node(20)
# b = 8
# c=9
# if not a or b<c:
#     print("yes")
# else:
#     print("no")
        
