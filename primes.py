import sys
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        for _ in range(vertices):
            row = [0] * vertices
            self.graph.append(row)

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V

        key[0] = 0

        min_heap = []
        for i in range(self.V):
            min_heap.append((key[i], i))
            heapq.heapify(min_heap)

        while min_heap:
            _, u = heapq.heappop(min_heap) 
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    for i in range(len(min_heap)):
                        if min_heap[i][1] == v:
                            min_heap[i] = (key[v], v)
                            break
                    heapq.heapify(min_heap)

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim_mst()
