---
# vim: set spell spelllang=pt_br:
title: Árvores geradoras mínimas
---

## Introdução

- Dado um grafo conexo não orientado $G = (V, E)$ e uma função peso $w: E
  \rightarrow \mathbb{R}$, queremos encontrar um subconjunto acíclico $T \subseteq E$
  que conecte todos os vértices de $G$ e cujo peso total

  $$
  \displaystyle w(T) =
  \sum_{(u, v) \in T} w(u, v)
  $$

  seja minimizado

- Como $T$ é acíclico e conecta todos os vértices, $T$ forma uma árvore, que
  chamamos de **árvore geradora mínima** (AGM ou MST em inglês)


## Introdução

Exemplo de uma AGM

![](imagens/Fig-23-1.pdf){width=6cm}

\pause

Propriedades de uma AGM

- Tem $|V| - 1$ arestas

- Não tem ciclos

- Pode não ser única


## Introdução

- O **problema da árvore geradora mínima** consiste em encontrar uma AGM de uma
  dado grafo com pesos nas arestas

- Veremos dois algoritmos gulosos para resolver este problema

    - Algoritmo de Kruskal

    - Algoritmo de Prim


## Como construir uma árvore geradora mínima

- Como construir uma árvore geradora mínima? \pause Uma aresta de cada vez! \pause

- Começamos com um conjunto vazio $A$ \pause

- Em cada etapa, determinamos um aresta $(u, v)$ que pode ser adicionada a $A$,
  de forma a manter a seguinte invariante

    - Antes de cada iteração, $A$ é um subconjunto de alguma árvore geradora
      mínima \pause

- A aresta $(u, v)$ é chamada de **aresta segura** para $A$


## Como construir uma árvore geradora mínima

\begin{codebox}
    \Procname{$\proc{generic-MST}(G, w)$}
    \li $A = \emptyset$
    \li \While $A$ não forma uma árvore geradora \Do
    \li     encontre uma aresta $(u,v)$ que seja segura para $A$
    \li     $A = A \cup \{ (u, v) \}$
        \End
    \li \Return $A$
\end{codebox}


## Como construir uma árvore geradora mínima

Vamos fornecer uma regra para reconhecer arestas seguras, mas antes precisamos
de algumas definições. \pause Seja $S \subset V$ e $A \subseteq E$

- Um **corte** $(S, V - S)$ de um grafo não orientado $G = (V, E)$ é uma
  partição de $V$ \pause

- Uma aresta $(u, v) \in E$ **cruza** o corte $(S, V - S)$ se um de seus
  extremos está em $S$ e o outro em $V - S$ \pause

- Um corte **respeita** o conjunto $A$ de arestas se nenhuma aresta em $A$
  cruza o corte \pause

- Uma aresta é uma **aresta leve** cruzando um corte se seu peso é o mínimo de
  qualquer aresta que cruza o corte


## Como construir uma árvore geradora mínima

![](imagens/Fig-23-2.pdf)


## Como construir uma árvore geradora mínima

### Teorema 23.1

Seja $G = (V, E)$ um grafo conexo não orientado com uma função peso $w$ de
valor real definido em $E$. Seja $A$ um subconjunto de $E$ que está incluído em
alguma árvore geradora mínima de $G$, seja $(S, V - S)$ qualquer corte de $G$
que respeita $A$ e seja $(u, v)$ uma aresta leve cruzando $(S, V - S)$. Então
a aresta $(u, v)$ é segura para $A$.


## Ideia da prova

![](imagens/Fig-23-3.pdf){width=5cm}

- Seja $T$ uma AGM que inclui $A$

    - Se $T$ contém $(u, v)$, é claro que $(u, v)$ é segura para $A$

    - Se $T$ não contém $(u, v)$, construímos outra AGM $T'$ que inclui $A \cup
      \{(u, v)\}$ (feito em sala, veja o livro)


## Como construir uma árvore geradora mínima

### Corolário 23.2

Seja $G = (V, E)$ um grafo conexo não orientado com uma função peso $w$ de
valor real definido em $E$. Seja $A$ um subconjunto de $E$ que está incluído em
alguma árvore geradora mínima de $G$, e seja $C = (V_C, E_C)$ um componente
conexo (árvore) na floresta $G_A = (V, A)$. Se $(u, v)$ é uma aresta leve
conectando $C$ a algum outro componente em $G_A$, então $(u, v)$ é segura para
$A$.

\pause

### Prova

Tomamos $S = V_C$ no teorema 23.1


## Algoritmo de Kruskal

- Baseia-se diretamente no algoritmo genérico

- Inicialmente cada vértice está em sua própria componente (árvore)

- De todas as arestas que conectam duas árvores quaisquer na floresta, uma
  aresta $(u, v)$ de peso mínimo é escolhida. A aresta $(u, v)$ é segura para
  alguma das duas árvores


## Algoritmo de Kruskal

- A questão principal é como gerenciar as árvores (verificar se dois vértices
  estão na mesma árvore e juntar duas árvores)

    - Utilizamos uma estrutura de dados de conjuntos disjuntos

    - Cada conjunto contém os vértices de uma árvore da floresta atual


## Algoritmo de Kruskal

\includegraphics[trim=0pt 2371pt 1920pt 0pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 2371pt 0pt 0pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=0pt 1581pt 1920pt 790pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 1581pt 0pt 790pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=0pt 791pt 1920pt 1580pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 791pt 0pt 1580pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=0pt 1pt 1920pt 2370pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1920pt 1pt 0pt 2370pt,clip,]{imagens/Fig-23-4-L.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=10pt 1582pt 1919pt 60pt,clip,]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1929pt 1582pt 0pt 60pt,clip,]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=10pt 791pt 1919pt 851pt,clip,]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1929pt 791pt 0pt 851pt,clip,]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=10pt 0pt 1919pt 1642pt,clip,]{imagens/Fig-23-4-R.pdf}

## Algoritmo de Kruskal

\includegraphics[trim=1929pt 0pt 0pt 1642pt,clip,]{imagens/Fig-23-4-R.pdf}


## Algoritmo de Kruskal

\begin{codebox}
    \Procname{$\proc{MST-Kruskal}(G, w)$}
    \li $A = \emptyset$
    \li \For $v \in \attrib{G}{V}$ \Do
    \li   $\proc{make-set(v)}$
        \End
    \li ordenar em ordem não decrescente as arestas de $E$ pelo peso $w$
    \li \For $(u, v) \in E$, na ordem obtida anteriormente \Do
    \li   \If $\proc{find-set}(u) \not = \proc{find-set}(v)$ \Then
    \li     $A = A \cup \{ (u, v) \}$
    \li     $\proc{union}(u, v)$
          \End
        \End
    \li \Return $A$
\end{codebox}


## Análise do algoritmo de Kruskal

- A ordenação das arestas na linha 4 demora $O(E \lg E)$

- Operações com conjuntos disjuntos (depende da implementação, supomos a
  implementação da seção 21.3)

    - O laço das linhas 5 a 8 executa $O(E)$ \proc{find-set} e \proc{union}.
      Juntamente com as $|V|$ operações \proc{make-set}, elas demoram $O((V
      + E)\alpha(V))$, onde $\alpha$ é uma função de crescimento muito lento

    - Pelo fato de $G$ ser supostamente conexo, temos que $|E| \ge |V| - 1$,
      portanto o tempo com operações com conjuntos disjuntos é $O(E\alpha(V))$

    - Além disso, $\alpha(|V|) = O(\lg V) = O(\lg E)$, e portanto o tempo total
      das operações com conjuntos disjuntos é $O(E\lg E)$


## Análise do algoritmo de Kruskal

- Somando o custo de ordenação e o custo das operações com conjuntos disjuntos,
  temos $O(E \lg E)$. Observando que $|E| < |V^2|$, temos que $\lg |E| = O(\lg
  V)$, e portanto, o tempo de execução do algoritmo é $O(E\lg V)$


## Algoritmo de Prim

- Baseia-se diretamente no algoritmo genérico

- As arestas do conjunto $A$ formam uma única árvore

- A árvore começa com uma raiz arbitrária $r$ e aumenta até alcançar todos os
  vértices em $V$

- Para cada vértice $v$, mantemos dois atributos, $\attrib{v}{chave} = w(v, u)$
  e $\attrib{v}{\pi} = u$, onde $(u, v)$ é uma aresta de peso mínimo que
  conecta $v$ a um vértice de $V$ (o vértice $u$). Usamos $\attrib{v}{chave}
  = \infty$ se não existe tal aresta

- Em cada passo, um vértice $v$ com a menor chave é adicionado a árvore junto
  com a aresta $(\attrib{v}{\pi}, v)$


## Algoritmo de Prim

- A questão principal para implementar o algoritmo de Prim de forma eficiente é
  tornar fácil a seleção de uma nova aresta a ser adicionada à árvore

    - Usamos uma fila de prioridades


## Algoritmo de Prim

\includegraphics[trim=0pt 3164pt 1920pt 0pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=1920pt 3164pt 0pt 0pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=0pt 2373pt 1920pt 791pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=1920pt 2373pt 0pt 791pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=0pt 1582pt 1920pt 1582pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=1920pt 1582pt 0pt 1582pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=0pt 791pt 1920pt 2373pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=1920pt 791pt 0pt 2373pt,clip,]{imagens/Fig-23-5.pdf}

## Algoritmo de Prim

\includegraphics[trim=0pt 0pt 1920pt 3164pt,clip,]{imagens/Fig-23-5.pdf}


## Algoritmo de Prim

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


## Análise do algoritmo de Prim

\small

- Depende de como a fila de prioridade é implementada

- Se a fila for implementada como um heap mínimo, o algoritmo \proc{build-min-heap}
  é utilizado na inicialização nas linhas 1 a 5 no tempo $O(V)$

- O corpo do laço while é executado $|V|$ vezes, como cada operação
  \proc{extract-min} demora $O(\lg V)$, o tempo total para todas as chamadas de
  \proc{extract-min} é $O(V \lg V)$

- O laço for das linhas 8 a 11 é executado no total $O(E)$ vezes

- O teste de pertinência da linha 9 pode ser implementa em tempo constante

- A atribuição na linha 11 envolve uma operação implícita de
  \proc{decrease-key}, que demora $O(\lg V)$, o tempo para todas as chamadas de
  \proc{decrease-key} é $O(E \lg V)$

- Portanto, o tempo total do algoritmo é $(V \lg V + E \lg V) = O(E \lg V)$


## Análise do algoritmo de Prim

- Se heap de Fibonacci for usando o tempo de execução assintótico pode ser
  melhorado

- \proc{extract-min} é executado em tempo amortizado de $O(\lg V)$

- \proc{decrease-key} é executado em tempo amortizado de $O(1)$

- Tempo total do algoritmo melhora para $O(E + V \lg V)$


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 23.
