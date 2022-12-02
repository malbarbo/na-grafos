---
# vim: set spell spelllang=pt_br:
title: Caminhos mínimos de todos os pares
---

## Introdução

<!-- TODO: mostrar a formulação da estrutura ótima para o algoritmo baseado em
multiplicação de matriz !-->

Dado um grafo orientado $G = (V, E)$ e uma função peso $w: E \rightarrow R$, queremos encontrar, para todo par de vértices $u, v \in V$, um caminho de peso mínimo de $u$ até $v$. \pause

Como resolver esse problema?


## Introdução

Podemos resolver este problema aplicando um algoritmo de caminho mínimo de única origem $|V|$ vezes, uma vez para cada vértice. \pause

Dijkstra (sem arestas com pesos negativos) \pause

- Arranjo linear: \pause $O(V^3 + VE) = O(V^3)$ \pause

- Heap binário: \pause $O(V E \lg V)$, se o grafo é denso $O(V^3 \lg V)$ \pause

- Heap de Fibonacci: \pause $O(V^2 \lg V + V E)$, se o grafo é denso $O(V^3)$ \pause


Bellman-Ford (grafos gerais) \pause

- $O(V^2E)$, se o grafo é denso $O(V^4)$ \pause


Podemos fazer melhor para o caso geral (grafos com arestas de peso negativo)?


## Considerações

Por conveniência vamos assumir que

- O grafo é representado por matriz de adjacências

- Os vértices são numerados como $1, 2, 3, \dots, n$, onde $n = |V|$

* O grafo não tem ciclos de peso negativos


## Entrada e saída

A entrada é uma matriz $n \times n\ W$ que representa os pesos das arestas. Isto é, $W = \left ( w_{ij} \right )$, onde
$$w_{ij} = \begin{cases}
    0 & \text{ se } i = j \\
    \text{o peso da aresta } (i, j) & \text{ se } i \not = j \text{ e } (i,j) \in E\\
    \infty & \text{ se } i \not = j \text{ e } (i,j) \not \in E\\
\end{cases}$$

\pause

E a saída? \pause

- Uma matriz $n \times n\ D = \left ( d_{ij} \right )$, onde a entrada $d_{ij}$ contém o peso do caminho mínimo do vértice $i$ até o vértice $j$, ou seja, $d_{ij} = \delta(i, j)$;

- Uma matriz $n \times n\ \Pi = \left ( \pi_{ij} \right )$, onde $\pi_{ij}$ é o vértice predecessor de $j$ em um caminho mínimo a partir de $i$.


## Modelo de PD

Vamos tentar usar o modelo de programação dinâmica que desenvolvemos para o problema de caminhos mínimos de única origem. \pause

A ideia é descrever caminhos mínimos com até $k$ arestas em termos de caminhos mínimos com até $k - 1$ arestas.


## Modelo de programação dinâmica

**Caminhos mínimos de única origem**

$\delta^k(s, v)$ -- peso do caminho mínimo da origem $s$ para $v$ que utiliza até $k$ arestas
$$\delta^k(s, v) =
\begin{cases}
  0 & \text{se $s = v$ e $k = 0$} \\
  \infty & \text{se $s \not = v$ e $k = 0$} \\
  \min \begin{cases}
    \delta^{k-1}(s, v) \\
    \min\limits_{(u, v) \in E}(\delta^{k-1}(s, u) + w(u, v))
  \end{cases} & \text{caso contrário}
\end{cases}$$


## Modelo de programação dinâmica

\small

**Caminhos mínimos de todos os pares**

Como a entrada e saída são matrizes, vamos mudar um pouco a notação. \pause

$\delta^k_{ij}$ -- peso do caminho mínimo de $i$ para $j$ que utiliza até $k$ arestas

<div class="columns">
<div class="column" width="60%">
$$\delta^k_{ij} =
\begin{cases}
  0 & \text{se $i = j$ e $k = 0$ } \\
  \infty & \text{se $i \not = j$ e $k = 0$ } \\
  \min \begin{cases}
    \delta^{k-1}_{ij} \\
    \min\limits_{1 \le u \le n}(\delta^{k-1}_{iu} + w_{uj})
  \end{cases} & \text{caso contrário}
\end{cases}$$

\pause

Podemos simplificar a equação? \pause Sim! \pause \vspace{-1em}

- $\delta^1_{ij} = w_{ij}$; e
- $w_{ii} = 0$ para todo $i$.

\pause
</div>
<div class="column" width="40%">
$$\delta^k_{ij} =
\begin{cases}
  w_{ij} & \text{se $k = 1$ } \\
  \min\limits_{1 \le u \le n}(\delta^{k-1}_{iu} + w_{uj}) & \text{se $k > 1$}
\end{cases}$$
</div>
</div>


## Modelo de programação dinâmica

<div class="columns">
<div class="column" width="45%">
\small

$$\delta^k_{ij} =
\begin{cases}
  w_{ij} & \text{se $k = 1$ } \\
  \min\limits_{1 \le u \le n}(\delta^{k-1}_{iu} + w_{uj}) & \text{se $k > 1$}
\end{cases}$$

Qual o tempo de execução do algoritmo que implementa essa equação diretamente? \pause
Vamos escrever o algoritmo e verificar!
</div>
<div class="column" width="55%">

\small

\pause

\begin{codebox}
    \Procname{$\proc{Alg}(W)$}
    \li $n$ = $\attrib{W}{linhas}$
    \li $D^{1} = \left ( d_{ij}^1 = w_{ij} \right )$ uma matriz $n \times n$.
    \li \For $k \gets 2$ \To $n - 1$ \Do
    \li   Seja $D^{k} = \left ( d_{ij}^{k} \right )$ uma matriz $n \times n$
    \li     \For $i \gets 1$ \To $n$ \Do
    \li       \For $j \gets 1$ \To $n$ \Do
    \li         $d_{ij}^k \gets \infty$
    \li         \For $u \gets 1$ \To $n$ \Do
    \li             $d_{ij}^{k} = \min(d_{ij}^{k}, d_{iu}^{k-1} + w_{uj})$
                \End
              \End
            \End
        \End
    \li \Return $D^{n - 1}$
\end{codebox}


\pause

Qual o tempo de execução? \pause $\Theta(V^4)$, o mesmo que executar \proc{Bellman-Ford} para cada vértice!
</div>
</div>


## Algoritmo Baseado em multiplicação de matrizes

A forma do código da iteração que calcula $D^k$ a partir de $D^{k-1}$ é semelhante a forma da multiplicação das matrizes $D^{k-1} \cdot W$. \pause Se usarmos a notação $D^{k-1} \cdot W$ para representar o cálculo de $D^k$ a partir de $D^{k-1}$ e $W$, podemos escrever: \pause \vspace{-1em}

$$\begin{aligned}
D^1 &= W \pause \\
D^2 &= D^1 \cdot W = W^2 \pause \\
D^3 &= D^2 \cdot W = W^3 \pause \\
\dots &  \\
D^{n-1} &= D^{n-2} \cdot W = W^{n - 1} \pause
\end{aligned}$$

Qual o resultado obtemos se fizermos $D^{n - 1} \cdot W$? \pause Se o grafo não tem ciclos de peso negativo, obtemos a própria matriz $D^{n-1}$. \pause

Será que podemos "acelerar" o cálculo de $D^{n - 1}$? \pause Sim!


## Algoritmo Baseado em multiplicação de matrizes

Repetição do quadrado

$$\begin{aligned}
D^1 \cdot D^1 &= D^2 \\
D^2 \cdot D^2 &= D^4 \\
D^4 \cdot D^4 &= D^8 \\
\dots &
\end{aligned}$$

\pause

Quantas vezes precisamos repetir o quadrado para chegar em $D^m$, onde $m \ge n - 1$? \pause $\Theta(\lg V)$ vezes. \pause

Então, podemos calcular $D^{n - 1}$ a partir de $D^1$ no tempo $\Theta(V^3 \lg V)$. \pause

Uma boa melhora! \pause Mas será que podemos fazer melhor? \pause Vamos tentar uma outra modelagem de programação dinâmica.


## Vértice intermediário

Para um caminho $p = \langle v_1, v_2, \dots, v_l \rangle$, um **vértice intermediário** é qualquer vértice de $p$ que não seja $v_1$ ou $v_l$. \pause

Vamos usar o conceito de vértice intermediário para formular a estrutura ótima de caminhos mínimos.

<!-- TODO: Quais são os subproblemas? -->


## Caracterização da estrutura da solução ótima

Considere um caminho mínimo $i \stackrel{p}{\leadsto} j$ com todos os vértices intermediários em $\{1, 2, \dots, k\}$, o vértice $k$ é um vértice intermediário de $p$? \pause

Ele pode ou não ser, então vamos analisar as duas possibilidades.


## Caracterização da estrutura da solução ótima

Se $k$ não é um vértice intermediário de $p$, então, todos os vértices intermediários de $p$ estão em $\{1, 2, \dots, k - 1\}$. \pause Deste modo, um caminho mínimo $i \leadsto j$ com todo os vértices intermediários no conjunto $\{1, 2, \dots, k - 1\}$, também é um caminho mínimo $i \leadsto j$ com todos os vértices intermediários no conjunto $\{1, 2, \dots, k\}$.


## Caracterização da estrutura da solução ótima

Se $k$ é um vértice intermediário do caminho $p$, então desmembramos o caminho $p$ em $i \stackrel{p_1}{\leadsto} k \stackrel{p_2}{\leadsto} j$.  $p_1$ é um caminho mínimo de $i$ até $k$, com todos os vértices intermediários no conjunto $\{1, 2, \dots, k - 1\}$. A mesma ideia se aplica a $p_2$

![](imagens/Fig-25-3.pdf){width=10cm}


## Definição recursiva do custo da solução ótima

Seja $D^{(k)} = \left (d_{ij}^{(k)} \right )$ uma matriz, onde $d_{ij}^{(k)}$ o peso de um caminho mínimo $i \leadsto j$ com todos os vértices intermediários em $\{1, 2, \dots, k\}$ \pause

$$d_{ij}^{(k)} = \begin{cases}
  w_{ij} & \text{se } k = 0 \\
  \min(d_{ij}^{(k-1)}, d_{ik}^{(k - 1)} + d_{kj}^{(k - 1)})) & \text{se } k \ge 1
\end{cases}$$

\pause

Observe que a matriz $D^{(n)}$ fornece a reposta desejada:  $d_{ij}^{(n)} = \delta(i, j)$ para todo $i, j \in V$, isto porque para qualquer caminho mínimo todos os vértices intermediários estão no conjunto $\{1, 2, \dots, n\}$.


## O algoritmo de Floyd-Warshall

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
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
**Análise do tempo de execução**
\pause

- Cada execução da linha 7 demora $O(1)$

- A linha 7 é executada $n^3$ vezes

- Portanto, o tempo de execução do algoritmo é $\Theta(n^3) = \Theta(V^3)$
</div>
</div>


## Exemplo de execução

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
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
\includegraphics[trim=0pt 1200pt 1420pt 0pt,clip,height=4.0cm]{imagens/Fig-25-1.pdf}

\pause

\includegraphics[trim=0pt 2898pt 1420pt 0pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}

\pause

\includegraphics[trim=1300pt 2898pt 0pt 0pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
</div>
</div>


## Exemplo de execução

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
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
\includegraphics[trim=0pt 1200pt 1420pt 0pt,clip,height=4.0cm]{imagens/Fig-25-1.pdf}
\includegraphics[trim=0pt 2319pt 1420pt 579pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
\includegraphics[trim=1300pt 2319pt 0pt 579pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
</div>
</div>


## Exemplo de execução

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
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
\includegraphics[trim=0pt 1200pt 1420pt 0pt,clip,height=4.0cm]{imagens/Fig-25-1.pdf}
\includegraphics[trim=0pt 1740pt 1420pt 1158pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
\includegraphics[trim=1300pt 1740pt 0pt 1158pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
</div>
</div>


## Exemplo de execução

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
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
\includegraphics[trim=0pt 1200pt 1420pt 0pt,clip,height=4.0cm]{imagens/Fig-25-1.pdf}
\includegraphics[trim=0pt 1161pt 1420pt 1737pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
\includegraphics[trim=1300pt 1161pt 0pt 1737pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
</div>
</div>


## Exemplo de execução

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
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
\includegraphics[trim=0pt 1200pt 1420pt 0pt,clip,height=4.0cm]{imagens/Fig-25-1.pdf}
\includegraphics[trim=0pt 582pt 1420pt 2316pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
\includegraphics[trim=1300pt 582pt 0pt 2316pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
</div>
</div>


## Exemplo de execução

<div class="columns">
<div class="column" width="60%">
\small
\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
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
\includegraphics[trim=0pt 1200pt 1420pt 0pt,clip,height=4.0cm]{imagens/Fig-25-1.pdf}
\includegraphics[trim=0pt 3pt 1420pt 2895pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
\includegraphics[trim=1300pt 3pt 0pt 2895pt,clip,width=4.5cm]{imagens/Fig-25-4.pdf}
</div>
</div>


## O algoritmo de Floyd-Warshall

Como construir um caminho mínimo? \pause

- Calcular a matriz predecessora $\Pi$, durante o calculo da matriz de distância de caminhos mínimos $D$ \pause

- Quando $k = 0$, um caminho mínimo de $i$ até $j$ não tem nenhum vértice intermediário, então \pause
  $$\pi_{ij}^{(0)} = \begin{cases}
    \text{\const{Nil}} & \text{se } i = j \text{ ou } w_{ij} = \infty\\
    i          & \text{se } i \not = j \text{ e } w_{ij} < \infty
  \end{cases}$$ \pause

- Quando $k \ge 1$ \pause
  $$\pi_{ij}^{(k)} = \begin{cases}
    \pi_{ij}^{(k-1)} & \text{se } d_{ij}^{(k-1)} \le d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\\
    \pi_{kj}^{(k-1)} & \text{se } d_{ij}^{(k-1)} > d_{ik}^{(k-1)} + d_{kj}^{(k-1)}
  \end{cases}$$


## O algoritmo de Floyd-Warshall

Considerando o exercício 25.2-4 e acrescentando o calculo de $\Pi$, podemos reescrever o procedimento \proc{Floyd-Warshall}


## O algoritmo de Floyd-Warshall

\footnotesize

\begin{codebox}
    \Procname{$\proc{Floyd-Warshall}(W)$}
    \li $n = \attrib{W}{linhas}$
    \li $D = W$
    \li $\Pi = \left ( \pi_{ij} \right )$ uma matriz $n \times n$
    \li \For $i = 1$ \To $n$ \Do
    \li     \For $j = 1$ \To $n$ \Do
    \li         \If $i = j$ ou $w_{ij} = \infty$ \Then
    \li             $\pi_{ij} = \const{nil}$
    \li         \Else
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


## Referências

Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 25.
