class Graph:
    def __init__(self, vCount):
      self.vertex_count = vCount
      self.vertex_Obj = {v:[] for v in range(vCount)}
    def add_edge(self, u, v, weight=1):
       if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
          self.vertex_Obj[u].append((v,weight))
          self.vertex_Obj[v].append((u,weight))
    def remove_edge(self, u, v):
       if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
          self.vertex_Obj[u] = {(key,value) for key, value in self.vertex_Obj[u] if key!=v} 
          self.vertex_Obj[v] = {(key,value) for key, value in self.vertex_Obj[v] if key!=u}
    def has_edge(self, u, v):
       if 0<=u<self.vertex_count and 0<=v<self.vertex_count:  
          return any(vertes==v for vertes,b in self.vertex_Obj[u])   
    def print_vertexObj(self):
       for (key, value) in self.vertex_Obj.items():
          print(f"v{key}:{value}")    


obj = {
   1:[(3,4), (2,4)],
   2:[(2,4), (1,4)],
   3:[(1,4)],
   4:[(3,4)],
}

# obj2 = {(key, value) for key, value in obj[1] if key!=2}
# print(any(a==3 for a, b in obj[1]))
a = Graph(5)
a.add_edge(1,2,6)
a.add_edge(3,2,6)
a.add_edge(4,1,6)
a.add_edge(0,1,5)
a.add_edge(0,1,5)
print(a.remove_edge(1,2))
print(a.has_edge(1,2))
a.print_vertexObj()
