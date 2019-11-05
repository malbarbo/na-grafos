---
# vim: set spell spelllang=pt_br:
title: Caminhos mínimos de todos os pares
---

## Introdução

<!-- TODO: mostrar a formulação da estrutura ótima para o algoritmo baseado em
multiplicação de matriz !-->

- Dado um grafo orientado $G = (V, E)$ e uma função peso $w: E \rightarrow R$,
  queremos encontrar, para todo par de vértices $u, v \in V$, o caminho de peso
  mínimo de $u$ até $v$


## Introdução

- Podemos resolver este problema aplicando um algoritmo de caminho mínimo de
  única origem $|V|$ vezes, uma vez para cada vértice

    - Dijkstra (sem arestas com pesos negativos)

        - Arranjo linear: $O(V^3 + VE) = O(V^3)$

        - Heap binário: $O(V E \lg V)$, se o grafo é denso $O(V^3 \lg V)$

        - Heap de fibonacci: $O(V^2 \lg V + V E)$, se o grafo é denso $O(V^3)$

    - Bellman-Ford (grafos gerais)

        - $O(V^2E)$, se o grafo é denso $O(V^4)$

- Veremos um algoritmo $O(V^3)$ que não usa nenhuma estrutura de dados especial


## Introdução

- Considerações

    - Supomos que não existem ciclos de pesos negativos

    - Os vértices estão numerados como $1, 2, 3, \dots, n$, onde $n = |V|$


## Introdução

- Entrada

    - Uma matriz $W n \times n$ que representa os pesos das arestas. Isto é,
      $W = w_{ij}$, onde

      $$w_{ij} = \begin{cases}
          0 & \text{ se } i = j \\
          \text{o peso da aresta } (i, j) & \text{ se } i \not = j \text{ e } (i,j) \in E\\
          \infty & \text{ se } i \not = j \text{ e } (i,j) \not \in E\\
      \end{cases}$$

- Saída

    - Matriz $D n \times n = d_{ij}$, onde a entrada $d_{ij}$ contém o peso do
      caminho mínimo do vértice $i$ até o vértice $j$, ou seja, $d_{ij}
      = \delta(i, j)$

    - Matriz predecessora $\Pi n \times n = \pi_{ij}$, onde $\pi_{ij}$
      é o vértice predecessor de $j$ em um caminho mínimo a partir de $i$


## Baseado em multiplicação de matrizes

- Não estudaremos este algoritmo


## O algoritmo de Floyd-Warshall

- Algoritmo de programação dinâmica com tempo $\Theta(V^3)$ \pause

- Ideia

    - O caminho mínimo pode ser calculado baseado nos caminhos mínimos para
      subproblemas já calculados e memorizados \pause

- Etapas para resolver um problema com programação dinâmica

    - Caracterizar a estrutura de uma solução ótima

    - Definir recursivamente o valor da solução ótima

    - Computar o valor da solução ótima de baixo para cima (bottom-up)

    - Construir a solução ótima a partir das informações computadas


## O algoritmo de Floyd-Warshall

- Para um caminho $p = \langle v_1, v_2, \dots, v_l \rangle$, um **vértice
  intermediário** é qualquer vértice de $p$ que não seja $v_1$ ou $v_l$

- Lembramos que $n = |V|$


## Caracterização da estrutura da solução ótima

- Considere um caminho mínimo $i \stackrel{p}{\leadsto} j$ com todo os vértices
  intermediários em $\{1, 2, \dots, k\}$

    - Se $k$ não é um vértice intermediário de $p$, então, todos os vértices
      intermediários de $p$ estão em $\{1, 2, \dots, k - 1\}$. Deste modo, um
      caminho mínimo $i \leadsto j$ com todo os vértices intermediários no
      conjunto $\{1, 2, \dots, k - 1\}$, também é um caminho mínimo $i \leadsto
      j$ com todos os vértices intermediários no conjunto $\{1, 2, \dots, k\}$

    - Se $k$ é um vértice intermediário do caminho $p$, então desmembramos
      o caminho $p$ em $i \stackrel{p_1}{\leadsto} k \stackrel{p_2}{\leadsto}
      j$. $p_1$ é um caminho mínimo de $i$ até $k$, com todos os vértices
      intermediários no conjunto $\{1, 2, \dots, k - 1\}$. A mesma ideia se
      aplica a $p_2$

      ![](imagens/Fig-25-3.pdf)


## Definição recursiva do custo da solução ótima

- Seja $d_{ij}^{(k)}$ o peso de um caminho mínimo $i \leadsto j$ com todos os
  vértices intermediários em $\{1, 2, \dots, k\}$

    $$d_{ij}^{(k)} = \begin{cases}
           w_{ij} & \text{se } k = 0 \\
           \min(d_{ij}^{(k-1)}, d_{ik}^{(k - 1)} + d_{kj}^{(k - 1)})) & \text{se } k \ge 1
        \end{cases}$$

- Observe que  a matriz $D^{(n)} = (d_{ij}^{(n)})$ fornece a reposta desejada:
  $d_{ij}^{(n)} = \delta(i, j)$ para todo $i, j \in V$, isto porque para
  qualquer caminho todos os vértices intermediários estão no conjunto $\{1, 2,
  \dots, n\}$


## O algoritmo de Floyd-Warshall

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{floyd-warshall}(W)$}
    \li $n$ = $\attrib{W}{linhas}$
    \li $D^{(0)} = W$
    \li \For $k \gets 1$ \To $n$ \Do
    \li     seja $D^{(k)} = \left ( d_{ij}^{(k)} \right )$ uma matriz $n \times n$
    \li     \For $i \gets 1$ \To $n$ \Do
    \li         \For $j \gets 1$ \To $n$ \Do
    \li             $d_{ij}^{(k)} = \min(d_{ij}^{(k-1)}, d_{ik}^{(k-1)} + d_{kj}^{(k-1)})$
                \End
            \End
        \End
    \li \Return $D^{(n)}$
\end{codebox}
</div>
<div class="column" width="40%">
\pause
Análise do tempo de execução
\pause

- Cada execução da linha 7 demora $O(1)$

- A linha 7 é executada $n^3$ vezes

- Portanto, o tempo de execução do algoritmo é $\Theta(n^3) = \Theta(V^3)$
</div>
</div>


## O algoritmo de Floyd-Warshall

\includegraphics[trim=0pt 1200pt 1200pt 0pt,clip,height=4.0cm]{imagens/Fig-25-1.pdf}


## O algoritmo de Floyd-Warshall

<!-- Gerado com bin/split-image clrs/Chapter\ 25/Fig-25-4.pdf 2619 425 6 1 width=10cm !-->

\includegraphics[trim=0pt 2898pt 0pt 0pt,clip,width=10cm]{imagens/Fig-25-4.pdf}

## O algoritmo de Floyd-Warshall

\includegraphics[trim=0pt 2319pt 0pt 579pt,clip,width=10cm]{imagens/Fig-25-4.pdf}

## O algoritmo de Floyd-Warshall

\includegraphics[trim=0pt 1740pt 0pt 1158pt,clip,width=10cm]{imagens/Fig-25-4.pdf}

## O algoritmo de Floyd-Warshall

\includegraphics[trim=0pt 1161pt 0pt 1737pt,clip,width=10cm]{imagens/Fig-25-4.pdf}

## O algoritmo de Floyd-Warshall

\includegraphics[trim=0pt 582pt 0pt 2316pt,clip,width=10cm]{imagens/Fig-25-4.pdf}

## O algoritmo de Floyd-Warshall

\includegraphics[trim=0pt 3pt 0pt 2895pt,clip,width=10cm]{imagens/Fig-25-4.pdf}


## O algoritmo de Floyd-Warshall

- Como construir um caminho mínimo

    - Calcular a matriz predecessora $\Pi$, durante o calculo da matriz de
      distância de caminhos mínimos $D$

    - Quando $k = 0$, um caminho mínimo de $i$ até $j$ não tem nenhum vértice
      intermediário, então

      $$\pi_{ij}^{(0)} = \begin{cases}
            \text{nil} & \text{se } i = j \text{ ou } w_{ij} = \infty\\
            i          & \text{se } i \not = j \text{ e } w_{ij} < \infty
      \end{cases}$$

    - Quando $k \ge 1$

      $$\pi_{ij}^{(k)} = \begin{cases}
            \pi_{ij}^{(k-1)} & \text{se } d_{ij}^{(k-1)} \le d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\\
            \pi_{kj}^{(k-1)} & \text{se } d_{ij}^{(k-1)} > d_{ik}^{(k-1)} + d_{kj}^{(k-1)}
      \end{cases}$$


## O algoritmo de Floyd-Warshall

- Considerando o exercício 25.2-4 e acrescentando o calculo de $\Pi$, podemos
  reescrever o procedimento \proc{floyd-warshall}


## O algoritmo de Floyd-Warshall

\footnotesize

\begin{codebox}
    \Procname{$\proc{floyd-warshall}(W)$}
    \li $n = \attrib{W}{linhas}$
    \li $D = W$
    \li $\Pi = \left ( \pi_{ij} \right )$ uma matriz $n \times n$
    \li \For $i = 1$ \To $n$ \Do
    \li     \For $j = 1$ \To $n$ \Do
    \li         \If $i = j$ ou $w_{ij} = \infty$ \Then
    \li             $\pi_{ij} = \const{nil}$
                \End
    \li         \If $i \not = j$ e $w_{ij} < \infty$ \Then
    \li             $\pi_{ij} = i$
                \End
            \End
        \End
    \li \For $k = 1$ \To $n$ \Do
    \li     \For $i = 1$ \To $n$ \Do
    \li         \For $j = 1$ \To $n$ \Do
    \li             \If $d_{ij} > d_{ik} + d_{kj}$ \Then
    \li                 $d_{ij} = d_{ik} + d_{kj}$
    \li                 $\pi_{ij} = \pi_{kj}$
                     \End
                \End
            \End
        \End
    \li \Return $D$, $\Pi$
\end{codebox}


## Algoritmo de Johnson para grafos esparsos

- Não estudaremos este algoritmo


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 25.
