---
# vim: set spell spelllang=pt_br:
title: Ciclos eulerianos e o problema do carteiro chinês
---

## Introdução

Um **caminho euleriano** é um caminho que usa cada aresta do grafo exatamente
uma vez

Um **ciclo euleriano** é um ciclo que usa cada aresta do grafo exatamente uma
vez

Um grafo que contém um ciclo euleriano é chamado de **grafo euleriano**

Um grafo que contém um caminho euleriano, mas não contém um ciclo euleriano
é chamado de **grafo semi-euleriano**


## Exemplos

![](imagens/exemplo-grafo-euleriano.pdf)


## Propriedades

**Lema 1**

Dado um grafo não orientado conexo $G = (V, E)$ com todos os vértices de grau
par, então qualquer par de vértices $u, v \in G$ faz parte de um ciclo sem
arestas repetidas.


## Propriedades

**Prova (por contradição)**

Suponha que exista um par de vértices $u, v \in G$ que não admita um ciclo em
comum. Como o grafo é conexo, então existe um caminho $p$ de $u$ para $v$. Isto
implica que deve existir uma aresta $(x, y)$ no caminho $p$ cuja a remoção
torna o grafo desconexo, caso contrário existiria um outro caminho alternativo
$p'$ de $u$ para $v$ disjunto de $p$ (formando um ciclo com $u$ e $v$). A
remoção da aresta $(x, y)$ gera dois componentes, sendo que $x$ e $y$ pertencem
a componentes distintos. Desta forma, $x$ e $y$ são os únicos vértices de grau
ímpar em seus componentes, mas isto é uma contradição, pois o número de
vértices de grau ímpar em um (sub)grafo deve ser par.


## Propriedades

**Teorema 1**

Um grafo não orientado conexo $G$ é um grafo euleriano se e somente se todo
vértice de $G$ tem grau par.

## Propriedades

**Prova (ida)**

Seja $G = (V, E)$ um grafo euleriano e seja $p$ um ciclo euleriano de $G$. Cada
ocorrência de um vértice $v \in V$ em $p$, implica uma aresta que chega em $v$
e uma aresta que sai de $v$. Como todas as arestas de $E$ fazem parte de $p$,
o número de arestas incidentes em cada vértice é par.


## Propriedades

**Prova (volta)**

Seja $G = (V, E)$ um grafo com todos os vértices de grau par. Na construção de
um caminho em $G$ sempre é possível chegar e sair de um vértice por arestas
ainda não utilizadas. Ou seja, é possível construir um ciclo arbitrário $C$ a
partir de um vértice qualquer $v$ (Lema 1). Se $C$ contém todas as arestas de
$G$, temos um ciclo euleriano. Senão, construímos um grafo $G'$, tal que
$\attrib{G'}{E} = \attrib{G}{E} - \{$arestas de $C \}$. Em $G'$ todos os
vértices tem grau par, e pelo menos um vértice de $C$ está em $\attrib{G'}{V}$
e tem grau maior que 0 (senão o grafo não seria conexo). Recomeçamos este
processo para o grafo $G'$, começando com um vértice $v' \in C$ com grau maior
que 0 e construímos um ciclo $C'$. Os ciclos $C$ e $C'$ podem ser unidos para
formar um único ciclo. Continuando este processo até acabar as arestas do
grafo, obteremos necessariamente um ciclo único que contém todas as arestas de
$G$.


## Algoritmo de Hierholzer (primeira versão)

<div class="columns">
<div class="column" width="55%">
\small
\begin{codebox}
    \Procname{$\proc{hierholzer-1}(G)$}
    \li $G' = (G.V, G.E)$
    \li $v_0 =$ um vértice de $G$
    \li $C =$ caminho contendo apenas $v_0$
    \li \While $\attrib{G'}{E} \not = \emptyset$ \Do
    \li     $u =$ vértice em $C$ tal que $d(u) > 0$ em $G'$
    \li     $U =$ ciclo em $G'$ que contém $u$
    \li     $C = C$ substituindo $u$ por $U$
    \li     $\attrib{G'}{E} = E$ - $\{$ arestas de $U \}$
        \End
    \li \Return $C$
\end{codebox}
</div>
<div class="column" width="45%">
\pause

Análise do tempo de execução

- As operações da linhas 5 e 7 podem ser implementadas em tempo constante
  (usando lista duplamente encadeada), portanto o total destas linhas é $O(E)$
- O tempo total das linhas 6 e 8 (usando análise agregada) é $O(E)$
- Portanto, o tempo de execução do algoritmo é $O(E)$
</div>
</div>


## Exemplo de execução do procedimento \proc{hierholzer-1}

![](imagens/exemplo-execucao-hierholzer.pdf)


## Algoritmo de Hierholzer (primeira versão)

O procedimento \proc{hierholzer-1} foi derivado diretamente da prova do Teorema
1, e por isto, podemos verificar facilmente que ele é correto. No entanto, a
sua implementação é um pouco trabalhosa

A seguir, apresentamos uma versão do algoritmo de Hierholzer que utiliza uma
pilha para auxiliar na construção do ciclo, o que facilita a implementação. No
entanto a prova de corretude não é tão simples (fica como exercício)


## Algoritmo de Hierholzer (segunda versão)

\begin{codebox}
    \Procname{$\proc{hierholzer-2}(G)$}
    \li $s = \{$ um vértice de $G$ $\}$ \Comment pilha
    \li $C = \{\}$ \Comment lista
    \li \While $s \not = \emptyset$ \Do
    \li     $u = \proc{pop}(s)$
    \li     $\proc{push-front}(C, u)$
    \li     \While $\attrib{G}{adj[u]} \not = \emptyset$ \Do
    \li         $v = \proc{pop-front(\attrib{G}{adj[u]})}$
    \li         \If $(u, v)$ não foi visitada \Then
    \li             $\proc{push}(S, u)$
    \li             marcar a aresta $(u, v)$ como visitada
    \li             $u = v$
                \End
            \End
        \End
    \li \Return $C$
\end{codebox}



## Algoritmo de Hierholzer (segunda versão)

Funcionamento

- $s$ é o ciclo temporário

- $C$ é o ciclo definitivo

- O laço da linha 6 constrói um ciclo que começa e termina com o vértice
  desempilhado na linha 4

- No caso de grafos não orientados, a remoção da aresta $(u, v)$ da lista de
  adjacências $u$ na linha 7 não garante que ela não será mais visitada (ela
  ainda está na lista de $v$). Utilizamos a marcação da linha 10
  e a verificação da linha 8 para evitar que arestas sejam visitadas mais que
  uma vez


## Algoritmo de Hierholzer (segunda versão)

Análise do tempo de execução

- Usamos análise agregada

- Cada aresta é removida da lista de adjacências duas vezes. A operação de
  remoção pode ser implementada em tempo constante, desta forma, o tempo total
  das operações de remoção é $\Theta(E)$

- As operações \proc{pop}, \proc{push}, \proc{push-front} e \proc{pop-front}
  podem ser implementadas com tempo constante. Como o grafo de entrada é conexo
  e portanto $E > V - 1$, a quantidade de vezes que estas operações são
  realizadas é limitado por $E$, desta forma, o tempo total gasto com estas
  operações é $O(E)$

- Portanto, o tempo de execução do algoritmo é $O(E)$



## O problema do carteiro chinês

Dado um grafo conexo com peso nas arestas, o **problema do carteiro chinês**
consiste em encontrar um ciclo de peso mínimo que passe por cada aresta pelo
menos uma vez

\pause

Aplicações

- Entrega de correspondência

- Coleta de lixo

- Nebulização no combate a dengue


## O problema do carteiro chinês

Grafo euleriano

- Aplicar o algoritmo de Hierholzer

\pause

Grafo não euleriano

- Transformar o grafo em euleriano adicionando arestas artificiais e aplicar
  o algoritmo de Hierholzer


## O problema do carteiro chinês

Se o grafo for semi-euleriano, adicionar uma aresta artificial que representa o
caminho mínimo entre os dois vértices de grau ímpar (o caminho mínimo pode ser
encontrado usando o algoritmo de Dijkstra)

\pause

Se o grafo tiver 4 ou mais vértices de grau ímpar

- Montar um grafo completo com os vértices de grau ímpar, onde cada aresta
  representa o menor caminho entre o par de vértices (algoritmo de
  Floyd-Warshall)

- Encontrar a melhor combinação de pares de vértices (emparelhamento perfeito,
  algoritmo de Edmonds de complexidade polinomial)


## Referências

Caminho euleriano. Wikipédia. <https://en.wikipedia.org/wiki/Eulerian_path>

Problema do carteiro chinês. Wikipédia. <https://en.wikipedia.org/wiki/Route_inspection_problem>
