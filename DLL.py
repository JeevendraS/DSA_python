'''   Dubbly linked list   '''

class Node:
    def __init__(self,item=None, next=None, prev=None):
        self.prev = prev
        self.item = item
        self.next = next    
class DLL:
    def __init__(self,data=None):
        n = Node(data)
        self.start = n
    def is_empty(self):
        return self.start.item==None
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.start is None:
            self.start= n
        temp = self.start 
        while temp.next is not None:
            temp = temp.next
        temp.next = n    

li = DLL(20) 
# print(li.is_empty()) 
li.insert_at_start(10) 
li.insert_at_start(5)
li.insert_at_last(55) 
print(li.start.next.next.prev.item)          