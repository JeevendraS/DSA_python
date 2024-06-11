class Graph:
    def __init__(self, vno):
      self.vno = vno 
      self.adj_matrix = [[0]*vno for i in range(vno)]
    def add_edge(self, u, v, weight=1):
       if 0<=u<self.vno and 0<=v<self.vno:
          self.adj_matrix[u][v] = weight  
          self.adj_matrix[v][u] = weight  
    def remove_edge(self, u, v):
       if 0<=u<self.vno and 0<=v<self.vno:
          self.adj_matrix[u][v] = 0
          self.adj_matrix[v][u] = 0
    def has_edge(self, u, v):
       if 0<=u<self.vno and 0<=v<self.vno:
          return self.adj_matrix[u][v]!=0  
    def print_adjMatrix(self):
       for i in self.adj_matrix:
         print("|".join(map(str, i)))
a = Graph(5)
a.add_edge(1,1,5)
a.add_edge(1,0,5)
a.add_edge(5,5,5)
a.print_adjMatrix()


