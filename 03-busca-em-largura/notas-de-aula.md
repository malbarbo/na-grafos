---
# vim: set spell spelllang=pt_br:
title: Busca em largura
---

## Introdução

- Dado um grafo $G = (V, E)$ e um vértice de origem $s$, a **busca em largura**
  (_Breadth-first search_ - BFS, em inglês) explora sistematicamente as arestas
  de $G$ até descobrir cada vértice acessível a partir de $s$

    - Calcula a distância (menor número de arestas) de $s$ até todos os
      vértices acessíveis a partir de $s$

    - Produz uma árvore de busca em largura

    - É a base para outros algoritmos


## Introdução

- Recebe este nome porque expande a fronteira entre vértices descobertos e não
  descobertos uniformemente ao longo da extensão da fronteira. Descobre todos
  os vértices de distância $k$ de $s$ antes de descobrir quaisquer vértices de
  distância $k + 1$


## Introdução

- Durante a execução do algoritmo, diversos atributos nos vértices são utilizados

  - Cor ($\id{cor}$): cada vértice inicialmente é branco. Quando um vértice
    é **descoberto** (encontrado pela primeira vez na busca) ele é colorido de
    cinza. Quando a lista de adjacências de um vértice é totalmente explorada,
    o vértice é colorido de preto.

  - Pai ($\pi$): quando um vértice $v$ é descoberto através da aresta $(u, v)$,
    dizemos que o vértice $u$ é **predecessor** ou **pai** de $v$. O atributo
    $\pi$ é utilizado para armazenar o predecessor de cada vértice.

  - Distância ($d$): a distância em relação ao vértice inicial da busca.


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


## Procedimento $\proc{BFS}$

<div class="columns">
<div class="column" width="30%">

\scriptsize

\begin{codebox}
  \Procname{$\proc{BFS(G, s)}$}
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

Tempo de execução \pause

- O teste da linha 13 garante que cada vértice é colocado na fila no máximo uma
  vez, e portanto, é retirado da fila no máximo uma vez

- As operações de colocar e retirar da fila tem tempo $O(1)$, assim, o tempo
  total das operações com filas é $O(V)$

- A lista de adjacência de cada vértice é examinada apenas quando o vértice
  é retirado da fila, desta forma, no máximo uma vez

- Como a soma dos comprimentos das listas de adjacências é $\Theta(E)$, o tempo
  para percorrer todas as listas é no máximo $O(E)$

- O tempo de inicialização é $O(V)$

- Tempo total de execução do $\proc{BFS}$ é $O(V + E)$
</div>
</div>


## Corretude

- Afirmamos no início dos slides que o procedimento $\proc{BFS}$ encontra as
  distâncias de $s$ para todos os vértices acessíveis a partir de $s$. Vamos
  ver porque isto é verdade.

- Definimos como a **distância do menor caminho** $\delta(s, v)$ de $s$ para
  $v$ como o número mínimo de arestas de qualquer caminho de $s$ para $v$, se
  não existe caminho de $s$ para $v$ então $\delta(s, v) = \infty$.

- Precisamos mostrar que o valor $\attrib{v}{d}$ de cada vértice do grafo,
  produzido pela chamada $\proc{BFS}(G, s)$, é igual a $\delta(s, v)$.


## Corretude

Seja $G = (V, E)$ um grafo orientado ou não orientado e $s \in V$ um vértice
arbitrário

### Lema 22.1

Se $(u, v) \in E$ , então \newline
$\delta(s, v) \le \delta(s, u) + 1$ \pause

### Lema 22.2

Se $\proc{BFS}(G, s)$ é executado, então após a execução \newline
$v.d \ge \delta(s, v)$ para todo vértice $v \in V$


## Corretude

### Lema 22.3

Se em um determinado momento da execução de $\proc{BFS}(G, s)$ a fila $Q$
contém $\langle v_1, v_2, \dots, v_r \rangle$, então

- $\attrib{v_r}{d} \le \attrib{v_1}{d} + 1$; e
- $\attrib{v_i}{d} \le \attrib{v_{i+1}}{d}$ para $i = 1, 2, \dots, r - 1$ \pause

### Corolário 22.4

Se $v_i$ é inserido antes de $v_j$ na fila durante a execução do \proc{BFS},
então \newline
$\attrib{v_i}{d} \le \attrib{v_j}{d}$ no momento que $v_j$ é inserido na fila


## Corretude

### Teorema 22.5 - Corretude do \proc{BFS}

Durante a execução do $\proc{BFS}(G, s)$, todos os vértices acessíveis a partir
de $s$ são descobertos, e depois do término da execução $\attrib{v}{d}
= \delta(s, v)$ para todo $v \in V$. \pause

Demostração feito em sala. Veja as referências para detalhes.



## Árvore de busca em largura

- \proc{BFS} constrói uma árvore de busca em largura

- A árvore é definida pelo campo pai ($\pi$) em cada vértice

- Para um grafo $G=(V, E)$ e um vértice de origem $s$, definimos o **subgrafo
  predecessor** de $G$ como $G_\pi=(V_\pi, E_\pi)$ onde

    - $V_\pi = \{v \in V: \attrib{v}{\pi} \neq \const{nil} \} \cup \{ s \}$
      (vértices acessíveis a partir de $s$)

    - $E_\pi = \{(\attrib{v}{\pi}, v): v \in V_\pi - \{s\}\}$ (arestas que
      conectam os vértices acessíveis a partir de $s$ - com exceção do próprio
      $s$ - ao pai)


## Árvore de busca em largura

- O subgrafo predecessor $G_\pi$ é uma árvore de busca em largura

    - $V_\pi$ consiste nos vértices acessíveis a partir de $s$

    - Para todo $v \in V_\pi$, existe um caminho único simples desde $s$ até
      $v$ em $G_\pi$, que também é um caminho mais curto de $s$ até $v$ em $G$

- Uma árvore de busca em largura é de fato uma árvore, pois é conexa e $|E_\pi| = |V_\pi| - 1$


## Árvore de busca em largura

Como exibir o caminho de $s$ para $v$? \pause

\begin{codebox}
  \Procname{$\proc{print-path(G, s, v)}$}
  \li \If $v \isequal s$ \Then
  \li   \proc{print} $s$
  \li \ElseIf $\attrib{v}{\pi} \isequal \const{nil}$ \Then
  \li   \proc{print} ``não existe nenhum caminho de'' $s$ para $v$
  \li \Else
  \li   $\proc{print-path}(G, s, \attrib{v}{\pi})$
  \li   \proc{print} $v$
      \End
\end{codebox}

\pause

Executado em tempo \pause linear no número de vértices no caminho impresso,
pois cada chamada recursiva é feita para um caminho com um vértice menor que
o atual


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.2.

- [Rascunho da prova de corretude do BFS](http://www.cs.toronto.edu/~krueger/csc263h/lectures/BFS.pdf)
