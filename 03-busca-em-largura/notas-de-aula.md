---
# vim: set spell spelllang=pt_br:
title: Busca em largura
---

## Introdução

Dado um grafo $G = (V, E)$ e um vértice de origem $s$, a **busca em largura** (_Breadth-first search_ - BFS, em inglês) explora sistematicamente as arestas de $G$ até descobrir cada vértice acessível a partir de $s$. \pause

- Calcula a distância mínima (menor número de arestas) de $s$ até todos os vértices acessíveis a partir de $s$ \pause

- Produz uma árvore de busca em largura \pause

- É a base para outros algoritmos \pause

- Funciona para grafos orientados e não orientados


## Introdução

Recebe este nome porque expande a fronteira entre vértices descobertos e não descobertos uniformemente ao longo da extensão da fronteira. Descobre todos os vértices de distância $k$ de $s$ antes de descobrir quaisquer vértices de distância $k + 1$.


## Introdução

Durante a execução do algoritmo, diversos atributos nos vértices são utilizados

- Cor ($\id{cor}$): cada vértice inicialmente é branco. Quando um vértice é **descoberto** (encontrado pela primeira vez na busca) ele é colorido de cinza. Quando a lista de adjacências de um vértice é totalmente explorada, o vértice é colorido de preto.

- Pai ($\pi$): quando um vértice $v$ é descoberto através da aresta $(u, v)$, dizemos que o vértice $u$ é **predecessor** ou **pai** de $v$. O atributo $\pi$ é utilizado para armazenar o predecessor de cada vértice.

- Distância ($d$): a distância mínima em relação ao vértice inicial.


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

Baseado nesta ideia de funcionamento, vamos escrever o algoritmo BFS. Vamos assumir que o grafo de entrada é representado por uma lista de adjacências. \pause

Nós construímos em sala o algoritmo "do zero". Como exercício, tente escrever novamente o algoritmo, mas desta vez sozinho!


## Procedimento $\proc{BFS}$

<div class="columns">
<div class="column" width="30%">

\scriptsize

\begin{codebox}
  \Procname{$\proc{BFS(G, s)}$}
  \li \For each vertex $v \in \attrib{G}{V} - \{ s \}$ \Do
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
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li       $\attrib{v}{cor} \gets \const{cinza}$
  \li       $\attrib{v}{d} \gets \attrib{u}{d} + 1$
  \li       $\attrib{v}{\pi} \gets u$
  \li       $\proc{Enqueue}(Q, v)$
          \End
        \End
  \li   $\attrib{u}{\id{cor}} \gets \const{preto}$
      \End
\end{codebox}

</div>

<div class="column" width="70%">

\small

\pause

**Tempo de execução** \pause

- O teste da linha 13 garante que cada vértice é colocado na fila no máximo uma vez, e portanto, é retirado da fila no máximo uma vez

- As operações de colocar e retirar da fila tem tempo $O(1)$, assim, o tempo total das operações com filas é $O(V)$

- A lista de adjacência de cada vértice é examinada apenas quando o vértice é retirado da fila, desta forma, no máximo uma vez

- Como a soma dos comprimentos das listas de adjacências é $\Theta(E)$, o tempo para percorrer todas as listas é no máximo $O(E)$

- O tempo de inicialização é $O(V)$

- Tempo total de execução do $\proc{BFS}$ é $O(V + E)$
</div>
</div>


## Corretude

Afirmamos no início dos slides que o procedimento $\proc{BFS}$ encontra as distâncias mínimas de $s$ para todos os vértices acessíveis a partir de $s$. Vamos ver porque isto é verdade. \pause

Definimos como a **distância do caminho mínimo** $\delta(s, v)$ de $s$ para $v$ como o número mínimo de arestas de qualquer caminho de $s$ para $v$, se não existe caminho de $s$ para $v$ então $\delta(s, v) = \infty$. \pause

Chamamos um caminho de comprimento $\delta(s, v)$ entre $s$ e $v$ de **caminho mínimo**.


## Uma propriedade de distâncias de menores caminhos

Seja $G = (V, E)$ um grafo orientado ou não orientado e $s \in V$ um vértice arbitrário. \pause

### Lema 22.1

Se $(u, v) \in E$ , então $\delta(s, v) \le \delta(s, u) + 1$. \pause


### Prova

$u$ é acessível a partir de $s$? \pause

- Se sim, então $v$ também é. \pause Além disso, o menor caminho entre $s$ e $v$ não pode ser maior que o menor caminho de $s$ para $u$ seguido de $(u, v)$, \pause então a desigual se mantém. \pause

- Se não, $\delta(s, u) = \pause \infty$ e a desigualdade se mantém. \pause $\qed$

\pause


Note que está é uma propriedade da definição de menor caminho e não do algoritmo em si.


## Corretude

Precisamos mostrar que o valor $\attrib{v}{d}$ de cada vértice do grafo, produzido pela chamada $\proc{BFS}(G, s)$, é igual a $\delta(s, v)$. \pause

Vamos começar mostrando um limite inferior para $\attrib{v}{d}$.


### Lema 22.2

Se $\proc{BFS}(G, s)$ é executado, então após a execução \newline
$v.d \ge \delta(s, v)$ para todo vértice $v \in V$.


## Corretude

<div class="columns">
<div class="column" width="33%">

\scriptsize

\begin{codebox}
  \Procname{$\proc{BFS(G, s)}$}
  \li \For each vertex $v \in \attrib{G}{V} - \{ s \}$ \Do
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
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li       $\attrib{v}{cor} \gets \const{cinza}$
  \li       $\attrib{v}{d} \gets \attrib{u}{d} + 1$
  \li       $\attrib{v}{\pi} \gets u$
  \li       $\proc{Enqueue}(Q, v)$
          \End
        \End
  \li   $\attrib{u}{\id{cor}} \gets \const{preto}$
      \End
\end{codebox}

</div>

<div class="column" width="67%">

\footnotesize

**Prova**

Vamos usar indução no número de operações \proc{Enqueue}. \pause A nossa hipótese de indução é que $\attrib{v}{d} \ge \delta(s, v)$ para todo $v \in V$. \pause

Base (imediatamente após a linha 9) \pause \vspace{-1em}

- Para o vértice inicial $s$, temos $\attrib{s}{d} = \pause 0 = \delta(s, s)$ \pause. Para todos os vértices $v \in V - \{ s \}$, temos $\attrib{v}{d} = \pause \infty \ge \delta(s, v)$, então a hipótese é verdadeira. \pause

Passo de indução \vspace{-1em}

- Considere um vértice branco $v$ que é descoberto a partir de um vértice $u$ \pause
- Pela hipótese de indução $\attrib{u}{d} \ge \delta(s, u)$ \pause
- Pela linha 15, temos $\attrib{v}{d} = \attrib{u}{d} + 1$ \pause, logo $\attrib{v}{d} \ge \delta(s, u) + 1$ \pause
- Como pelo lema 22.1 $\delta(s, u) + 1 \ge \delta(s, v)$ \pause, então $\attrib{v}{d} \ge \delta(s, v)$ \pause
- Como a cor de $v$ é alterado para \const{cinza} as linhas de 14-17 não serão mais executadas para $v$ e a sua distância não será mais alterada, portando a hipótese de indução se mantém. $\qed$

</div>
</div>


## Corretude

### Lema 22.3

Se em um determinado momento da execução de $\proc{BFS}(G, s)$ a fila $Q$ contém $\langle v_1, v_2, \dots, v_r \rangle$, então

- $\attrib{v_r}{d} \le \attrib{v_1}{d} + 1$; e
- $\attrib{v_i}{d} \le \attrib{v_{i+1}}{d}$ para $i = 1, 2, \dots, r - 1$ \pause

### Prova

Indução no número de operações com a fila. \pause

Exercício: leia a prova no livro (tente entender frase por frase, se está difícil entender uma afirmação, tente ver a afirmação como pergunta)


## Corretude

### Corolário 22.4

Se $v_i$ é inserido antes de $v_j$ na fila durante a execução do \proc{BFS}, então \newline
$\attrib{v_i}{d} \le \attrib{v_j}{d}$ no momento que $v_j$ é inserido na fila. \pause

### Prova

Direto do Lema 22.3 e do fato que cada vértice tem o valor de $d$ atribuído no máximo uma vez.




## Corretude

### Teorema 22.5 - Corretude do \proc{BFS}

Durante a execução do $\proc{BFS}(G, s)$, todos os vértices acessíveis a partir de $s$ são descobertos, e depois do término da execução $\attrib{v}{d} = \delta(s, v)$ para todo $v \in V$. \pause


### Prova

Por contradição.


## Corretude

<div class="columns">
<div class="column" width="35%">

\scriptsize

\begin{codebox}
  \Procname{$\proc{BFS(G, s)}$}
  \li \For each vertex $v \in \attrib{G}{V} - \{ s \}$ \Do
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
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li       $\attrib{v}{cor} \gets \const{cinza}$
  \li       $\attrib{v}{d} \gets \attrib{u}{d} + 1$
  \li       $\attrib{v}{\pi} \gets u$
  \li       $\proc{Enqueue}(Q, v)$
          \End
        \End
  \li   $\attrib{u}{\id{cor}} \gets \const{preto}$
      \End
\end{codebox}

</div>

<div class="column" width="65%">

\footnotesize

Vamos assumir, com o propósito de contradição, que algum vértice $v$ receba um $d$ diferente de $\delta(s, v)$. \pause Seja $v$ o vértice com o menor $\delta(s, v)$ que recebeu o $d$ incorreto. \pause \vspace{-1em}

- O vértice $v$ pode ser igual a $s$? \pause Não, pois o valor $\attrib{s}{d} = 0$ está correto.
- O vértice $v$ é acessível a partir de $s$? \pause Sim, porque senão o algoritmo teria determinado que $\attrib{v}{d} = \infty$ que é $\delta(s, v)$ e portanto está correto. \pause
- Sabendo que $v$ é acessível a partir de $s$ e $v \not = s$, seja $u$ o vértice predecessor de $v$ em um menor caminho de $s$ para $v$. \pause Temos que $\delta(s, v) = \delta(s, u) + 1$. \pause
- O algoritmo calculou $\attrib{u}{d}$ corretamente, isto é, $\attrib{u}{d} = \delta(s, u)$? \pause Sim, pois $\delta(s, u) < \delta(s, v)$ e $v$ é o vértice com menor $\delta$ que recebeu $d$ incorreto. \pause
- Do Lema 22.2 sabemos que $\attrib{v}{d} \ge \delta(s, v)$. Será que $\attrib{v}{d}$ pode ser igual a $\delta(s, v)$? \pause Não! Logo $\attrib{v}{d} > \delta(s, v)$. \pause
- Juntando estas propriedades temos $\attrib{v}{d} > \delta(s, v) = \delta(s, u) + 1 = \attrib{u}{d} + 1$

</div>
</div>


## Corretude

<div class="columns">
<div class="column" width="35%">

\scriptsize

\begin{codebox}
  \Procname{$\proc{BFS(G, s)}$}
  \li \For each vertex $v \in \attrib{G}{V} - \{ s \}$ \Do
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
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li       $\attrib{v}{cor} \gets \const{cinza}$
  \li       $\attrib{v}{d} \gets \attrib{u}{d} + 1$
  \li       $\attrib{v}{\pi} \gets u$
  \li       $\proc{Enqueue}(Q, v)$
          \End
        \End
  \li   $\attrib{u}{\id{cor}} \gets \const{preto}$
      \End
\end{codebox}

</div>

<div class="column" width="65%">

\footnotesize

Sabendo que $\attrib{v}{d} > \attrib{u}{d} + 1$ (Eq 22.1), vamos analisar o momento em que o BFS retira $u$ da fila (linha 11). \pause Nesse momento o vértice $v$ pode ser \const{branco}, \const{cinza} ou \const{preto}. Vamos mostrar que em cada um desses casos nos derivamos uma contradição para a equação 22.1. \pause \vspace{-1em}

- Se $v$ é \const{branco}, qual é o valor que o BFS atribui para $\attrib{v}{d}$? \pause O valor $\attrib{u}{d} + 1$ (linha 15), que contradiz a Eq 22.1. \pause
- Se $v$ é \const{preto} então ele já foi removido da fila, como $\attrib{v}{d}$ se compara com $\attrib{u}{d}$? \pause Pelo Corolário 22.4 $\attrib{v}{d} \le \attrib{u}{d}$, contrariando a Eq 22.1. \pause
- Se $v$ é \const{cinza}, então ele foi pintado de cinza quando um vértice $w$ estava sendo explorado e $\attrib{v}{d} = \attrib{w}{d} + 1$. $w$ foi removido antes de $u$ da fila? \pause Sim, \pause e portanto, pelo Corolário 22.4, $\attrib{w}{d} \le \attrib{u}{d}$. \pause
- Logo $\attrib{v}{d} = \attrib{w}{d} + 1 \le \attrib{u}{d} + 1$, mais uma vez um contradição com a Eq 22.1. \pause

Então não pode existir um vértice $v$ cujo o $d$ foi calculado incorretamente, portanto concluímos que $\attrib{v}{d} = \delta(s, v)$ para todo $v \in V$. $\qed$

</div>
</div>


## Árvore de busca em largura

\proc{BFS} constrói uma árvore de busca em largura.

A árvore é definida pelo campo pai ($\pi$) em cada vértice.

Para um grafo $G=(V, E)$ e um vértice de origem $s$, definimos o **subgrafo predecessor** de $G$ como $G_\pi=(V_\pi, E_\pi)$ onde

- $V_\pi = \{v \in V: \attrib{v}{\pi} \neq \const{nil} \} \cup \{ s \}$ (vértices acessíveis a partir de $s$)

- $E_\pi = \{(\attrib{v}{\pi}, v): v \in V_\pi - \{s\}\}$ (arestas que  conectam os vértices acessíveis a partir de $s$ - com exceção do próprio $s$ - ao pai)


## Árvore de busca em largura

O subgrafo predecessor $G_\pi$ é uma árvore de busca em largura

- $V_\pi$ consiste nos vértices acessíveis a partir de $s$

- Para todo $v \in V_\pi$, existe um caminho único simples desde $s$ até $v$ em $G_\pi$, que também é um caminho mais curto de $s$ até $v$ em $G$

Uma árvore de busca em largura é de fato uma árvore, pois é conexa e $|E_\pi| = |V_\pi| - 1$


## Árvore de busca em largura

<div class="columns">
<div class="column" width="40%">
\includegraphics[trim=80pt 3pt 2300pt 2256pt,clip,width=4.5cm]{imagens/Fig-22-3.pdf}
\vspace{5cm}

</div>

<div class="column" width="60%">

\small

Como exibir o caminho de $s$ para $v$? \pause

Quais são os casos mais simples? \pause

- $s = v$, qual é a saída? \pause $s$. \pause
- $\attrib{v}{\pi} \isequal \const{nil}$, qual é saída? \pause Indicação que não existem caminho. \pause

E os outros casos? \pause Se tivermos o caminho de $s$ até o predecessor de $v$ (que é $\attrib{v}{\pi}$), então basta adiciona o $v$ no caminho.

</div>
</div>


## Árvore de busca em largura


<div class="columns">
<div class="column" width="40%">
\includegraphics[trim=80pt 3pt 2300pt 2256pt,clip,width=4.5cm]{imagens/Fig-22-3.pdf}


</div>

<div class="column" width="60%">

\small

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

Executado em tempo \pause linear no número de vértices no caminho impresso, pois cada chamada recursiva é feita para um caminho com um vértice menor que o atual.

</div>
</div>

## Exercícios

<div class="columns">
<div class="column" width="35%">

\scriptsize

\begin{codebox}
  \Procname{$\proc{BFS(G, s)}$}
  \li \For each vertex $v \in \attrib{G}{V} - \{ s \}$ \Do
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
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li       $\attrib{v}{cor} \gets \const{cinza}$
  \li       $\attrib{v}{d} \gets \attrib{u}{d} + 1$
  \li       $\attrib{v}{\pi} \gets u$
  \li       $\proc{Enqueue}(Q, v)$
          \End
        \End
  \li   $\attrib{u}{\id{cor}} \gets \const{preto}$
      \End
\end{codebox}

</div>

<div class="column" width="65%">

\small

É possível simplificar o BFS de forma que após a sua execução ainda possamos identificar os vértices acessíveis a partir do vértice inicial?\pause

- Podemos remover o cálculo do valor $d$? \pause Sim, o fluxo de execução do algoritmo não depende de $d$. \pause

- Podemos remover o cálculo do valor $\pi$? \pause Sim, o fluxo de execução do algoritmo não depende de $\pi$. \pause

- Podemos remover a linha 18? \pause Sim, o fluxo de execução é determinado por apenas duas situações, vértice branco ou não branco, não é necessário diferenciar entre cinza e preto.

</div>
</div>


## Exercícios

22.2-1 Mostre os valores de $d$ e $\pi$ resultantes da execução da busca em largura no grafo direcionado da Figura 22.2, usando o vértice 3 como inicial.

\includegraphics[trim=0cm 0cm 84cm 0cm,clip,width=3.7cm]{imagens/Fig-22-2.pdf}


## Exercícios

22.2-5 Argumente que em uma busca em largura, o valor de $\attrib{u}{d}$ atribuído para um vértice $u$ é independente da ordem que os vértices aparecem em cada lista de adjacência. Usando a Figura 22.3 como exemplo, mostre que a árvore produzida pelo BFS pode depender da ordem dentro das listas de adjacências.

\includegraphics[trim=80pt 2259pt 2300pt 0pt,clip,height=2.5cm]{imagens/Fig-22-3.pdf}


## Exercícios

Usando como base o BFS, explique como

1) Verificar se um grafo não orientado é conexo.

2) Identificar quantas componentes conexas um grafo não orientado tem.

3) Verificar se um grafo não orientado é bipartido.


Dicas

- Faça diversos exemplos de grafos com e sem as características desejadas e mostre o resultado da execução do BFS neles

- Baseado nesses exemplos, tente identificar aspectos nos resultados que possam ajudar na solução das questões


## Exercícios

Veja a lista completa de exercícios e algumas soluções na página da disciplina.


## Referências

Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.2.

[Rascunho da prova de corretude do BFS](http://www.cs.toronto.edu/~krueger/csc263h/lectures/BFS.pdf).
