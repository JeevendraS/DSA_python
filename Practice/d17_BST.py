# class Node:
#     def __init__(self, item=None, left=None, right=None):
#       self.item = item 
#       self.left = left 
#       self.right = right 
# class BST:
#    def __init__(self):
#      self.root = None
#    def is_empty(self):
#       return self.root==None 
#    def rInsert(self, root, data):
#       if root is None:
#          return Node(data)
#       if data<root.item:
#          root.left = self.rInsert(root.left, data)
#       elif data>root.item:
#          root.right = self.rInsert(root.right, data)
#       return root 
#    def insert(self, data):
#       self.root = self.rInsert(self.root, data) 
#    def rSearch(self, root, data):
#       if root is None:
#          return None
#       if data>root.item:
#          return self.rSearch(root.right, data)
#       elif data<root.item:
#          return self.rSearch(root.left, data)
#       elif data==root.item:
#          return root
#       else:
#          return None       
#    def search(self, data):
#       return self.rSearch(self.root, data)
#    def preOrder(self):
#       items = []  
#       self.rPreOrder(self.root, items)
#       return items 
#    def rPreOrder(self, root, list):
#       if root:
#          list.append(root.item)
#          self.rPreOrder(root.left, list)
#          self.rPreOrder(root.right, list)
#    def inOrder(self):
#       items = []      
#       self.rInOrder(self.root, items)
#       return items 
#    def rInOrder(self, root, list):
#       if root: 
#          self.rInOrder(root.left, list)
#          list.append(root.item)
#          self.rInOrder(root.right, list)
#    def postOrder(self):
#       items = []      
#       self.rPostOrder(self.root, items)
#       return items 
#    def rPostOrder(self, root, list):
#       if root: 
#          self.rPostOrder(root.left, list)
#          self.rPostOrder(root.right, list)
#          list.append(root.item)
#    def maxNum(self, root):
#       current = root
#       while current.right is not None:
#          current = current.right 
#       return current.item      
#    def minNum(self, root):
#       current = root
#       while current.left is not None:
#          current = current.left 
#       return current.item     
#    def delete(self, data):
#       self.root = self.rDelete(self.root, data)
#    def rDelete(self, root, data):
#       if root is None:
#          return None
#       if data<root.item:
#          root.left = self.rDelete(root.left, data)  
#       elif data>root.item:
#          root.right = self.rDelete(root.right, data)
#       else:
#          if root.right and root.left is None:
#             return None
#          elif root.right is None:
#             return root.left
#          elif root.left is None:
#             return root.right
#          root.item = self.maxNum(root.left)
#          root.left = self.rDelete(root.left, root.item)
#       return root    

# b = BST()   
# b.insert(50)
# b.insert(40)
# b.insert(10)
# b.insert(45)
# b.insert(60)
# b.insert(65)
# b.insert(80)
# b.insert(70)
# b.insert(85)
# b.insert(8)
# b.delete(8)
# print("inorder", b.inOrder())



# ****************************************practice*******************************************

class Node:
    def __init__(self,item, left=None, right=None):
      self.item = item 
      self.left = left 
      self.right = right 

class BST: 
   def __init__(self):
     self.root = None
   def is_empty(self):
      return self.root==None
   def insert(self, data):
      self.root = self.rInsert(self.root, data)
   def rInsert(self, root, data):
      n = Node(data)
      if root is None:
         return n
      elif data<root.item:
         root.left = self.rInsert(root.left, data)
      elif data>root.item :
         root.right = self.rInsert(root.right, data)
      return root 
   def search(self, data):
      return self.rSearch(self.root, data)
   def rSearch(self, root, data):
      if root is None:
         return None
      elif root.item==data:
         return root
      elif data<root.item:
         return self.rSearch(root.left, data)
      elif data>root.item:
         return self.rSearch(root.right, data) 
   def preOrder(self):
      items = []        
      self.rPreOrder(self.root, items)
      return items
   def rPreOrder(self, root, list):
      if root:
         list.append(root.item)
         self.rPreOrder(root.left, list)
         self.rPreOrder(root.right, list)
   def inOrder(self):
      items = []        
      self.rInOrder(self.root, items)
      return items
   def rInOrder(self, root, list):
      if root:
         self.rInOrder(root.left, list)
         list.append(root.item)
         self.rInOrder(root.right, list)
   def postOrder(self):
      items = []        
      self.rPostOrder(self.root, items)
      return items
   def rPostOrder(self, root, list):
      if root:
         self.rPostOrder(root.left, list)
         self.rPostOrder(root.right, list)
         list.append(root.item)
   def maxNum(self, temp):
      Currnet = temp 
      while Currnet.right is not None:
         Currnet = Currnet.right 
      return Currnet.item 
   def minNum(self, temp):
      Currnet = temp 
      while Currnet.left is not None:
         Currnet = Currnet.left 
      return Currnet.item 
   def delete(self, data):
      self.root = self.rDelete(self.root, data)
   def rDelete(self, root, data):
      if root is None:
         return None
      elif data<root.item:
         root.left = self.rDelete(root.left, data)
      elif data>root.item:
         root.right = self.rDelete(root.right, data)
      else:
         if root.right is None:
            return root.left 
         elif root.left is None:
            return root.right 
         root.item = self.maxNum(root.left)
         root.left = self.rDelete(root.left, root.item)
      return root             
            


b = BST()         
b.insert(50)
b.insert(40)
b.insert(10)
b.insert(45)
b.insert(60)
b.insert(8)
b.insert(65)
b.insert(80)
b.insert(70)
b.insert(85)
b.delete(8)
print(b.inOrder())
print(b.maxNum(b.root))
print(b.minNum(b.root))

