---
title: Caminhos mínimos de todos os pares
template: slide.tex
---

# Introdução

### Introdução

<!-- TODO: mostrar a formulação da estrutura ótima para o algoritmo baseado em
multiplicação de matriz !-->

-   Dado um grafo orientado $G = (V, E)$ e uma função peso $w: E \rightarrow R$,
    queremos encontrar, para todo par de vértices $u, v \in V$, o caminho de
    peso mínimo de $u$ até $v$

### Introdução

-   Podemos resolver este problema aplicando um algoritmo de caminho mínimo de
    única origem $|V|$ vezes, uma vez para cada vértice

    -   Dijkstra (sem arestas com pesos negativos)

        -   Arranjo linear: $O(V^3 + VE) = O(V^3)$

        -   Heap binário: $O(V E \lg V)$, se o grafo é denso $O(V^3 \lg V)$

        -   Heap de fibonacci: $O(V^2 \lg V + V E)$, se o grafo é denso $O(V^3)$

    -   Bellman-Ford (grafos gerais)

        -   $O(V^2E)$, se o grafo é denso $O(V^4)$

-   Veremos um algoritmo $O(V^3)$ que não usa nenhuma estrutura de dados
    especial

### Introdução

-   Considerações

    -   Supomos que não existem ciclos de pesos negativos

    -   Os vértices estão numerados como $1, 2, 3, \dots, n$, onde $n = |V|$

### Introdução

-   Entrada

    -   Uma matriz $W n \times n$ que representa os pesos das arestas. Isto é,
        $W = w_{ij}$, onde

        $$w_{ij} = \begin{cases}
              0 & \text{ se } i = j \\
              \text{o peso da aresta } (i, j) & \text{ se } i \not = j \text{ e } (i,j) \in E\\
              \infty & \text{ se } i \not = j \text{ e } (i,j) \not \in E\\
            \end{cases}$$

-   Saída

    -   Matriz $D n \times n = d_{ij}$, onde a entrada $d_{ij}$ contém o peso do
        caminho mínimo do vértice $i$ até o vértice $j$, ou seja,
        $d_{ij} = \delta(i, j)$

    -   Matriz predecessora $\Pi n \times n = \pi_{ij}$, onde $\pi_{ij}$ é o
        vértice predecessor de $j$ em um caminho mínimo a partir de $i$


# Algoritmos


## Baseado em multiplicação de matrizes

### Baseado em multiplicação de matrizes

-   Não estudaremos este algoritmo


## Algoritmo de Floyd-Warshall

### O algoritmo de Floyd-Warshall

-   Algoritmo de programação dinâmica com tempo $\Theta(V^3)$ \pause

-   Ideia

    -   O caminho mínimo pode ser calculado baseado nos caminhos mínimos para
        subproblemas já calculados e memorizados \pause

-   Etapas para resolver um problema com programação dinâmica

    -   Caracterizar a estrutura de uma solução ótima

    -   Definir recursivamente o valor da solução ótima

    -   Computar o valor da solução ótima de baixo para cima (bottom-up)

    -   Construir a solução ótima a partir das informações computadas

### O algoritmo de Floyd-Warshall

-   Para um caminho $p = \langle v_1, v_2, \dots, v_l \rangle$, um **vértice
    intermediário** é qualquer vértice de $p$ que não seja $v_1$ ou $v_l$

-   Lembramos que $n = |V|$

### Caracterização da estrutura da solução ótima

-   Considere um caminho mínimo $i \stackrel{p}{\leadsto} j$ com todo os
    vértices intermediários em $\{1, 2, \dots, k\}$

    -   Se $k$ não é um vértice intermediário de $p$, então, todos os vértices
        intermediários de $p$ estão em $\{1, 2, \dots, k - 1\}$. Deste modo, um
        caminho mínimo $i \leadsto j$ com todo os vértices intermediários no
        conjunto $\{1, 2, \dots, k - 1\}$, também é um caminho mínimo
        $i \leadsto j$ com todos os vértices intermediários no conjunto
        $\{1, 2, \dots, k\}$

    -   Se $k$ é um vértice intermediário do caminho $p$, então desmembramos o
        caminho $p$ em
        $i \stackrel{p_1}{\leadsto} k \stackrel{p_2}{\leadsto} j$. $p_1$ é um
        caminho mínimo de $i$ até $k$, com todos os vértices intermediários no
        conjunto $\{1, 2, \dots, k - 1\}$. A mesma ideia se aplica a $p_2$

        ![](Fig-25-3)

### Definição recursiva do custo da solução ótima

-   Seja $d_{ij}^{(k)}$ o peso de um caminho mínimo $i \leadsto j$ com todos
    os vértices intermediários em $\{1, 2, \dots, k\}$

    $$d_{ij}^{(k)} = \begin{cases}
           w_{ij} & \text{se } k = 0 \\
           \min(d_{ij}^{(k-1)}, d_{ik}^{(k - 1)} + d_{kj}^{(k - 1)})) & \text{se } k \ge 1
        \end{cases}$$

-   Observe que  a matriz $D^{(n)} = (d_{ij}^{(n)})$ fornece a reposta
    desejada: $d_{ij}^{(n)} = \delta(i, j)$ para todo $i, j \in V$, isto porque
    para qualquer caminho todos os vértices intermediários estão no conjunto
    $\{1, 2, …, n\}$

### O algoritmo de Floyd-Warshall

\texttt{floyd-warshall($W$)}\
\texttt{1 $n$ = $W$.linhas}\
\texttt{2 $D^{(0)}$ = $W$}\
\texttt{3 for $k = 1$ to $n$}\
\texttt{4 \ \ seja $D^{(k)} = \left ( d_{ij}^{(k)} \right )$ uma matriz $n \times n$}\
\texttt{5 \ \ for $i = 1$ to $n$}\
\texttt{6 \ \ \ \ for $j = 1$ to $n$}\
\texttt{7 \ \ \ \ \ \ $d_{ij}^{(k)}$ = min($d_{ij}^{(k-1)}$, $d_{ik}^{(k-1)} + d_{kj}^{(k-1)}$)}\
\texttt{8 return $D^{(n)}$}

\pause

-   Análise do tempo de execução

    -   Cada execução da linha 7 demora $O(1)$

    -   A linha 7 é executada $n^3$ vezes

    -   Portanto, o tempo de execução do algoritmo é $\Theta(n^3) = \Theta(V^3)$

### O algoritmo de Floyd-Warshall

![]([trim=0pt 1200pt 1200pt 0pt,clip,height=4.0cm]Fig-25-1)

### O algoritmo de Floyd-Warshall

<!-- Gerado com bin/split-image clrs/Chapter\ 25/Fig-25-4.pdf 2619 425 6 1 width=10cm !-->

![]([trim=0pt 2898pt 0pt 0pt,clip,width=10cm]Fig-25-4)

### O algoritmo de Floyd-Warshall

![]([trim=0pt 2319pt 0pt 579pt,clip,width=10cm]Fig-25-4)

### O algoritmo de Floyd-Warshall

![]([trim=0pt 1740pt 0pt 1158pt,clip,width=10cm]Fig-25-4)

### O algoritmo de Floyd-Warshall

![]([trim=0pt 1161pt 0pt 1737pt,clip,width=10cm]Fig-25-4)

### O algoritmo de Floyd-Warshall

![]([trim=0pt 582pt 0pt 2316pt,clip,width=10cm]Fig-25-4)

### O algoritmo de Floyd-Warshall

![]([trim=0pt 3pt 0pt 2895pt,clip,width=10cm]Fig-25-4)


### O algoritmo de Floyd-Warshall

-   Como construir um caminho mínimo

    -   Calcular a matriz predecessora $\Pi$, durante o calculo da matriz de
        distância de caminhos mínimos $D$

    -   Quando $k = 0$, um caminho mínimo de $i$ até $j$ não tem nenhum vértice
        intermediário, então
 
        $$\pi_{ij}^{(0)} = \begin{cases}
                \text{nil} & \text{se } i = j \text{ ou } w_{ij} = \infty\\
                i          & \text{se } i \not = j \text{ e } w_{ij} < \infty
              \end{cases}$$

    -   Quando $k \ge 1$

        $$\pi_{ij}^{(k)} = \begin{cases}
                \pi_{ij}^{(k-1)} & \text{se } d_{ij}^{(k-1)} \le d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\\
                \pi_{kj}^{(k-1)} & \text{se } d_{ij}^{(k-1)} > d_{ik}^{(k-1)} + d_{kj}^{(k-1)}
              \end{cases}$$

### O algoritmo de Floyd-Warshall

-   Considerando o exercício 25.2-4 e acrescentando o calculo de $\Pi$, podemos
    reescrever o procedimento `floyd-warshall`

### O algoritmo de Floyd-Warshall

\texttt{floyd-warshall($W$)}\
\texttt{1 $n = W$.linhas}\
\texttt{2 $D = W$}\
\texttt{3 $\Pi = \left ( \pi_{ij} \right )$ uma matriz $n \times n$}\
\texttt{4 for $i = 1$ to $n$}\
\texttt{5 \ \ for $j = 1$ to $n$}\
\texttt{6 \ \ \ \ if $i = j$ ou $w_{ij} = \infty$}\
\texttt{7 \ \ \ \ \ \ $\pi_{ij} = nil$}\
\texttt{8 \ \ \ \ if $i \not = j$ e $w_{ij} < \infty$}\
\texttt{9 \ \ \ \ \ \ $\pi_{ij} = i$}\
\texttt{10 for $k = 1$ to $n$}\
\texttt{11 \ \ for $i = 1$ to $n$}\
\texttt{12 \ \ \ \ for $j = 1$ to $n$}\
\texttt{13 \ \ \ \ \ \ if $d_{ij} > d_{ik} + d_{kj}$}\
\texttt{14 \ \ \ \ \ \ \ \ $d_{ij} = d_{ik} + d_{kj}$}\
\texttt{15 \ \ \ \ \ \ \ \ $\pi_{ij} = \pi_{kj}$}\
\texttt{16 return $D$, $\Pi$}


## Agoritmo de Johnson para grafos esparsos

### Algoritmo de Johnson para grafos esparsos

-   Não estudaremos este algoritmo

# Referências

### Referências

-   Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 25.


<!-- vim: set spell spelllang=pt_br: -->
