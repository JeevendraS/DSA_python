#++++++++++++++++++++++++++ Binary Tree ++++++++++++++++++++++++++++++++++++++++++++++++++
'''

Binary tree is defined as a finite set of elements, called nodes, such that 

--- T is empty (called the nulled tree or empty tree), or

--- T is contained a distinguished node R, called the root of T , and the remaining nodes of T form an ordered
pair of disjoint binary trees T1 and T2

Any node in the binary tree has either 0,1,2 child nodes.

'''


#+++++++++++++++++++++++++++++++ Binary Search Tree ++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Binary search Tree is a binary tree with the value at node N is greater than every value in the left subtree
of N and is less than every value in the right subtree of N

Unless, explicity said, BST doesn't allow duplicate values.

'''



class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item 
        self.left = left 
        self.right = right      

class BST:
    def __init__(self):
        self.root = None
    def rInsert(self,root,data):
        if root is None:
            return Node(data)
        if data>root.item:
            root.right = self.rInsert(root.right,data)    
        elif data<root.item:
            root.left = self.rInsert(root.left,data) 
        return root       
    def insert(self,data):
        self.root = self.rInsert(self.root,data)
    def rSearch(self,root,data):
        if root.item==data:
            return root
        elif data<root.item:
            return self.rSearch(root.left,data)
        elif data>root.item:
            return self.rSearch(root.right,data)
        else:
            return None            
    def search(self,data):
        return self.rSearch(self.root,data)
    def preorder(self):
        items = []
        self.rPreorder(self.root,items)
        return items
    def rPreorder(self,root,list):
        if root:
            list.append(root.item)
            self.rPreorder(root.left,list)
            self.rPreorder(root.right,list)
    def inorder(self):
        items = []
        self.rInorder(self.root,items)
        return items
    def rInorder(self,root,list):
        if root:
            self.rInorder(root.left,list)
            list.append(root.item)
            self.rInorder(root.right,list)
    def postorder(self):
        items = []
        self.rPostorder(self.root,items)
        return items
    def rPostorder(self,root,list):
        if root:
            self.rPostorder(root.left,list)
            self.rPostorder(root.right,list)
            list.append(root.item)
    def minNum(self,temp):
        current = temp 
        while current.left is not None:
            current = current.left 
        return current.item             
    def maxNum(self,temp):
        current = temp 
        while current.right is not None:
            current = current.right 
        return current.item       
    def size(self):
        return len(self.inorder())  
    def delete(self,data):
        self.root = self.rDelete(self.root,data)  
    def rDelete(self,root,data):
        if root is None:
            return root 
        if data>root.item:
            root.right = self.rDelete(root.right,data)
        elif data<root.item:
            root.left = self.rDelete(root.left,data)
        else:
             if root.right is None:
                 print(root.left)
                 return root.left 
             elif root.left is None:
                 return root.right
             root.item = self.maxNum(root.left)
             self.rDelete(root.left,root.item)
        return root     
              
                     
b = BST() 
b.insert(34)
b.insert(30)
b.insert(20)
b.insert(33)
b.insert(35)
b.insert(36)
print(b.maxNum(b.root))
print(b.minNum(b.root))
b.delete(34)
print(b.inorder())
print(b.size())
print(b.root.item)

                
                    
        
# def travers(n):
#     if n.left is not None:
#         travers(n.left)
#     if n.right is not None:
#         travers(n.right)                      
                