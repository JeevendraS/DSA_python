from for_import import *
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
    def travers(self,src):
        Q = Queue()
        Q.enqueue(src)
        visited = [False]*self.vertex_count
        visited[src] = True
        while not Q.is_empty():
            n = Q.get_front()
            Q.dequeue()
            print(n)
            for i in self.adj_list[n]:
                if visited[i[0]] == False:
                    Q.enqueue(i[0])
                    visited[i[0]] = True


g = Graph(9)
g.add_edge(0,1)             
g.add_edge(1,2)             
g.add_edge(1,3)             
g.add_edge(3,6)             
g.add_edge(4,7)             
g.add_edge(5,8)             
g.add_edge(6,8)             
g.add_edge(0,8)             
g.add_edge(3,5)             
g.add_edge(5,7)             
g.add_edge(8,1)             

g.print_list()
g.travers(0)
            



# q = Queue()
# q.enqueue(20)
# q.enqueue(21)
# q.enqueue(22)
# q.enqueue(23)
# q.enqueue(24)
# q.enqueue(25)
# q.dequeue()
# print(q.size())
# print(q.rear)
# print(q.front)
# g = Graph(5)
# g.travers(1)
