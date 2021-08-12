from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    def insert_edge(self,v1:int,v2:int)->None:
        self.graph[v1].append(v2)
    def print_graph(self):
        for node in self.graph:
            print(str(node)+"--->",end='')
            for value in self.graph[node]:
                print(str(value),end=' ')
            print()

class undirected_graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    def insert_edge(self,v1:int,v2:int)->None:
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    def print_graph(self)->None:
        for node in self.graph:
            print(str(node)+"--->",end='')
            for value in self.graph[node]:
                print(str(value),end=' ')
            print()
if __name__=='__main__':
    g=Graph()
    g.insert_edge(1,5)
    g.insert_edge(5,2)
    g.insert_edge(2,7)
    g.insert_edge(7,1)

    g.print_graph()
    grip=undirected_graph()
    grip.insert_edge(1,5)
    grip.insert_edge(5,2)
    grip.insert_edge(2,7)
    grip.insert_edge(7,1)
    grip.print_graph()