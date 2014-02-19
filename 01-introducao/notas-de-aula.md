---
title: Introdução
template: slide.tex
---

# Histórico

### Histórico

-   Em 1736 Leonhard Euler propôs e resolveu o problema das sete pontes de
    Königsberg

-   A cidade de Königsberg era cortada por um rio que continha duas ilhas

-   Existiam 7 pontes que ligavam as ilhas e as margens do rios

-   O problema consistia em encontrar um caminho que cruzasse cada uma das 7
    pontes uma única vez

-   Existe tal caminho?

### Histórico

-   Euler formulou o problema em termos abstratos


![]([inline,width=3cm]konigsberg-1) \pause
$\rightarrow$
![]([inline,width=3cm]konigsberg-2) \pause
$\rightarrow$
![]([inline,width=3cm]konigsberg-3)


### Histórico

-   Euler observou que toda vez que alguém atinge uma porção de terra por uma
    ponte, deve deixar a porção de terra também por uma ponte

-   Para que cada ponte fosse cruzada apenas uma vez, todas as porcões de terra,
    exceto talvez a inicial e a final, deveriam ter um número par de pontes
    ligadas a ela

-   Mas todas as porções de terra do problema tem um número ímpar de pontes

-   Com esta observação, Euler mostrou que não é possível fazer o percurso

-   Surgiu a área da matemática que é conhecida como Teoria dos Grafos

# Definições e propriedades

### Definições e propriedades

-   Um **grafo orientado** $G$ é um par $(V, E)$, onde

    -   $V$ é um conjunto finito, chamado de **conjunto de vértices**

    -   $E$ é uma relação binária em $V$, chamado de **conjunto de arestas**

-   Em um **grafo não orientado** $G = (V, E)$, $E$ consiste de pares de
    vértices não ordenados

-   Os grafos podem ser representados graficamente

    -   Os vértices são desenhados como círculos

    -   As arestas são desenhadas como curvas ligando dois círculos, no caso de
        grafos orientados, as curvas tem um seta em uma das extremidades

### Definições e propriedades

![B-2](Fig-B-2)

-   Na figura B-2-a, qual é o conjunto de vértices e o conjunto de arestas?

    \pause $V = \{1, 2, 3, 4, 5, 6\}$,
    $E = \{(1,2), (2,2), (2,4), (2,5), (4,1), (4,5), (5,4), (6,3)\}$

    \pause

-   Na figura B-2-b, qual é o conjunto de vértices e o conjunto de arestas?

    \pause $V = \{1, 2, 3, 4, 5, 6\}$, $E = \{(1,2), (1,5), (2,5), (3,6)\}$

### Definições e propriedades

![B-2](Fig-B-2)

-   Observações

    -   Em grafos orientados são permitidos **autoloops** (arestas de um vértice
        para ele mesmo). Em grafos não orientados não são permitidos. Exemplo:
        aresta $(2, 2)$ da figura B-2-a

    -   Um grafo orientado sem autoloops é chamado de **grafo simples**

    -   Para grafos não orientados, definimos a convenção de utilizar $(u,v)$
        para uma aresta, ao invés da notação de conjunto $\{u, v\}$. $(u, v)$ e
        $(v, u)$ são consideradas a mesma aresta

### Definições e propriedades

-   Para uma aresta $(u, v)$ em um grafo orientado, dizemos que

    -   $(u, v)$ é **incidente do** ou **sai do** vértice $u$ e é **incidente
        no** ou **entra no** vértice $v$ \pause

    -   Quais as arestas que saem do vértice 2 na figura B-2-a? \pause $(2,2), (2,4)$
        e $(2,5)$ \pause

    -   Quais as arestas que entram no vértice 2 na figura B-2-a? \pause $(1,2)$ e
        $(2,2)$

    \pause

-   Para uma aresta $(u, v)$ em um grafo não orientado, dizemos que

    -   $(u, v)$ é **incidente** nos vértices $u$ e $v$ \pause

    -   Quais são as arestas incidentes no vértice 2 da figura B-2-b? \pause $(1,2)$
        e $(2,5)$

### Definições e propriedades

-   Para uma aresta $(u, v)$, dizemos que o vértice $v$ é **adjacente** ao
    vértice $u$

-   Para grafos não orientados, a relação de adjacência é simétrica

-   Se $v$ é adjacente a $u$ em um grafo orientado, escrevemos $u \rightarrow v$
    \pause

-   O vértice 1 é adjacente ao vértice 2 na figura B-2-b? \pause Sim. \pause E na
    figura B-2-a? \pause Não, pois não existe a aresta $(2, 1)$

### Definições e propriedades

-   Em um grafo não orientado

    -   O **grau** de um vértice é o número de arestas incidentes nele \pause

    -   Na figura B-2-b, qual é o grau do vértice 2? \pause 2

    \pause

-   Em um grafo orientado

    -   O **grau de saída** de um vértice é o número de arestas que saem dele

    -   O **grau de entrada** de um vértice é o número de arestas que entram
        nele

    -   O **grau** de um vértice é soma do grau de saída e do grau de entrada
        \pause

    -   Na figura B-2-a, qual é o grau de entrada, o grau de saída e o grau do
        vértice 2? \pause 2, 3 e 5

    \pause

-   Um vértice **isolado** tem grau 0 \pause

    -   Existe algum vértice isolado nos grafos da figura B-2? \pause Sim, o
        vértice 4 da figura B-2-b


## Caminhos e ciclos

### Caminhos e ciclos

-   Um **caminho** de **comprimento k** de um vértice $u$ até um vértice $u'$ em
    um grafo $G = (V, E)$ é uma sequência
    $\langle v_0, v_1, v_2, \dots, v_k \rangle$ de vértices tal que $u = v_0$,
    $u' = v_k$ e $(v_{i-1}, v_i) \in E$ para $i = 1, 2, \dots, k$

-   O comprimento do caminho é a quantidade de aresta no caminho

-   O caminho **contém** os vértice $v_0, v_1, \dots, v_k$ e as arestas
    $(v_0, v_1), (v_1, v_2), \dots, (v_{k-1}, v_k)$

-   Se existe um caminho $p$ de $u$ até $u'$, dizemos que $u'$ é **acessível** a
    partir de $u$ via $p$, ou $u \stackrel{p}{\leadsto} u'$ se o grafo é
    orientado

-   Sempre existe um caminho de comprimento 0 de $u$ para $u$

-   Exemplos da figura B-2-a: $\langle 1, 2, 5, 4 \rangle$,
    $\langle 2, 5, 4, 5 \rangle$ e $\langle 3 \rangle$

### Caminhos e ciclos

-   Um caminho é **simples** se todos os vértices no caminho são distintos

-   Existe um caminho de tamanho 5 no grafo da figura B-2-a? \pause Sim. Por exemplo,
    $\langle 1, 2, 5, 4, 1, 2 \rangle$ \pause

-   Existe um caminho simples de tamanho 5 no grafo da figura B-2-a? \pause Não

### Caminhos e ciclos

-   Um **subcaminho** do caminho $p = \langle v_0, v_1, \dots, v_k \rangle$ é
    uma subsequência contígua de seus vértices

-   Em um grafo orientado

    -   Um caminho $\langle v_0, v_1, \dots, v_k \rangle$ forma um **ciclo** se
        $v_0 = v_k$ e o caminho contém pelo menos uma aresta

    -   O ciclo é **simples** se além disso $v_1, v_2, \dots, v_k$ são distintos

    -   Dois caminhos $\langle v_0, v_1, \dots, v_{k-1}, v_0 \rangle$ e
        $\langle v_0', v_1', \dots, v_{k-1}', v_0' \rangle$ formam o mesmo ciclo
        se existe um inteiro $j$ tal que $v_i' = v_{(i + j) \mod k}$ para
        $i = 0, 1, \dots, k - 1$

        -   Considerando a figura B-2-a, dê dois caminhos que formam o mesmo ciclo
            que o caminho $\langle 1, 2, 4, 1 \rangle$. \pause
            $\langle 2, 4, 1, 2 \rangle$ e $\langle 4, 1, 2, 4 \rangle$

### Caminhos e ciclos

-   Em um grafo não orientado

    -   Um caminho $\langle v_0, v_1, \dots, v_k \rangle$ forma um **ciclo** se
        $k \ge 3$ e $v_0 = v_k$

    -   O ciclo é **simples** se $v_1, v_2, \dots, v_k$ são distintos

-   Um grafo sem ciclo é **acíclico**

## Conexidade

### Conexidade

-   Um grafo não orientado é **conexo** se cada vértice é acessível a partir de
    todos os outros \pause

-   Os **componentes conexos** de um grafo são as classes de equivalência de
    vértices sob a relação “é acessível a partir de”

    -   Na figura B-2-b quais são os componentes conexos? \pause $\{1, 2, 5\}$,
        $\{3, 6\}$ e $\{4\}$

    \pause

-   Um grafo não orientado é conexo se tem exatamente um componente conexo

### Conexidade

-   Um grafo orientado é **fortemente conexo** se para cada par de vértices
    $(u, v)$, $v$ é acessível a partir de $u$

-   Os **componentes fortemente conexos** de um grafo orientado são as classes
    de equivalência de vértices sob a relação “são mutuamente acessíveis” \pause

-   Um grafo orientado é fortemente conexo se ele só tem um componente
    fortemente conexo

    -   Quais os componentes fortemente conexos da figura B-2-a? \pause $\{1, 2, 4, 5\}$
        \pause , $\{3\}$ e $\{6\}$ \pause

    -   Todos os pares de vértices em $\{1, 2, 4, 5\}$ são mutuamente acessíveis
        \pause

    -   Os vértices $\{3, 6\}$ não formam um componente fortemente conexo. Por
        quê? \pause O vértice 6 não pode ser acessado a partir do vértice 3

## Isomorfismo

### Isomorfismo

-   Dois grafos $G=(V, E)$ e $G'=(V', E')$ são **isomorfos** se existe uma
    bijeção $f: V \rightarrow V'$ tal que $(u, v) \in E$ se e somente se $(f(u),
      f(v)) \in E'$

    -   Podemos identificar os vértices de $G$ como vértices de $G'$, mantendo
        as arestas correspondentes em $G$ e $G'$

### Isomorfismo

![B-3](Fig-B-3)

### Isomorfismo

-   Os grafos da figura B-3-a são isomorfos entre si?

    -   $V=\{1, 2, 3, 4, 5, 6\}$ e $V'=\{u, v, w, x, y, z\}$ \pause

    -   $|V|=6$ e $|V'|=6$ ; $|E|= 9$ e $|E'|=9$ \pause

    -   Mapeamento de $V$ para $V'$ dado pela função bijetora\
        $f(1)= u$, $f(2)=v$, $f(3)=w$, $f(4)=x$, $f(5)=y$, $f(6)=z$ \pause

    -   Sim, são isomorfos

### Isomorfismo

-   Os grafos da figura B-3-b, são isomorfos?

    -   $V=\{1, 2, 3, 4, 5\}$ e $V'=\{u, v, w, x, y\}$ \pause

    -   $|V|=5$ e $|V'|=5$; $|E|=7$ e $|E'|=7$ \pause

    -   $G$ tem um vértice de grau 4, mas $G'$ não tem \pause

    -   Não são isomorfos

## Subgrafos

### Subgrafos

-   $G'=(V', E')$ é um **subgrafo** de $G=(V, E)$ se $V' \subseteq V$ e
    $E' \subseteq E$ \pause

-   Dado um conjunto $V'$ de modo que $V' \subseteq V$, o subgrafo de $G$
    **induzido** por $V'$ é o grafo $G'=(V', E')$, onde
    $E'=\{(u, v) \in E: u, v \in V'\}$

-   Qual é o subgrafo induzido pelo conjunto de vértices $\{1, 2, 3, 6\}$ na
    figura B-2-a? \pause $G = (\{1, 2, 3, 6\}, \{(1, 2), (2, 2), (6, 3)\}$

## Versões orientada e não orientada

### Versões orientada e não orientada

<!-- TODO: colocar exemplo !-->

-   Dado um grafo não orientado $G=(V, E)$, a **versão orientada** de $G$ é o
    grafo orientado $G'=(V, E')$, onde $(u, v) \in E'$ se e somente se
    $(u, v) \in E$

    -   Cada aresta não orientada $(u, v)$ em $G$ é substituída na versão
        orientada pelas duas arestas orientadas $(u, v)$ e $(v, u)$

    \pause

-   Dado um grafo orientado $G=(V, E)$, a **versão não orientada** de $G$ é o
    grafo não orientado $G'=(V, E')$, onde $(u, v) \in E'$ se e somente se
    $u \neq v$ e $(u, v) \in E$

    -   A versão não orientada contém as arestas de $G$ “com suas orientações
        removidas” e autoloops eliminados \pause

    -   Mesmo que o grafo orientado contenha as arestas $(u, v)$ e $(v, u)$, o
        grafo não orientado conterá $(u, v)$ somente uma vez

## Vizinho

### Vizinho

-   Em um grafo orientado, um vizinho de um vértice $u$ é qualquer vértice que
    seja adjacente a $u$ na versão não orientada

    -   $v$ é **vizinho** de $u$ se $(u, v) \in E$ ou $(v, u) \in E$

    \pause

-   Em um grafo não orientado, $u$ e $v$ são vizinhos se são adjacentes

# Grafos com nomes especiais

### Grafos com nomes especiais

<!-- TODO: colocar exemplo !-->

-   **Grafo completo** é um grafo não orientado no qual todo par de vértices é
    adjacente

-   Um grafo completo com $n$ vértices é chamado de $K_n$ \pause

-   **Grafo bipartido** é um grafo não orientado $G=(V, E)$ em que $V$ pode ser
    particionado em dois conjuntos $V_1$ e $V_2$ tais que $(u, v) \in E$ implica
    que\
    $u \in V_1$ e $v \in V_2$ ou\
    $u \in V_2$ e $v \in V_1$

    -   Todas as arestas ficam entre os dois conjuntos $V_1$ e $V_2$

    \pause

-   Um grafo acíclico não orientado é uma **floresta**

-   Um grafo conexo acíclico não orientado é uma **árvore (livre)** \pause

-   **gao**: grafo acíclico orientado

# Variantes de grafos

### Variantes de grafos

-   Semelhantes a grafos não orientados

    -   **Multigrafo**: pode ter várias arestas entre vértices e também
        autoloops \pause

    -   **Hipergrafo**: cada **hiperarestas**, em lugar de conectar dois
        vértices, conecta um subconjunto arbitrário de vértices

# Referências

### Referências

-   [Wikipedia - Seven Bridges of
    Königsberg](https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg)

-   Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo B.4.


<!-- vim: set spell spelllang=pt_br: -->
