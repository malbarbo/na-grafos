---
# vim: set spell spelllang=pt_br:
title: 05 - Ordenação topológica
---

1. Exercício 22.4-1 do CLRS3 ou CLRS2.

2. Exercício 22.4-2 do CLRS3 ou CLRS2. (Dica: programação dinâmica)

3. Exercício 22.4-3 do CLRS3 ou CLRS2.

4. Exercício 22.4-4 do CLRS3 ou CLRS2.

5. Exercício 22.4-5 do CLRS3 ou CLRS2.


# Referências

-   [CLRS2] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{2} edition. Capítulo 22.4.

-   [CLRS3] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.4.

\newpage


**Exercício 5 (22.4-5)**

Para cada vértice nós calculamos o grau de entrada no início do algoritmo. Nós mantemos uma fila com os vértices com grau de entrada 0. Enquanto houver vértices na fila, retiramos um vértice $u$ e adicionamos ao final de uma lista $L$, em seguida diminuímos de 1 o grau de entrada dos vértices adjacentes a $u$ para simular a remoção do vértice $u$ do grafo. Se um vértice ficar com grau de entrada igual a zero, ele é adicionado na fila. No final, se não existirem ciclos no grafo de entrada, a lista $L$ conterá os vértices em ordem topológica. Se existirem ciclos no grafo de entrada, alguns vértices nunca vão ficar com grau de entrada zero e portanto nunca vão entrar na fila. Desta forma o algoritmo irá devolver a lista $L$ incompleta. O pseudo código a seguir implementa esta ideia. Fazendo uma análise agregada podemos concluir que o tempo de execução do algoritmo é $O(V + E)$.

\begin{codebox}
  \Procname{$\proc{topological-sort2}(G)$}
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   $\attrib{u}{grau-entrada} \gets 0$
      \End
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   \For $v \in \attrib{G}{Adj}[u]$ \Do
  \li     $\attrib{v}{grau-entrada} \gets \attrib{v}{grau-entrada} + 1$
        \End
      \End
  \li $Q \gets \emptyset$
  \li $L \gets \emptyset$
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   \If $\attrib{u}{grau-entrada} \isequal 0$ \Then
  \li     $\proc{enqueue}(Q, u)$
        \End
      \End
  \li \While $Q \not = \emptyset$ \Do
  \li   $u \gets \proc{dequeue}(Q)$
  \li   Adicione $u$ no final da lista $L$
  \li   \For $v \in \attrib{G}{Adj}[u]$ \Do
  \li     $\attrib{v}{grau-entrada} \gets \attrib{v}{grau-entrada} - 1$
  \li     \If $\attrib{v}{grau-entrada} \isequal 0$ \Then
  \li       $\proc{enqueue}(Q, v)$
          \End
        \End
      \End
  \li \Return $L$
\end{codebox}
