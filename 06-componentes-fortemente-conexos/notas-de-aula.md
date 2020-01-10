---
# vim: set spell spelllang=pt_br:
title: Componentes fortemente conexos
---

## Introdução

<!-- TODO: adicionar aplicações !-->

- Um **componente fortemente conexo** (SCC) de um grafo orientado $G = (V, E)$
  é um conjunto máximo de vértices $C \subseteq V$, tal que, para todo par de
  vértice $u$ e $v$, $u \leadsto v$ e $v \leadsto u$

\pause

\includegraphics[trim=0pt 1450pt 0pt 0pt,clip,width=8cm]{imagens/Fig-22-9.pdf}


## Grafo transposto

- O algoritmo para identificar componentes fortemente conexos utiliza o grafo
  transposto de $G = (V, E)$

    - $G^T = (V, E^T), E^T = \{(u, v) : (v, u) \in E\}$

    - $G^T$ é $G$ com todas as arestas invertidas

    - $G^T$ pode ser calculado em tempo $\Theta(V + E)$ para a representação de
      lista de adjacências

    - $G$ e $G^T$ tem os mesmos SCC’s


## Grafo de componentes

- Grafo de componentes

    - $G^\text{SCC} = (V^\text{SCC}, E^\text{SCC})$

    - $V^\text{SCC}$ tem um vértice para cada SCC em $G$

    - $E^\text{SCC}$ contém uma aresta se existe uma aresta correspondente
      entre os SCC’s de $G$


## Grafo de componentes

- Um dos aspectos chaves para o algoritmo que veremos é que $G^\text{SCC}$ é um
  gao

\pause

\includegraphics[trim=0pt 1450pt 0pt 0pt,clip,width=6cm]{imagens/Fig-22-9.pdf}

\includegraphics[trim=0pt 0pt 0pt 1450pt,clip,width=6cm]{imagens/Fig-22-9.pdf}


## Grafo de componentes

### Lema 22.13

Sejam $C$ e $C'$ SCC distintos em um grafo orientado $G = (V, E)$, seja $u,
v \in C$ e seja $u', v' \in C'$. Suponha que exista um caminho $u \leadsto u'$
em $G$. Então, não pode existir um caminho $v' \leadsto v$ em $G$ \pause

### Prova

Suponha que exista um caminho $v' \leadsto v$ em $G$. Então existem caminhos $u
\leadsto u' \leadsto v'$ e $v' \leadsto v \leadsto u$ em $G$. Portanto, $u$
e $v'$ são acessíveis um a partir do outro, e não podem estar em SCC separados


## Procedimento \proc{strongly-connected-components}

<div class="columns">
<div class="column" width="45%">
\scriptsize

\begin{codebox}
    \Procname{$\proc{strongly-connected-components}(G)$}
    \li chamar $\proc{DFS}(G)$ para calcular o
    \zi     tempo de término $\attrib{v}{f}$ de cara vértice
    \li calcular $G^T$
    \li chamar $\proc{DFS}(G^T)$ mas, no laço principal
    \zi     de $\proc{DFS}$, considerar os vértices
    \zi     em ordem decrescente de $\attrib{u}{f}$
    \li os vértices de cada árvore DFS formada na
    \zi     linha 3 formam um componente
    \zi     fortemente conexo
\end{codebox}

</div>

<div class="column" width="55%">

\footnotesize

\pause

Tempo de execução \pause

- O tempo do $\proc{DFS}$ das linhas 1 e 3 é $\Theta(V + E)$

- Conforme os vértices são terminados na chamada do $\proc{DFS}$ da linha 1, os
  vértices são inseridos na frente de uma lista ligada ($O(1)$), como cada
  vértice é inserido apenas uma vez, o tempo total de operações de inserções é
  $\Theta(V)$

- O tempo para calcular o grafo transposto na linha 2 é $\Theta(V + E)$

- Portanto, o tempo de execução do algoritmo é $\Theta(V + E)$
</div>
</div>


## Exemplo de execução

![](imagens/Fig-22-9.pdf){width=6cm}


## Corretude do \proc{strongly-connected-components}

- Ao considerar os vértices na segunda execução do $\proc{DFS}$ na ordem
  decrescente dos tempos de términos obtidos na primeira execução do
  $\proc{DFS}$, estamos visitando os vértices do grafo de componentes em ordem
  topológica


## Corretude do \proc{strongly-connected-components}

- Vamos definir duas questões de notação

    - As referências a $\attrib{u}{d}$ e $\attrib{u}{f}$ referem-se aos valores
      obtidos na primeira execução do $\proc{DFS}$

    - Para um conjunto $U \subseteq V$, definimos

        - $d(U) = \min_{u \in U} \{ \attrib{u}{d} \}$ (tempo de descoberta mais antigo)

        - $f(U) = \max_{u \in U} \{ \attrib{u}{f} \}$ (tempo de término mais recente)


## Corretude do \proc{strongly-connected-components}

### Lema 22.14

Sejam $C$ e $C'$ SCC distintos em $G = (V, E)$. Suponha que exista uma aresta
$(u, v) \in E$, tal que $u \in C$ e $v \in C'$. Então $f(C) > f(C')$. \pause

### Prova

Que componente teve o primeiro vértice descoberto, $C$ ou $C'$? \pause Vamos
considerar os dois casos


## Corretude do \proc{strongly-connected-components}

- No primeiro caso $d(C) < d(C')$. Seja $x$ o primeiro vértice descoberto de
  $C$ \pause

    - Qual a cor dos vértices em $C$ e $C'$ no momento em que $x$ é descoberto?
      \pause Branco, porque $x$ foi o primeiro vértice descoberto de $C$ e $C'$
      \pause

    - Existe um caminho de vértices branco de $x$ para todos os vértices
      de $C$ \pause

    - Como $(u, v) \in E$ e $u \in C$ e $v \in C'$, então existe um caminho de
      vértices brancos de $x \leadsto u \rightarrow v \leadsto w$ para cada
      vértice $w \in C'$ \pause

    - Portanto, pelo teorema do caminho branco, todos os vértices de $C$ e $C'$
      se tornam descendentes de $x$ \pause

    - Pelo Corolário 22.8, $x$ tem o maior tempo de término entre todos os
      descentes e portanto $\attrib{x}{f} = f(C) > f(C')$.


## Corretude do \proc{strongly-connected-components}

- No segundo caso $d(C') < d(C)$. Seja $y$ o primeiro vértice descoberto de
  $C'$ \pause

    - Qual a cor dos vértices em $C$ e $C'$ no momento em que $y$ é descoberto?
      \pause Branco, porque $y$ foi o primeiro vértice descoberto de $C$ e $C'$
      \pause

    - Existe um caminho de vértices branco de $y$ para todos os vértices de
      $C'$. \pause Então todos os vértices de $C'$ se tornam descendentes
      de $y$ e portanto $\attrib{y}{f} = f(C')$

    - E os vértices de $C$ serão descendentes de $y$? \pause Como existe
      a aresta $(u, v)$ de $C$ para $C'$, não pode existir uma aresta de $C'$
      para $C$ (Lema 22.13) e portanto os vértices de $C$ não são acessíveis
      a partir de $y$ e não serão seu descendentes

    - Portanto, no tempo $\attrib{y}{f}$ todos os vértices de $C$ ainda são
      brancos, então para qualquer vértices $w \in C$, $\attrib{w}{f}
      > \attrib{y}{f}$ e portanto $f(C) > f(C')$


## Corretude do \proc{strongly-connected-components}

### Corolário 22.15

Sejam $C$ e $C'$ SCC distintos em $G = (V, E)$. Suponha que exista uma aresta
$(u, v) \in E^T$, tal que $u \in C$ e $v \in C'$. Então $f(C) < f(C')$


## Corretude do \proc{strongly-connected-components}

### Teorema 22.16

$\proc{strongly-connected-components}(G)$ calcula corretamente os SCC's de um
grafo orientado $G$

- A segunda execução do $\proc{DFS}$ começa com um SCC $C$ tal que $f(C)$ é máximo

- Seja $x \in C$ o vértice inicial, a segunda execução do $\proc{DFS}$ visita
  todos os vértices de $C$. Pelo corolário 22.15, como $f(C) > f(C')$ para todo
  $C \not = C'$, não existe aresta de $C$ para $C'$. Logo, o $\proc{DFS}$
  visita apenas os vértices de $C$ (descobrindo este SCC)

- A próxima origem escolhida na segunda execução do $\proc{DFS}$ está em um SCC
  $C'$ tal que $f(C')$ é máximo em relação a todos os outros SCC (sem
  considerar $C$). O $\proc{DFS}$ visita todos os vértices de $C'$, e as únicas
  arestas para fora de $C'$ vão para $C$, cujo os vértices já foram visitados

- O processo continua até que todos os vértices sejam visitados


## Corretude do \proc{strongly-connected-components}

- Cada vez que uma origem é escolhida pelo segundo $\proc{DFS}$, ele só pode
  alcançar

    - Os vértices no SCC dele (através de arestas da árvore)

    - Os vértices que já foram visitados no segundo $\proc{DFS}$


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.5.
