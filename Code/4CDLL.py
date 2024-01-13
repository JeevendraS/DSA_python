class NODE:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev 
        self.item = item
        self.next = next
class CDLL:
    def __init__(self,start=None):
        self.start = start  
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n = NODE(None,data,None)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev 
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
    def insert_at_last(self,data):
        n = NODE(None,data,None)
        if self.is_empty():
            n.next = n
            n.prev = n 
            self.start = n 
        else:
            n.next = self.start 
            n.prev = self.start.prev
            self.start.prev.next = n 
            self.start.prev = n
    def search(self,data):
        temp = self.start 
        if temp==None:
            return None
        if temp.item==data:
            return temp
        else:
            temp = temp.next
        while temp!=self.start:
            if temp.item==data:
                return temp
            temp = temp.next 
        return None 
    def insert_after(self,temp,data):
        if temp is not None:
            n = NODE(None,data,None)
            n.next = temp.next 
            n.prev = temp 
            temp.next.prev = n 
            temp.next = n 
    def printlist(self):
        temp = self.start 
        if temp is not None:
            print(temp.item,end=" ")
            temp = temp.next 
            while temp!=self.start:
                print(temp.item,end=" ")
                temp = temp.next 
    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next 
                self.start.next.prev = self.start.prev 
                self.start = self.start.next 
    def delete_last(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start 
                self.start.prev = self.start.prev.prev 
    def delete_item(self,data):
        if self.start is not None:
            temp = self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp = temp.next 
                while temp!=self.start:
                    if temp.item==data:
                        temp.next.prev = temp.prev 
                        temp.prev.next = temp.next
                        break
                    temp = temp.next    
    def __iter__(self):
        return CDLLIterator(self.start) 
                       
class CDLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start 
        self.count = 0 
    def __iter__(self):
        return self 
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data = self.current.item 
        self.current = self.current.next 
        return data                         
                    
                                                                                          
                
li = CDLL()
li.insert_at_start(10)
li.insert_after(li.search(10),20)
li.insert_after(li.search(20),25)
li.insert_at_last(30)
li.insert_at_last(33)
li.insert_at_last(34)
li.insert_at_last(35)
li.insert_at_last(36)
li.insert_at_last(37)
li.insert_at_last(38)
li.delete_first()
li.delete_last()
li.delete_item(37)
li.printlist()
# for i in li:
#     print(i)
# print(li.search(10))
