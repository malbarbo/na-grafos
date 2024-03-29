---
# vim: set spell spelllang=pt_br:
title: 01 - Conceitos e definições
---

1.  Usando a definição de caminho, justifique a afirmativa: sempre existe um caminho de comprimento 0 de um vértice $u$ para $u$.

2.  Liste todos os subcaminhos do caminho $\langle 1, 2, 2, 5 \rangle$.

3.  Dado um ciclo simples $c = \langle v_0, v_1, \dots, v_{k-1}, v_0 \rangle$, quantos caminhos distintos existem que formam o mesmo ciclo que $c$?

4.  Desenhe os grafos $K_1, K_2, K_3, K_4$ e $K_5$.

5.  Desenhe um grafo bipartido com 5 vértices e 6 arestas e liste os elementos dos conjuntos $V$ e $E$ do grafo e das partições $V_1$ e $V_2$.

6.  Desenhe todos os grafos que são árvores com até 4 vértices (não é necessário desenhar os grafos isomorfos).

7.  Desenhe todos os grafos que são florestas com até 5 vértices (não é necessário desenhar os grafos isomorfos).

8.  Desenhe um grafo fortemente conexo com 6 vértices e com o número mínimo possível de arestas.

9.  Desenhe um grafo não orientado com 6 vértices e três componentes usando o número mínimo possível de arestas.

10. Criar definições que de fato descrevam o conceito que queremos pode ser difícil. Além da imprecisão, podemos cometer dois erros em uma definições: generalizar demais e permitir que coisas que não gostaríamos se enquadre na definição; restringir demais e excluir coisas que gostaríamos que se enquadrasse na definição. Considere a seguinte definição que aparece em algumas versões do livro CLRS:

    - Um caminho $\langle v_0, v_1, \dots, v_k \rangle$ forma um **ciclo** se $k \ge 3$ e $v_0 = v_k$.

    Contraste essa definição com a que vimos em sala e diga (explique) se você acha que esta definição descreve de forma apropriada a noção de ciclo para grafo orientado.



\newpage


# Soluções

1. Na definição é dito que um caminho de um vértice $u$ até um vértice $u'$ é uma sequência de vértices $\langle v_0, v_1, v_2, \dots, v_k \rangle$, tal que, $u = v_0$ e $u' = v_k$ e para $i = 1, 2, \dots, k$ existe a aresta $(v_{i - 1}, v_i)$ no grafo. Quando consideramos a sequência $\langle v_0 \rangle$, podemos notar que ela forma um caminho de $v_0$ até $v_0$, pois o vértice inicial e o vértice final da sequência é $v_0$, e o conjunto de restrições de existência de arestas $(v_{i - 1}, v)$ no grafo para $i = 1, 2, \dots, k$ é vazio (pois $k = 0$), e portanto todas as restrições são satisfeitas. Desta forma, para qualquer vértices $u$, sempre existe o caminho $\langle u \rangle$ de tamanho $0$ de $u$ para $u$.

2. Subcaminhos de tamanho 0: $\langle 1 \rangle$, $\langle 2 \rangle$, $\langle 5 \rangle$. Subcaminhos de tamanho 1: $\langle 1, 2 \rangle$, $\langle 2, 2 \rangle$, $\langle 2, 5 \rangle$. Subcaminhos de tamanho 2: $\langle 1, 2, 2 \rangle$, $\langle 2, 2, 5 \rangle$ Subcaminhos de tamanho 3: $\langle 1,  2, 2, 5 \rangle$.
