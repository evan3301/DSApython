# TODO: implement a graph and traverse via DFS

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # Adjecency matrix
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


    def add_edge(self, u, v):
        # Add edge between vertices u & v
        self.graph[u][v] = 1
        self.graph[v][u] = 1


    def dfs(self, v, visited):
        # DFS starting from vertex v
        visited[v] = True
        print(v, end='')

            # Recursively explore connected vertices
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and not visited[i]:
                 self.dfs(i, visited)


    def dfs_traversal(self, v):
        visited = [False] * self.vertices
        self.dfs(v, visited)

g = Graph(4)
g = add_edge(0, 1)
g = add_edge(1, 2)
g = add_edge(2, 4)