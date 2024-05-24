class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self):
        self.start = None
    def isEmpty(self):
        return self.start == None
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n
    def insert_at_last(self, data):
        n = Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n   
    def search(self, data):
        if not self.isEmpty():
            temp = self.start 
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None 
        return None
    def insert_after(self, data, temp):
        if temp is not None:
            n = Node(data, temp.next) 
            temp.next = n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ") 
            temp = temp.next 
    def delete_first(self):
        if not self.isEmpty():
            self.start = self.start.next
    def delete_last(self):
        if not self.isEmpty():
            temp = self.start 
            if temp.next is None:
                self.start = None
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None  
    def delete_item(self, data):
        if not self.isEmpty():
            temp = self.start 
            if temp.item==data:
                temp  = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next   
    def __iter__(self):
        return SLLIterator(self.start)                

class SLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
      return self
    def __next__(self):
      if not self.current: 
          raise StopIteration
      data = self.current.item 
      self.current = self.current.next
      return data


# s  = SLL()      
# s.insert_at_start(30)
# s.insert_at_start(20)
# s.insert_at_start(10)
# s.insert_after(40,s.search(30))
# s.insert_at_last(50)
# s.insert_at_last(60)
# print(s.search(10))

# s.print_list()

                  