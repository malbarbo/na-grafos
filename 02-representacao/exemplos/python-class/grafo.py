class Vertice:
    def __init__(self, num):
        self.num = num
        self.adj = []

    def __str__(self):
        return "Vertice(%d)" % (self.num,)

class Grafo:
    def __init__(self, n):
        self.vertices = [Vertice(i) for i in range(n)]

    def addAresta(self, u, v):
        self.vertices[u].adj.append(self.vertices[v])
