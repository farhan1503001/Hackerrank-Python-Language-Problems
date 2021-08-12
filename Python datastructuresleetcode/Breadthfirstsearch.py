from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    def insert_edge(self,v1:int,v2:int)->None:
        self.graph[v1].append(v2)
    def print_graph(self)->None:
        for node in self.graph:
            print(str(node)+"--->",end='')
            for value in self.graph[node]:
                print(str(value),end=' ')
            print()
    def BFS(self,startnode)->None:
        visited=set()
        queue=list()
        queue.append(startnode)
        while(len(queue)):
            u=queue.pop(0)
            if u not in visited:
                print(u,end=' ')
                visited.add(u)
            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v)

if __name__=='__main__':
    g=Graph()
    g.insert_edge(2, 1)
    g.insert_edge(2, 5)
    g.insert_edge(5, 6)
    g.insert_edge(5, 8)
    g.insert_edge(6, 9)

    g.print_graph()
    g.BFS(2)