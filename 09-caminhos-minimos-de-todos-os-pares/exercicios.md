---
# vim: set spell spelllang=pt_br:
title: 09 - Caminhos mínimos de todos os pares
---

@. (CLRS3 25.1-2) Porque é necessário que $w_{ii} = 0$ para todos $1 \le i \le n$?

@. Considerando a matriz $D^{n - 1}$, produzido pelo algoritmo \proc{Slow-All-Pairs-Shortest-Paths}, mostre como calcular a matriz $\Pi^{n - 1}$ em tempo $O(n^3)$.

@. Qual o propósito do algoritmo \proc{Floyd-Warshall}? Qual técnica de projeto de algoritmo foi utilizada para construir o algoritmo? Explique.

@. Execute o algoritmo de \proc{Floyd-Warshall} para o grafo abaixo e depois, usando as matrizes $D$ e $\Pi$, encontre a árvore de caminhos mínimos de cada vértice.

    ![](imagens/Fig-25-2.pdf){width=5cm}

@. (CLRS3 25.2-5) Se modificarmos a forma que a equação 25.7 trata igualdade de

    $$\pi_{ij}^{(k)} = \begin{cases}
    \pi_{ij}^{(k-1)} & \text{se } d_{ij}^{(k-1)} \le d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\\
    \pi_{kj}^{(k-1)} & \text{se } d_{ij}^{(k-1)} > d_{ik}^{(k-1)} + d_{kj}^{(k-1)}
    \end{cases}$$

    para

    $$\pi_{ij}^{(k)} = \begin{cases}
    \pi_{ij}^{(k-1)} & \text{se } d_{ij}^{(k-1)} < d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\\
    \pi_{kj}^{(k-1)} & \text{se } d_{ij}^{(k-1)} \ge d_{ik}^{(k-1)} + d_{kj}^{(k-1)}
    \end{cases}$$

    a definição continua correta?


@. (CLRS3 25.2-6) Como podemos usar a saída do algoritmo \proc{Floyd-Warshall} para detectar a presença de ciclo de peso negativo?


# Referências

-   [CLRS3] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 25.
