---
# vim: set spell spelllang=pt_br:
# TODO: falar da implementação de conjuntos disjuntos
# TODO: falar das implementações das filas de prioridades
title: Árvores geradoras mínimas
---

## Problema

O prefeito de uma cidade decidiu conectar todas as escolas através de uma rede de fibra ótica a internet. \pause Uma das escolas (qualquer uma) servirá como _gateway_, as demais devem ser ligadas a esta escola de alguma forma. \pause

Em um estudo preliminar foi feito um levantamento das possível ligações entre as escolas e determinado o custo de cada ligação. \pause O prefeito quer gastar o mínimo possível e garantir que todas as escolas estejam conectas a internet. \pause Como decidir quais ligações devem ser feitas? \pause

Vamos criar um grafo com estas informações para nos ajudar a entender o problema:

- Cada escola é representada por um vértice

- Cada possível ligação entre as escolas é representada por uma aresta com um valor (custo da ligação)


## Problema

![](imagens/fig-23-1.pdf){width=6cm}

\pause

Fazer apenas a ligação $(i, g)$ conecta todas as escolas? \pause Não!\pause

Fazer apenas as ligações $(i, g)$, $(g, h)$ e $(h, i)$ conecta todas as escolas? \pause Não!


## Solução

![](imagens/Fig-23-1.pdf){width=6cm}

Quais características uma solução deve ter? \pause

- Deve conectar todos os vértices \pause

- Deve ter $|V| - 1$ arestas\pause, ou seja, ser uma árvore \pause

- Ter custo mínimo entre todas as possíveis árvores \pause (pode haver mais que uma) \pause

Uma forma de confirmar que entendemos o problema é fazer uma definição precisa dele. \pause Então vamos fazer isso.


## Problema da árvore geradora mínima

Dado um grafo conexo não orientado $G = (V, E)$ e uma função peso $w: E \rightarrow \mathbb{R}$, queremos encontrar um subconjunto acíclico $T \subseteq E$ que conecte todos os vértices de $G$ e cujo peso total

$$\displaystyle w(T) = \sum_{(u, v) \in T} w(u, v)$$

seja mínimo. \pause

Como $T$ é acíclico e conecta todos os vértices, $T$ forma uma árvore, que chamamos de **árvore geradora mínima** (AGM ou MST em inglês). \pause

No contexto de árvores geradoras, vamos usar $T$ para nos referir tanto ao conjunto de arestas quanto ao subgrafo induzido pelo conjunto de arestas.


## Tipo do problema

Agora que entendemos o problema, vamos construir exemplos e pensar no processo que utilizamos para encontrar as respostas. \pause Conhecer o tipo do problema que estamos lidando pode nos ajudar nesta etapa. \pause


### Tipos de problemas computacionais

\pause

Decisão (sim ou não). \pause Exemplo: Verificar se existe um caminho simples entre dois vértices em um grafo. \pause

Busca (saída arbitrária). \pause Exemplo: Encontrar um caminho simples entre dois vértices em um grafo. \pause

Contagem (número de soluções para um problema de busca). \pause Exemplo: Contar quantos caminhos simples existem entre dois vértices de um grafo. \pause

Otimização (melhor solução entre todas as soluções para um problema de busca). \pause Exemplo: Encontrar um caminho simples com o menor número de arestas entre dois vértices em um grafo.


## Tipo do problema

Que tipo de problema é encontrar uma árvore geradora de custo mínimo? \pause De otimização. \pause

Quais técnicas de projeto de algoritmos são comumente utilizadas para problemas de otimização? \pause

- Algoritmo guloso \pause

- Programação dinâmica \pause

- Melhoramento iterativo \pause

- Etc \pause


Vamos tentar utilizar estas técnicas para derivar hipóteses de algoritmos.


## Ideias de algoritmos

Veja o vídeo da aula para entender como chegamos nessas ideias. \pause

Melhoramento iterativo

- Começar como uma árvore geradora qualquer

- Tentar encontrar uma árvore com custo menor substituindo uma aresta que está na árvore por outra que não está \pause


Algoritmo Guloso 1

- Adicionar arestas na solução (deste que não criem ciclos) em ordem crescente de peso \pause


Algoritmo Guloso 2

- Começar com um vértice na árvore e ir "ligando" novos vértices à árvore usando as arestas de menor peso


## Ideias de algoritmos

A ideia do Algoritmo Guloso 1 foi proposta primeiramente por Kruskal e a a ideia do Algoritmo Guloso 2 por Prim. \pause

As duas abordagens podem ser analisadas usando as mesmas propriedades. \pause Vamos ver como o livro apresenta esta análise.


## Como construir uma árvore geradora mínima?

Construímos uma árvore geradora mínima uma aresta por vez. \pause

Começamos com um conjunto vazio $A$. \pause Em cada iteração determinamos um aresta $(u, v)$ que pode ser adicionada a $A$, de forma a manter a seguinte invariante: \pause

- Antes de cada iteração, $A$ é um subconjunto de alguma árvore geradora mínima. Chamamos a aresta $(u, v)$ de **aresta segura** para $A$. \pause

No final, temos uma árvore geradora mínima!


## Como construir uma árvore geradora mínima

\begin{codebox}
    \Procname{$\proc{Generic-MST}(G, w)$}
    \li $A = \emptyset$
    \li \While $A$ não forma uma árvore geradora \Do
    \li     encontre uma aresta $(u,v)$ que seja segura para $A$
    \li     $A = A \cup \{ (u, v) \}$
        \End
    \li \Return $A$
\end{codebox}

\pause

Agora vamos ver com detalhes como os algoritmo de Krukal e Prim constroem um AGM uma aresta por vez.


## Algoritmo de Kruskal

Baseia-se diretamente no algoritmo genérico

- Inicialmente cada vértice está em sua própria componente (árvore)

- De todas as arestas que conectam duas árvores quaisquer na floresta, uma aresta $(u, v)$ de peso mínimo é escolhida. A aresta $(u, v)$ é segura para alguma das duas árvores (vamos provar isso depois).


## Algoritmo de Kruskal

\includegraphics[trim=0pt 2371pt 1920pt 0pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 2371pt 0pt 0pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=0pt 1581pt 1920pt 790pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 1581pt 0pt 790pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=0pt 791pt 1920pt 1580pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 791pt 0pt 1580pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=0pt 1pt 1920pt 2370pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 1pt 0pt 2370pt,clip,width=9cm]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=10pt 1582pt 1919pt 60pt,clip,width=9cm]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1929pt 1582pt 0pt 60pt,clip,width=9cm]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=10pt 791pt 1919pt 851pt,clip,width=9cm]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1929pt 791pt 0pt 851pt,clip,width=9cm]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=10pt 0pt 1919pt 1642pt,clip,width=9cm]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1929pt 0pt 0pt 1642pt,clip,width=9cm]{imagens/Fig-23-4-R.pdf}


## Algoritmo de Kruskal

Qual é o "desafio" para implementar este algoritmo de forma eficiente? \pause É o gerenciamento das árvores: verificar se dois vértices estão na mesma árvore e juntar duas árvores. \pause

Esta situação é comum em outros contexto e pode ser resolvida com um estrutura de dados para conjuntos disjuntos. \pause Três operações são definidas para este tipo de estrutura: \pause

- \proc{Mark-Set($v$)}, coloca o vértice $v$ no seu próprio conjunto (árvore) \pause

- \proc{Find-Set($v$)}, identifica em qual conjunto o vértice $v$ está \pause

- \proc{Union($u$, $v$)}, junta os vértices do conjunto de $u$ e $v$ em um único conjunto \pause

A seção 21.3 descreve uma implementação bastante eficiente, onde o tempo de execução de $m$ operações em $n$ elementos é $O(m \alpha(n))$, sendo $\alpha$ é uma função que cresce lentamente.


## Algoritmo de Kruskal

Baseado no exemplo de funcionamento e nas operações de conjuntos disjuntos, vamos escrever o pseudo código do algoritmo.

## Algoritmo de Kruskal

<div class="columns">
<div class="column" width="35%">
\begin{codebox}
  \Procname{$\proc{MST-Kruskal}(G, w)$}
  \li $A = \emptyset$
  \li \For each vertex $v \in \attrib{G}{V}$ \Do
  \li   $\proc{make-set(v)}$
      \End
  \li ordenar em ordem não decrescente
  \zi as arestas de $G$ pelo peso $w$
  \li \For each edge $(u, v) \in E^*$ \Do
  \li   \If $\proc{find-set}(u) \not = \proc{find-set}(v)$ \Then
  \li     $A = A \cup \{ (u, v) \}$
  \li     $\proc{union}(u, v)$
        \End
      \End
  \li \Return $A$
\end{codebox}

\* Em ordem não decrescente de peso

</div>
<div class="column" width="65%">
\pause

Análise do tempo de execução

- A ordenação das arestas na linha 4 tem tempo \pause $O(E \lg E)$ \pause

- Operações com conjuntos disjunto

    - O laço das linhas 5 a 8 executa $O(E)$ vezes \proc{find-set} e \proc{union}. Juntamente com as $|V|$ operações \proc{make-set}, elas têm tempo $O((V + E)\alpha(V))$. \pause Pelo fato de $G$ ser conexo, temos que $|E| \ge |V| - 1$ e portanto o tempo com operações com conjuntos disjuntos é $O(E\alpha(V))$ \pause. Além disso, $\alpha(|V|) = O(\lg V) = O(\lg E)$, e portanto o tempo total das operações com conjuntos disjuntos é $O(E\lg E)$. \pause

- Somando o custo de ordenação e o custo das operações com conjuntos disjuntos, temos $O(E \lg E)$. Observando que $|E| < |V^2|$, temos que $\lg |E| = O(\lg V)$, e portanto, o tempo de execução do algoritmo é $O(E \lg V)$.

</div>
</div>


## Algoritmo de Prim

Também baseado diretamente no algoritmo genérico

- Começa com uma árvore com uma raiz arbitrária $r$

- Expande a árvore até alcançar todos os vértices, sempre escolhendo conectar um vértice da árvore com outro que não está na árvore usando a aresta de menor peso



## Algoritmo de Prim

Como apenas uma árvore é mantida, podemos representá-la da mesma forma que no \proc{BFS} e \proc{DFS}.

- Para cada vértice $v$, mantemos o atributo $\attrib{v}{\pi} = u$, onde $(u, v)$ é uma aresta de peso mínimo que conecta $v$ a um vértice da árvore (o vértice $u$)

- Também precisamos armazenar o peso da aresta $(u, v)$, para isso mantemos em cada vértice $v$ um atributo $\attrib{v}{chave} = w(v, u)$. Se $v$ não pode ser ligado a árvore, então $\attrib{v}{\pi} = \const{Nil}$ e $\attrib{v}{chave} = \infty$



## Algoritmo de Prim

\includegraphics[trim=0pt 3164pt 1920pt 0pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|   $b$  |   $c$  |   $d$  |   $e$  |   $f$  |   $g$  |   $h$  |   $i$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |$\infty$|$\infty$|$\infty$|$\infty$|$\infty$|   $8$  |$\infty$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |        |        |        |        |        |   $a$  |        |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=1920pt 3164pt 0pt 0pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|   $c$  |   $d$  |   $e$  |   $f$  |   $g$  |   $h$  |   $i$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |$\infty$|$\infty$|$\infty$|$\infty$|   $8$  |$\infty$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |        |        |        |        |   $a$  |        |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=0pt 2373pt 1920pt 791pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|$\bm{c}$|   $d$  |   $e$  |   $f$  |   $g$  |   $h$  |   $i$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |   $7$  |$\infty$|   $4$  |$\infty$|   $8$  |   $2$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |   $c$  |        |   $c$  |        |   $a$  |   $c$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=1920pt 2373pt 0pt 791pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|$\bm{c}$|   $d$  |   $e$  |   $f$  |   $g$  |   $h$  |$\bm{i}$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |   $7$  |$\infty$|   $4$  |   $6$  |   $7$  |   $2$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |   $c$  |        |   $c$  |   $i$  |   $i$  |   $c$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=0pt 1582pt 1920pt 1582pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|$\bm{c}$|   $d$  |   $e$  |$\bm{f}$|   $g$  |   $h$  |$\bm{i}$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |   $7$  |  $10$  |   $4$  |   $2$  |   $7$  |   $2$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |   $c$  |   $f$  |   $c$  |   $f$  |   $i$  |   $c$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=1920pt 1582pt 0pt 1582pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|$\bm{c}$|   $d$  |   $e$  |$\bm{f}$|$\bm{g}$|   $h$  |$\bm{i}$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |   $7$  |  $10$  |   $4$  |   $2$  |   $1$  |   $2$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |   $c$  |   $f$  |   $c$  |   $f$  |   $g$  |   $c$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=0pt 791pt 1920pt 2373pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|$\bm{c}$|   $d$  |   $e$  |$\bm{f}$|$\bm{g}$|$\bm{h}$|$\bm{i}$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |   $7$  |  $10$  |   $4$  |   $2$  |   $1$  |   $2$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |   $c$  |   $f$  |   $c$  |   $f$  |   $g$  |   $c$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=1920pt 791pt 0pt 2373pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|$\bm{c}$|$\bm{d}$|   $e$  |$\bm{f}$|$\bm{g}$|$\bm{h}$|$\bm{i}$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |   $7$  |   $9$  |   $4$  |   $2$  |   $1$  |   $2$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |   $c$  |   $d$  |   $c$  |   $f$  |   $g$  |   $c$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

\includegraphics[trim=0pt 0pt 1920pt 3164pt,clip,width=9cm]{imagens/Fig-23-5.pdf}

<div class="columns">
<div class="column" width="25%"></div>
<div class="column" width="50%">

+--------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+:------:+
| Vértice |$\bm{a}$|$\bm{b}$|$\bm{c}$|$\bm{d}$|$\bm{e}$|$\bm{f}$|$\bm{g}$|$\bm{h}$|$\bm{i}$|
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $chave$ |    0   |   $4$  |   $8$  |   $7$  |   $9$  |   $4$  |   $2$  |   $1$  |   $2$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| $\pi$   |        |   $a$  |   $b$  |   $c$  |   $d$  |   $c$  |   $f$  |   $g$  |   $c$  |
+---------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

</div>
<div class="column" width="25%"></div>
</div>


## Algoritmo de Prim

Qual é o desafio para implementar o algoritmo de Prim de forma eficiente? \pause É escolher qual o próximo vértice a ser conectado na árvore. \pause

Vamos usar o conceito de fila de prioridades. Uma fila de prioridades tem as seguintes operações

- \proc{extract-min($Q$)}, remove o primeiro elemento da fila $Q$ (de acordo com a prioridade)

- \proc{decrease-key($Q$, $v$)}, atualiza a prioridade de $v$ na fila $Q$


## Algoritmo de Prim

Baseado no exemplo de funcionamento e nas operações de fila de prioridades, vamos escrever o pseudo código do algoritmo.


## Algoritmo de Prim

<div class="columns">
<div class="column" width="40%">
\footnotesize
\begin{codebox}
  \Procname{$\proc{MST-Prim}(G, w, r)$}
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   $\attrib{u}{chave} = \infty$
  \li   $\attrib{u}{\pi} = \const{nil}$
      \End
  \li $\attrib{r}{chave} = 0$
  \li $Q = \attrib{G}{V}$
  \li \While $Q \not = \emptyset$ \Do
  \li   $u = \proc{extract-min}(Q)$
  \li   \For $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $v \in Q$ e $w(u, v) < \attrib{v}{chave}$ \Then
  \li       $\attrib{v}{\pi} = u$
  \li       $\attrib{v}{chave} = w(u, v)$
          \End
        \End
      \End
\end{codebox}
</div>
<div class="column" width="60%">
\footnotesize
\pause
Análise do tempo de execução
\pause

- A inicialização nas linhas de 1 a 3 tem tempo $O(V)$
- A inicialização da fila na linha 4 requer $|V|$ operações \proc{insert} na fila (ou pode ser feito com uma única operação \proc{create})
- A operação \proc{extract-min} é executada uma vez para cada vértice
- O laço for das linhas 8 a 11 é executado no total $O(E)$ vezes
    - \footnotesize O teste de pertinência da linha 9 pode ser implementa em tempo constante usando um atributo no vértice
    - A atribuição na linha 11 envolve uma operação implícita de \proc{decrease-key}
- Portanto, o tempo de execução total é $O(V) \times O(\proc{insert}) + O(V) \times O(\proc{extract-min)} + O(E) \times O(\proc{decrease-key})$
</div>
</div>


## Análise do algoritmo de Prim

Como podemos implementar uma fila de prioridades? \pause

- Usando um arranjo simples \pause
    - \proc{create} inicializa um arranho com todos os vértices, $O(V)$ \pause
    - \proc{extract-min}, faz uma busca linear no arranjo e remove o vértice com menor chave, tempo $O(V)$ \pause
    - \proc{decrease-key} não faz nada, portanto $O(1)$ \pause

- Usando um Heap (Seção 6.5) \pause
    - \proc{create} inicializa um arranho com todos os vértices, $O(V)$ \pause
    - \proc{extract-min}, faz uma busca linear no arranjo e remove o vértice com menor chave, tempo $O(\lg V)$ \pause
    - \proc{decrease-key} não faz nada, portanto $O(\lg V)$ \pause

- Usando um Heap de Fibonacci (Capítulo 19)
    - Interesse teórico, na prática é superado pelo Heap


## Análise do algoritmo de Prim

Tempos das operações

Operação           | Arranjo  | Heap           | Heap de Fibonacci
-------------------|----------|----------------|------------------
\proc{create}      | $O(V)$   |   $O(V)$       | $O(V)$
\proc{extract-min} | $O(V)$   | $O(\lg V)$     | $O(\lg V)$ (amortizado)
\proc{decrease-key}| $O(1)$   | $O(\lg V)$     | $O(1)$ (amortizado)

\pause

Tempo de \proc{MST-Prim}

Tempo              | Arranjo         | Heap                  | Heap de Fibonacci
-------------------|-----------------|-----------------------|------------------
Grafo qualquer     | \pause $O(V^2)$ | \pause $O(E \lg V)$   | \pause $O(E + V \lg V)$ \pause
Grafo denso        | \pause $O(V^2)$ | \pause $O(V^2 \lg V)$ | \pause $O(V^2)$


## Regrar para reconhecer arestas seguras

Vamos fornecer uma regra para reconhecer arestas seguras, mas antes precisamos de algumas definições. \pause Seja $G = (V, E)$ um grafo não orientado, $S \subset V$ e $A \subseteq E$

- Um **corte** $(S, V - S)$ de $G$ é uma partição de $V$ \pause

- Uma aresta $(u, v) \in E$ **cruza** o corte $(S, V - S)$ se um de seus extremos está em $S$ e o outro em $V - S$ \pause

- Um corte **respeita** o conjunto $A$ de arestas se nenhuma aresta em $A$ cruza o corte \pause

- Uma aresta é uma **aresta leve** cruzando um corte se seu peso é o mínimo de qualquer aresta que cruza o corte


## Regrar para reconhecer arestas seguras

![](imagens/Fig-23-2.pdf)


## Regrar para reconhecer arestas seguras

### Teorema 23.1

Seja $G = (V, E)$ um grafo conexo não orientado com uma função peso $w$ de valor real definido em $E$. Seja $A$ um subconjunto de $E$ que está incluído em alguma árvore geradora mínima de $G$, seja $(S, V - S)$ qualquer corte de $G$ que respeita $A$ e seja $(u, v)$ uma aresta leve cruzando $(S, V - S)$. Então a aresta $(u, v)$ é segura para $A$. \pause

### Prova

Prova por construção. \pause

Seja $T$ uma AGM que contém $A$

- Se $T$ contém $(u, v)$, é claro que $(u, v)$ é segura para $A$

- Se $T$ não contém $(u, v)$, construímos outra AGM $T'$ que contem $A \cup \{(u, v)\}$

## Prova

<div class="columns">
<div class="column" width="30%">
![](imagens/Fig-23-3.pdf){width=4.5cm}

$T$ é a AGM que inclui $A$.

$(S, V - S)$ é qualquer corte que respeita $A$.

$(u, v)$ é uma aresta leve cruzando o corte.

</div>
<div class="column" width="70%">
\pause

Temos que mostrar que $(u, v)$ é segura para $A$.

A aresta $(u, v)$ forma um ciclo com as arestas no caminho simples $p$ de $u$ para $v$ em $T$. \pause Tem alguma aresta do caminho $p$ que cruza o corte? \pause Sim! \pause Porque $u$ e $v$ estão em lados opostos do corte. \pause Seja $(x, y)$ esta aresta. \pause

A aresta $(x, y)$ está em $A$? \pause Não, \pause pois o corte respeita $A$. \pause

Removendo a aresta $(x, y)$ quebra $T$ em dois componentes, adicionando $(u, v)$ reconecta os componentes formando a nova árvore geradora $T' = (T - \{(x, y)\}) \cup \{(u, v)\}$. \pause

Qual é a relação entre os pesos de $(x, y)$ e $(u, v)$? \pause Tanto $(x, y)$ e $(u, v)$ cruzam o corte $(S, V - S)$, como $(u, v)$ é uma aresta leve para este corte, então $w(u, v) \le w(x, y)$. Logo $w(T') = w(T) - w(x, y) + w(u, v) \le w(T)$. Como $T$ é uma AGM então $w(T) \le w(T')$, então $w(T) = w(T')$. Então $T'$ também é uma AGM.

</div>
</div>


## Como construir uma árvore geradora mínima

### Corolário 23.2

Seja $G = (V, E)$ um grafo conexo não orientado com uma função peso $w$ de valor real definido em $E$. Seja $A$ um subconjunto de $E$ que está incluído em alguma árvore geradora mínima de $G$, e seja $C = (V_C, E_C)$ um componente conexo (árvore) na floresta $G_A = (V, A)$. Se $(u, v)$ é uma aresta leve conectando $C$ a algum outro componente em $G_A$, então $(u, v)$ é segura para $A$.

\pause

### Prova

Tomamos $S = V_C$ no Teorema 23.1.


## Exercícios

23.1-1 Seja $(u, v)$ uma aresta de peso mínimo em um grafo conexo $G$. Mostre que $(u, v)$ pertence a alguma árvore geradora mínima de $G$.


## Exercícios

23.1-3 Mostre que se uma aresta $(u, v)$ está contido em alguma árvore geradora mínima, então ela é uma aresta leve cruzando algum corte do grafo.


## Exercícios

Veja a lista de exercícios e algumas soluções na página da disciplina.


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 23.
