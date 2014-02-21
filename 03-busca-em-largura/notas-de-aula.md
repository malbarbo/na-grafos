---
title: Busca em largura
template: slide.tex
---

# Introdução

### Introdução

<!--
Dica: apresentar o conceito do número de Erdös
      e o problema associado
!-->

-   Dado um grafo $G = (V, E)$ e um vértice de origem $s$, a busca em largura
    explora sistematicamente as arestas de $G$ até descobrir cada vértice
    acessível a partir de $s$

-   O algoritmo calcula a distância (menor número de arestas) deste $s$ até
    todos os vértices acessíveis a partir de $s$

-   O algoritmo produz uma árvore primeiro em extensão

-   Recebe este nome porque expande a fronteira entre vértices descobertos e não
    descobertos uniformemente ao longo da extensão da fronteira. Descobre todos
    os vértices de distância $k$ de $s$ antes de descobrir quaisquer vértices de
    distância $k + 1$

# Exemplo de execução

### Exemplo de execução

<!-- Gerado com o comando bin/split-image clrs/Chapter\ 22/Fig-22-3.pdf 1500 470 5 2 height=2.5cm !-->

![]([trim=0pt 2259pt 1807pt 0pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=1807pt 2259pt 0pt 0pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=0pt 1695pt 1807pt 564pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=1807pt 1695pt 0pt 564pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=0pt 1131pt 1807pt 1128pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=1807pt 1131pt 0pt 1128pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=0pt 567pt 1807pt 1692pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=1807pt 567pt 0pt 1692pt,clip,height=2.5cm]Fig-22-3)

### Exemplo de execução

![]([trim=0pt 3pt 1807pt 2256pt,clip,height=2.5cm]Fig-22-3)


# Procedimento `bfs`

### Procedimento `bfs`

```
bfs(G, s)
 1 for cada vértice u em G.V - {s}
 2   u.d = infinito
 3   u.pai = nil
 4   u.cor = branco
 5 s.d = 0
 6 s.pai = nil
 7 s.cor = cinza
 8 Q = {}
 9 Q.add(s)
10 while Q != {}
11   u = Q.remove()
12   for cada vértice v em G.adj[u]
13     if v.cor == branco
14       v.d = u.d + 1
15       v.pai = u
16       v.cor = cinza
17       Q.add(v)
18   u.cor = preto
```

# Análise do tempo de execução do `bfs`

### Análise do tempo de execução do `bfs`

-   Análise agregada \pause

-   O teste da linha 13 garante que cada vértice é colocado na fila no máximo
    uma vez, e portanto, é retirado da fila no máximo uma vez

-   As operações de colocar e retirar da fila demoram $O(1)$, assim, o tempo
    total das operações com filas é $O(V)$

-   A lista de adjacência de cada vértice é examinada apenas quando o vértice é
    retirado da fila, desta forma, no máximo uma vez

-   Como a soma dos comprimentos das listas de adjacências é $\Theta(E)$, o
    tempo para percorrer todas as listas é no máximo $O(E)$

-   O tempo de inicialização é $O(V)$

-   Tempo total de execução do `bfs` é $O(V + E)$

# Árvore primeiro na extensão

### Árvore primeiro na extensão

<!-- FIXME: usar árvore primeiro na extensão ou árvore primeiro na largura? !-->

-   `bfs` constrói uma árvore primeiro na extensão

-   A árvore é definida pelo campo pai ($\pi$) em cada vértice

-   Para um grafo $G=(V, E)$ e um vértice de origem $s$, definimos o **subgrafo
    predecessor** de $G$ como $G_\pi=(V_\pi, E_\pi)$ onde

    -   $V_\pi = \{v \in V: v.\pi \neq \text{NIL} \} \cup \{s\}$

    -   $E_\pi = \{(v.\pi, v):v \in V_\pi - \{s\}\}$

    \pause

-   O subgrafo predecessor $G_\pi$ é uma árvore primeiro na extensão

    -   $V_\pi$ consiste nos vértices acessíveis a partir de $s$

    -   Para todo $v \in V_\pi$, existe um caminho único simples desde $s$ até
        $v$ em $G_\pi$, que também é um caminho mais curto de $s$ até $v$ em
        $G$

-   Uma árvore primeiro na extensão é de fato uma árvore, pois é conexa e
    $|E_\pi| = |V_\pi| - 1$

### Árvores primeiro na extensão

```
imprimir-caminho(G, s, v)
1  if v == s
2    imprimir s
3  else if v.pai == nil
4    imprimir "nenhum caminho existente de" s "para" v
5  else
6    imprimir-caminho(G, s, v.pai)
7    imprimir v
```

-   Executado em tempo \pause linear no número de vértices no caminho impresso,
    pois cada chamada recursiva é feita para um caminho com um vértice menor que
    o atual

# Referências

### Referências

-   Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.2.


<!-- vim: set spell spelllang=pt_br: -->
