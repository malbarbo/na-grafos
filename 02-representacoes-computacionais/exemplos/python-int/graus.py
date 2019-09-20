def graus_de_saida(adj):
    '''
    Exemplos
    >>> adj = [
    ...     [1, 3],
    ...     [4],
    ...     [5, 4],
    ...     [1],
    ...     [3],
    ...     [5]
    ... ]
    >>> graus_de_saida(adj)
    [2, 1, 2, 1, 1, 1]
    '''
    graus = [0] * len(adj)
    for u in range(0, len(adj)):
       for _ in adj[u]:
          graus[u] += 1
    return graus


def graus_de_entrada(adj):
    '''
    Exemplos
    >>> adj = [
    ...     [1, 3],
    ...     [4],
    ...     [5, 4],
    ...     [1],
    ...     [3],
    ...     [5]
    ... ]
    >>> graus_de_entrada(adj)
    [0, 2, 0, 2, 2, 2]
    '''
    graus = [0] * len(adj)
    for u in range(0, len(adj)):
       for v in adj[u]:
          graus[v] += 1
    return graus
