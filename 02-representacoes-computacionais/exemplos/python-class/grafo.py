from typing import List

class Vertice:
    """
    Representa um vértice de um grafo com um número e uma lista de adjacências.
    """

    def __init__(self, num: int) -> None:
        """
        Cria um novo vértice com o número num e com uma lista de adjacências vazia.

        Em geral este construtor não é chamado diretamente mas é chamado pelo
        construtor da classe Grafo.
        """
        self.num = num
        self.adj: List[Vertice] = []

    def __str__(self) -> str:
        return "Vertice(%d)" % (self.num,)

class Grafo:
    """
    Representa um grafo orientado
    """

    def __init__(self, n: int) -> None:
        """
        Cria um novo grafo com n vértices com os números 0, 1, ..., n-1.
        """
        self.vertices = [Vertice(i) for i in range(n)]


    def addAresta(self, u: int, v: int):
        """
        Adiciona a aresta (u, v) ao grafo.

        u e v precisam ser vértices válidos, isto é precisam ser um valor
        entre 0 e n - 1, onde n é a quantidade de vértices do grafo.

        Este método não verifica se a aresta (u, v) já existe no grafo.
        """
        self.vertices[u].adj.append(self.vertices[v])
