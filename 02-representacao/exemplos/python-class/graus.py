#!/usr/bin/python3

from grafo import *

def calcular_graus_de_saida(g):
    for v in g.vertices:
        # atributo criado dinamicamente, nao eh necessario declarar
        # na classe Vertice
        v.grauSaida = 0

    for u in g.vertices:
        for v in u.adj:
            u.grauSaida += 1

def mostrar_graus_saida(g):
    for v in g.vertices:
        print "%s.grauSaida = %d" % (str(v), v.grauSaida)

g = Grafo(6)
g.addAresta(0, 1)
g.addAresta(0, 3)
g.addAresta(1, 4)
g.addAresta(2, 4)
g.addAresta(2, 5)
g.addAresta(3, 1)
g.addAresta(4, 3)
g.addAresta(5, 5)

calcular_graus_de_saida(g)
mostrar_graus_saida(g)
