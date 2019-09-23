---
# vim: set spell spelllang=pt_br:
title: Busca em largura
---

## Introdução

- Dado um grafo $G = (V, E)$ e um vértice de origem $s$, a busca em largura
  explora sistematicamente as arestas de $G$ até descobrir cada vértice
  acessível a partir de $s$

    - Produz uma árvore de busca em largura

    - Calcula a distância (menor número de arestas) de $s$ até todos os
      vértices acessíveis a partir de $s$

- Recebe este nome porque expande a fronteira entre vértices descobertos e não
  descobertos uniformemente ao longo da extensão da fronteira. Descobre todos
  os vértices de distância $k$ de $s$ antes de descobrir quaisquer vértices de
  distância $k + 1$


## Exemplo de execução

<!-- Gerado com o comando bin/split-image clrs/Chapter\ 22/Fig-22-3.pdf 1500 470 5 2 height=2.5cm !-->

\includegraphics[trim=0pt 2259pt 1807pt 0pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=1807pt 2259pt 0pt 0pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=0pt 1695pt 1807pt 564pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=1807pt 1695pt 0pt 564pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=0pt 1131pt 1807pt 1128pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=1807pt 1131pt 0pt 1128pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=0pt 567pt 1807pt 1692pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=1807pt 567pt 0pt 1692pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exemplo de execução

\includegraphics[trim=0pt 3pt 1807pt 2256pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Procedimento $\proc{bfs}$

<div class="columns">
<div class="column" width="30%">

\scriptsize

\begin{codebox}
  \Procname{$\proc{bfs(G, s)}$}
  \li \For $v \in \attrib{G}{V} - \{ s \}$ \Do
  \li   $\attrib{v}{d} \gets \infty$
  \li   $\attrib{v}{\pi} \gets \const{nil}$
  \li   $\attrib{v}{cor} \gets \const{branco}$
      \End
  \li $\attrib{s}{d} \gets 0$
  \li $\attrib{s}{\pi} \gets \const{nil}$
  \li $\attrib{s}{cor} \gets \const{cinza}$
  \li $Q \gets \emptyset$
  \li $\proc{Enqueue}(Q, s)$
  \li \While $Q \not = \emptyset$ \Do
  \li   $u \gets \proc{Dequeue}(Q)$
  \li   \For $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li       $\attrib{v}{d} \gets \attrib{u}{d} + 1$
  \li       $\attrib{v}{\pi} \gets u$
  \li       $\attrib{v}{cor} \gets \const{cinza}$
  \li       $\proc{Enqueue}(Q, v)$
          \End
        \End
  \li   $\attrib{u}{\id{cor}} \gets \const{preto}$
      \End
\end{codebox}

</div>

<div class="column" width="70%">

\footnotesize

\pause

Análise agregada \pause

- O teste da linha 13 garante que cada vértice é colocado na fila no máximo uma
  vez, e portanto, é retirado da fila no máximo uma vez

- As operações de colocar e retirar da fila demoram $O(1)$, assim, o tempo
  total das operações com filas é $O(V)$

- A lista de adjacência de cada vértice é examinada apenas quando o vértice
  é retirado da fila, desta forma, no máximo uma vez

- Como a soma dos comprimentos das listas de adjacências é $\Theta(E)$, o tempo
  para percorrer todas as listas é no máximo $O(E)$

- O tempo de inicialização é $O(V)$

- Tempo total de execução do $\proc{bfs}$ é $O(V + E)$
</div>
</div>


## Árvore de busca em largura

- \proc{bfs} constrói uma árvore de busca em largura

- A árvore é definida pelo campo pai ($\pi$) em cada vértice

- Para um grafo $G=(V, E)$ e um vértice de origem $s$, definimos o **subgrafo
  predecessor** de $G$ como $G_\pi=(V_\pi, E_\pi)$ onde

    - $V_\pi = \{v \in V: \attrib{v}{\pi} \neq \const{nil} \} \cup \{ s \}$

    - $E_\pi = \{(\attrib{v}{\pi}, v): v \in V_\pi - \{s\}\}$


## Árvore de busca em largura

- O subgrafo predecessor $G_\pi$ é uma árvore de busca em largura

    - $V_\pi$ consiste nos vértices acessíveis a partir de $s$

    - Para todo $v \in V_\pi$, existe um caminho único simples desde $s$ até
      $v$ em $G_\pi$, que também é um caminho mais curto de $s$ até $v$ em $G$

- Uma árvore primeiro na extensão é de fato uma árvore, pois é conexa e
    $|E_\pi| = |V_\pi| - 1$


## Árvore de busca em largura

\begin{codebox}
  \Procname{$\proc{print-path(G, s, v)}$}
  \li \If $v \isequal s$ \Then
  \li   \proc{print} $s$
  \li \ElseIf $\attrib{v}{\pi} \isequal \const{nil}$ \Then
  \li   \proc{print} "não existe nenhum caminho de" $s$ para $v$
  \li \Else
  \li   $\proc{print-path}(G, s, \attrib{v}{\pi})$
  \li   \proc{print} $v$
      \End
\end{codebox}

- Executado em tempo \pause linear no número de vértices no caminho impresso,
  pois cada chamada recursiva é feita para um caminho com um vértice menor que
  o atual


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.2.
