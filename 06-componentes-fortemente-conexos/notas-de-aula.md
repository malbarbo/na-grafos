---
# vim: set spell spelllang=pt_br:
title: Componentes fortemente conexos
---

## Introdução

Vimos anteriormente uma classe de problemas que consistia em determinar a ordem de execução de tarefas com precedências. \pause

Um aspecto interessante na resolução desses problemas foi a modelagem:

- Representar o problema com um modelo (grafo) e definir o que é uma solução (ordenação topológica). \pause

Embora nós tenhamos "construído" o problema da ordenação topológica para resolver o problema de determinar a ordem de execução de tarefas com precedências, muitos outros problemas podem ser resolvidos com a ordenação topológica.


## Introdução

A criação e utilização de modelos é uma ferramente bastante útil na resolução de problemas. \pause

De fato, para muitos problemas o principal passo na sua resolução é a modelagem. \pause Isto porque a modelagem pode ter sido feita em termos de um problema já conhecido e para o qual já existem algoritmos eficientes. \pause

Por isso é importante estudar problemas e algoritmos em grafos! Quanto mais problemas e algoritmos você conhecer, melhor preparado você estará para resolver problemas do mundo real.



## Componente fortemente conexo

<!-- TODO: adicionar aplicações !-->

Um **componente fortemente conexo** (SCC) de um grafo orientado $G = (V, E)$ é um conjunto máximo de vértices $C \subseteq V$, tal que, para todo par de vértice $u$ e $v \in C$, existe um caminho de $u$ para $v$ e um caminho de $v$ para $u$, isto é $u \leadsto v$ e $v \leadsto u$.

\pause

\includegraphics[trim=0pt 1450pt 0pt 0pt,clip,width=8cm]{imagens/Fig-22-9.pdf}


## Grafo de componentes

Podemos entender melhor a relação entre os SCC's de um grafo criado um grafo com os SCC's. \pause

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1450pt 0pt 0pt,clip,width=6cm]{imagens/Fig-22-9.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=0pt 0pt 0pt 1450pt,clip,width=6cm]{imagens/Fig-22-9.pdf}
</div>
</div>

\pause

Que característica interessante podemos observar no grafo de componentes? \pause Ele é acíclico. \pause

O **grafo de componentes** de um grafo $G = (V, E)$ com os SCC's $C_1, C_2, \dots C_k$ é o grafo $G^\text{SCC} = (V^\text{SCC}, E^\text{SCC})$, onde:

- $V^\text{SCC} = \{v_1, v_2, \dots, v_k\}$ e cada vértice $v_i$ representa o SCC $C_i$ de $G$.

- $E^\text{SCC} = \{(v_i, v_j) |$ existe um vértice $x \in C_i$, um vértice $y \in C_j$ e $(x, y) \in E\}$



## Grafo de componentes

### Lema 22.13

Sejam $C$ e $C'$ SCC distintos em um grafo orientado $G = (V, E)$, seja $u, v \in C$ e seja $u', v' \in C'$. Suponha que exista um caminho $u \leadsto u'$ em $G$. Então, não pode existir um caminho $v' \leadsto v$ em $G$. \pause

### Prova

Por contradição. \pause

Suponha que exista um caminho $v' \leadsto v$ em $G$. \pause Então existem caminhos $u \leadsto u' \leadsto v'$ e $v' \leadsto v \leadsto u$ em $G$. \pause Portanto, $u$ e $v'$ são acessíveis um a partir do outro, e não podem estar em SCC separados, o que é uma contradição! $\qed$


## Grafo transposto

O **grafo transposto** de um grafo $G = (V, E)$ é o grafo $G^T = (V, E^T)$, onde $E^T = \{(u, v) : (v, u) \in E\}$. \pause Ou seja, $G^T$ é $G$ com todas as arestas invertidas. \pause

<div class="columns">
<div class="column" width="60%">
\includegraphics[trim=0pt 650pt 0pt 0pt,clip,width=6cm]{imagens/Fig-22-9.pdf}
</div>
<div class="column" width="40%">
\pause
Qual o tempo necessário para calcular $G^T$ a partir de $G$? \pause $\Theta(V + E)$ para lista de adjacências (veja o exercício 22.1-3).
\pause
Qual a relação entre os SCC's de $G$ e $G^T$. \pause São os mesmos. \pause Ou seja, dois vértices $u$ e $v$ são acessíveis um a partir do outro em $G$ se e somente se eles são acessíveis um a partir do outro em $G^T$.
</div>
</div>


## Procedimento \proc{strongly-connected-components}

<div class="columns">
<div class="column" width="50%">
\scriptsize

Usando estas observações e propriedades Kosaraju propos o seguinte algoritmo para encontrar os componentes fortemente conexos de um grafo:

\begin{codebox}
    \Procname{$\proc{strongly-connected-components}(G)$}
    \li chamar $\proc{DFS}(G)$ para calcular o
    \zi     tempo de término $\attrib{v}{f}$ de cada vértice
    \li calcular $G^T$
    \li chamar $\proc{DFS}(G^T)$ mas, no laço principal
    \zi     de $\proc{DFS}$, considerar os vértices
    \zi     em ordem decrescente de $\attrib{u}{f}$
    \li os vértices de cada árvore DFS formada na
    \zi     linha 3 formam um componente
    \zi     fortemente conexo
\end{codebox}

\pause

Ideia: ao considerar os vértices na segunda execução do $\proc{DFS}$ na ordem decrescente dos tempos de términos obtidos na primeira execução do $\proc{DFS}$, estamos visitando os vértices do grafo de componentes em ordem topológica.
</div>

<div class="column" width="50%">

\pause
\includegraphics[trim=0pt 0pt 0pt 0pt,clip,width=6cm]{imagens/Fig-22-9.pdf}

</div>
</div>

## Procedimento \proc{strongly-connected-components}

<div class="columns">
<div class="column" width="50%">
\scriptsize

\begin{codebox}
    \Procname{$\proc{strongly-connected-components}(G)$}
    \li chamar $\proc{DFS}(G)$ para calcular o
    \zi     tempo de término $\attrib{v}{f}$ de cada vértice
    \li calcular $G^T$
    \li chamar $\proc{DFS}(G^T)$ mas, no laço principal
    \zi     de $\proc{DFS}$, considerar os vértices
    \zi     em ordem decrescente de $\attrib{u}{f}$
    \li os vértices de cada árvore DFS formada na
    \zi     linha 3 formam um componente
    \zi     fortemente conexo
\end{codebox}

</div>

<div class="column" width="50%">

\pause

Tempo de execução \pause

- O tempo do $\proc{DFS}$ das linhas 1 e 3 é $\Theta(V + E)$ \pause

- Conforme os vértices são terminados na chamada do $\proc{DFS}$ da linha 1, os vértices são inseridos na frente de uma lista ligada ($O(1)$), como cada vértice é inserido apenas uma vez, o tempo total de operações de inserções é $\Theta(V)$ \pause

- O tempo para calcular o grafo transposto na linha 2 é $\Theta(V + E)$ \pause

- Portanto, o tempo de execução do algoritmo é $\Theta(V + E)$
</div>
</div>


## Corretude do \proc{strongly-connected-components}

Vamos definir duas questões de notação

- As referências a $\attrib{u}{d}$ e $\attrib{u}{f}$ referem-se aos valores obtidos na primeira execução do $\proc{DFS}$

- Para um conjunto $U \subseteq V$, definimos

    - $d(U) = \min_{u \in U} \{ \attrib{u}{d} \}$ (tempo de descoberta mais antigo)

    - $f(U) = \max_{u \in U} \{ \attrib{u}{f} \}$ (tempo de término mais recente)


## Corretude do \proc{strongly-connected-components}

### Lema 22.14

Sejam $C$ e $C'$ SCC distintos em $G = (V, E)$. Suponha que exista uma aresta $(u, v) \in E$, tal que $u \in C$ e $v \in C'$. Então $f(C) > f(C')$. \pause

### Prova

Que componente teve o primeiro vértice descoberto, $C$ ou $C'$? \pause Vamos considerar os dois casos.


## Corretude do \proc{strongly-connected-components}

No primeiro caso $d(C) < d(C')$. Seja $x$ o primeiro vértice descoberto de $C$: \pause

- Qual a cor dos vértices em $C$ e $C'$ no momento em que $x$ é descoberto? \pause Branco, porque $x$ foi o primeiro vértice descoberto de $C$ e $C'$. \pause

- Existe um caminho de vértices branco de $x$ para todos os vértices de $C$. \pause

- Como $(u, v) \in E$ e $u \in C$ e $v \in C'$, então existe um caminho de vértices brancos $x \leadsto u \rightarrow v \leadsto w$ para cada vértice $w \in C'$. \pause

- Portanto, pelo teorema do caminho branco, todos os vértices de $C$ e $C'$ se tornam descendentes de $x$. \pause

- Pelo Corolário 22.8, $x$ tem o maior tempo de término entre todos os descentes e portanto $\attrib{x}{f} = f(C) > f(C')$.


## Corretude do \proc{strongly-connected-components}

No segundo caso $d(C') < d(C)$. Seja $y$ o primeiro vértice descoberto de $C'$: \pause

- Qual a cor dos vértices em $C$ e $C'$ no momento em que $y$ é descoberto? \pause Branco, porque $y$ foi o primeiro vértice descoberto de $C$ e $C'$. \pause

- Existe um caminho de vértices branco de $y$ para todos os vértices de $C'$. \pause Então todos os vértices de $C'$ se tornam descendentes de $y$ e portanto $\attrib{y}{f} = f(C')$. \pause

- E os vértices de $C$ serão descendentes de $y$? \pause Não. Como existe a aresta $(u, v)$ de $C$ para $C'$, não pode existir uma aresta de $C'$ para $C$ (Lema 22.13) e portanto os vértices de $C$ não são acessíveis a partir de $y$ e não serão seu descendentes. \pause

- Logo, no tempo $\attrib{y}{f}$ todos os vértices de $C$ ainda são brancos, então para qualquer vértices $w \in C$, $\attrib{w}{f} > \attrib{y}{f}$ e portanto $f(C) > f(C')$. $\qed$


## Corretude do \proc{strongly-connected-components}

### Corolário 22.15

Sejam $C$ e $C'$ SCC distintos em $G = (V, E)$. Suponha que exista uma aresta $(u, v) \in E^T$, tal que $u \in C$ e $v \in C'$, então $f(C) < f(C')$. \pause

### Prova

Como $(u, v) \in E^T$, então $(v, u) \in E$. Como os SCC's de $G$ e $G^T$ são os mesmos, o lema 22.14 implica que $f(C) < f(C')$. $\qed$

\pause

Este corolário é fundamental para entendermos porque o algoritmo $\proc{strongly-connected-components}(G)$ funciona corretamente.

## Corretude do \proc{strongly-connected-components}

### Teorema 22.16

$\proc{strongly-connected-components}(G)$ calcula corretamente os SCC's de um grafo orientado $G$. \pause

### Prova \pause

Vamos discutir a ideia da prova. Para a prova formal, veja o livro.


## Corretude do \proc{strongly-connected-components}

A segunda execução do $\proc{DFS}$ começa por um vértice em uma SCC $C$ tal que $f(C)$ é máximo. Seja $x$ este vértice. \pause

A execução do $\proc{DFS}$ iniciada em $x$ visita pelo menos todos os vértices de $C$. \pause Algum outro vértice de alguma outra componente $C' \not = C$ é visitado nessa execução? \pause Pelo corolário 22.15, se existisse alguma aresta de um vértice de $C$ para um vértice de $C'$, então $f(C) < f(C')$, mas como $f(C) > f(C')$, então esta aresta não existe e portando nenhum vértice de outra componente é descoberto. \pause Logo, esta execução do $\proc{DFS}$ visita apenas os vértices de $C$, descobrindo este SCC. \pause

A próximo vértice inicial escolhido pelo $\proc{DFS}$ está em um SCC $C'$ tal que $f(C')$ é máximo em relação a todos os outros SCC (sem considerar $C$). \pause O \proc{DFS} visita todos os vértices de $C'$, e as únicas arestas para fora de $C'$ vão para $C$ (mesma argumentação usando o corolário 22.15 do item anterior), cujo os vértices já foram visitados. Ou seja, esta execução do \proc{DFS} descobre apenas os vértices de $C'$. \pause

Este processo continua até que todas as componentes tenham sido encontradas.


## Exercícios

22.5-1 - Como o número de componentes fortemente conexos de um grafo pode mudar se uma nova aresta é adiciona?

## Exercícios

22.5-6 - Dado um grafo orientado $G = (V, E)$, explique como criar um outro grafo $G' = (V, E')$ tal que

a) $G'$ tem os mesmos componentes fortemente conexos de $G$;

b) $G'$ tem o mesmo grafo de componentes de $G$; e

c) $E'$ tem o menor número possível de arestas.

Descreva um algoritmo eficiente para calcular $G'$.

## Exercícios

Veja a lista de exercícios e algumas soluções na página da disciplina.


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.5.
