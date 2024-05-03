class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
 
    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
 
# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
 
print("DFS:")
g.dfs(2)
print("\nBFS:")
g.bfs(2)



















































# the constructor (__inti__):The constructor initializes an empty dictionary self.graph to store the graph's adjacency list representation.

# Adding Edges (add_edge):
# The add_edge method takes two vertices u and v as input and adds an edge from u to v in the graph.
# If u already exists in the graph, v is appended to the list of neighbors of u. Otherwise, a new key-value pair is created in self.graph with u as the key and [v] as the value.

# Depth-First Search (DFS) Traversal:
# The dfs_util method is a helper function for DFS traversal. It recursively explores all vertices reachable from a given starting vertex.
# It takes two parameters: vertex (the current vertex being explored) and visited (a set to keep track of visited vertices).
# It marks the current vertex as visited, prints it, and then recursively calls itself for each unvisited neighbor of the current vertex.

# Breadth-First Search (BFS) Traversal:
# The bfs method performs BFS traversal starting from a specified vertex.
# It initializes an empty set visited and a queue queue with the starting vertex.
# While the queue is not empty, it dequeues a vertex, marks it as visited, prints it, and enqueues its unvisited neighbors.
# This process continues until all reachable vertices are visited.