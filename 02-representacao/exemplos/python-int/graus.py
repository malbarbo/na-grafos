#!/usr/bin/python2

def calcular_graus_de_saida(adj):
    grau_saida = [0] * len(adj)
    for v in range(0, len(adj)):
       for u in adj[v]:
          grau_saida[v] += 1
    return grau_saida

def mostrar_graus_de_saida(grau_saida):
    for v in range(len(grau_saida)): 
        print "Vertice(%d).grauSaida = %d" % (v, grau_saida[v])

adj = [
  [1, 3],
  [4],
  [5, 4],
  [1],
  [3],
  [5]
]

grau_saida = calcular_graus_de_saida(adj)
mostrar_graus_de_saida(grau_saida)
