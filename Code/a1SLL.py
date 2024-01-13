'''  Singly Linked List       '''

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
class SLL:
    def __init__(self,start=None):
        n = Node(start)
        self.start = n
    def is_empty(self):
        return self.start==None 
    def insert_at_start(self, data):
        n = Node(data,self.start)
        self.start = n 
    def insert_at_last(self,data):
        n = Node(data) 
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None 
    def insert_after(self,data,temp):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
    def printlist(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is  None:
            self.start =  None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None 
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item ==data:
                self.start = None
        else:
            temp = self.start
            if temp.item==data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp = temp.next
    def __iter__(self):
        return SLLIterator(self.start)
                     
class SLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
      
      
          
'''
mylist = SLL()
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_last(20)
mylist.insert_at_last(60)
mylist.insert_at_last(70)
# mylist.insert_after(11,mylist.search(40))
# mylist.delete_item(40)
# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_last()
# mylist.printlist()
for i in mylist:
    print(i)

'''        
