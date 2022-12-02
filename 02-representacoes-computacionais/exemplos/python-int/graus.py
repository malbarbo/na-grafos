#!/usr/bin/env python3

# Este programa calcula os graus de entrada e os graus de saida dos vértices de
# um grafo.

from typing import List


def graus_de_saida(adj: List[List[int]]) -> List[int]:
    '''
    Calcula os graus de saída dos vértices do grafo representado por adj.
    '''

    graus = [0] * len(adj)

    for u in range(len(adj)):
       for _ in adj[u]:
          graus[u] += 1

    return graus


def graus_de_entrada(adj: List[List[int]]) -> List[int]:
    '''
    Calcula os graus de entrada dos vértices do grafo representado por adj.
    '''

    graus = [0] * len(adj)

    for u in range(len(adj)):
       for v in adj[u]:
          graus[v] += 1

    return graus


def main():
    # Grafo da figura 22-2 do livro do Cormen.
    adj = [
        [1, 3],
        [4],
        [5, 4],
        [1],
        [3],
        [5]
    ]

    graus = graus_de_saida(adj)

    assert graus[0] == 2
    assert graus[1] == 1
    assert graus[2] == 2
    assert graus[3] == 1
    assert graus[4] == 1
    assert graus[5] == 1

    print("Função graus_de_saida: OK")

    graus = graus_de_entrada(adj)

    assert graus[0] == 0
    assert graus[1] == 2
    assert graus[2] == 0
    assert graus[3] == 2
    assert graus[4] == 2
    assert graus[5] == 2

    print("Função graus_de_entrada: OK")

if __name__ == "__main__":
    main()
