#!/usr/bin/python3

# Este programa calcula o grau de entrada de cada vértices de um grafo.

from typing import List
from grafo import *


def graus_de_saida(g: Grafo):
    """
    Calcula os graus de saída dos vértices do grafo g.

    O grau de cada vértice é armazenado no seu atributo grauSaida.
    """
    for v in g.vertices:
        # Atributo criado dinamicamente, não é necessário declarar na
        # classe Vertice
        v.grauSaida = 0

    for u in g.vertices:
        for v in u.adj:
            u.grauSaida += 1


def main():
    # Grafo da figura 22-2 do livro do Cormen
    g = Grafo(6)
    g.addAresta(0, 1)
    g.addAresta(0, 3)
    g.addAresta(1, 4)
    g.addAresta(2, 4)
    g.addAresta(2, 5)
    g.addAresta(3, 1)
    g.addAresta(4, 3)
    g.addAresta(5, 5)

    graus_de_saida(g)

    assert g.vertices[0].grauSaida == 2
    assert g.vertices[1].grauSaida == 1
    assert g.vertices[2].grauSaida == 2
    assert g.vertices[3].grauSaida == 1
    assert g.vertices[4].grauSaida == 1
    assert g.vertices[5].grauSaida == 1


if __name__ == "__main__":
    main()
