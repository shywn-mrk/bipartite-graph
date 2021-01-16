from random import randint

class Graph(): 
    def __init__(self, V): 
        self.V = V 
        self.graph = [[0 for column in range(V)] for row in range(V)]

    def is_bipartite(self, src): 
        colorArr = [-1] * self.V 

        colorArr[src] = 1

        queue = [] 
        queue.append(src) 

        while queue: 
            u = queue.pop() 

            if self.graph[u][u] == 1: 
                return False

            for v in range(self.V): 
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u] 
                    queue.append(v) 

                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False

        return True


def random_adjacency_matrix(n):   
    matrix = [[randint(0, 1) for i in range(n)] for j in range(n)]

    # removes the loops
    for i in range(n):
        matrix[i][i] = 0

    # makes sure the graph is correct
    for i in range(n):
        for j in range(n):
            matrix[j][i] = matrix[i][j]

    # print(matrix)
    return matrix

graph_size = randint(3, 10)

g = Graph(graph_size)

g.graph = random_adjacency_matrix(graph_size)

print("Yes") if g.is_bipartite(0) else print("No")
