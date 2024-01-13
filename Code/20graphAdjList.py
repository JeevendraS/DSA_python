class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}
    def add_edge(self,u,v,weight=1):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("invalid vertex")  
    def remove_edge(self,u,v):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            self.adj_list[u] =  [(key,value) for key,value in self.adj_list[u] if key!=v]
            self.adj_list[v] =  [(key,value) for key,value in self.adj_list[v] if key!=u]
        else:
            print("invalid edge")    
    def has_edge(self,u,v):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            return any(vertex==v for vertex,x in self.adj_list[u])
        else:
            print("invalid vertex")
    def print_list(self):
        for key,value in self.adj_list.items():
            print(f"V {key} : {value}")      


             
        

b = Graph(5)
b.add_edge(1,2,5)
b.add_edge(0,2,6)
b.add_edge(0,3,6)
b.add_edge(4,3,6)
# print(b.remove_edge(0,3))
print(b.adj_list)
print(b.has_edge(3,2))
b.print_list()

# li = [(34,34),(3,4),(32,2),(4,5),(32,45)]
# li = [ (key,value) for key,value in li if key!=3]
# print(li)
