class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class SLL:
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
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n          
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
    def search(self,data):
        temp = self.start 
        while temp is not None:
            if temp.item == data:
                return temp 
            temp = temp.next
        # return None   
    def insert_after(self,data,temp):
        if temp is  not None:
            n = Node(data,temp.next)
            temp.next = n
    def delete_first(self):
        self.start = self.start.next   
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next 
            temp.next = None 
                  
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start = None
        else:
            temp = self.start 
            if temp.item==data:
                temp = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp= temp.next    
    def __iter__(self):
         return SLLiterable()                     
class SLLiterable:
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

        
mylist = SLL(20)
# mylist.insert_at_start(5)
mylist.insert_at_start(6)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_at_start(20)
mylist.insert_after(5,mylist.search(40))
# print(mylist) 
# print(mylist.search(30))
# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_last()
mylist.delete_item(5)
# mylist.print_list()
for i in mylist:
    print(i)  