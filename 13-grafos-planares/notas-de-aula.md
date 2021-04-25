---
# vim: set spell spelllang=pt_br:
title: Grafos planares
---

## Introdução

<!-- TODO: falar das aplicações !-->

<!-- TODO: falar mais dos problemas de planarização !-->

Uma **imersão** de um grafo $G$ em uma superfície $S$ é uma representação
geométrica (desenho) de $G$ em $S$ tal que dois vértices distintos não ocupam
o mesmo lugar em $S$ e não existe cruzamento de arestas, a não ser nos extremos
quando duas arestas são adjacentes.

\pause

Um grafo $G$ é **planar** se ele tem imersão no plano ($\mathbb{R}^2$)

- As regiões limitadas por uma imersão planar são chamadas de **faces**

- Todo imersão planar têm uma face ilimitada denominada de **face externa**


## Exemplos

![](imagens/exemplo-grafo-planar.pdf)


## Propriedades

<!-- TODO: definir o que é fronteira !-->
<!-- TODO: substituir ascii art por figura !-->

O **grau de uma face** é o tamanho de um caminho mínimo na fronteira da face

```text
   b ----- d ----- f ------- g
   |       |       | 3       |
   |   1   |   2   |    i    |  4
   |       |       |    |    |
   a ----- c ----- e -- h -- j
```

- A fronteira da face 2 tem as arestas $df, fe, ec, de$, então a face 2 tem
  grau 4

- A fronteira da face 3 tem as arestas $fg, gj, jh, hi, he, ef$, mas qualquer
  percurso na fronteira da face 3 deverá passar pela aresta $ih$ duas vezes,
  como por exemplo, $fg, gj, jh, hi, ih, he, ef$. Portanto, o grau da face
  3 é 7.


## Propriedades

**Teorema 1 - Fórmula de Euler**

Seja $G = (V, E)$ um grafo planar e conexo com $f$ faces, então $|V| + f = |E| + 2$.

\pause

A discussão da prova foi feita em sala. Veja as referências.


## Propriedades

**Corolário 1**

Seja $G = (V, E)$ um grafo planar e conexo com $|V| \ge 3$, então $|E| \le 3|V| - 6$

## Propriedades

**Prova**

- Seja $W$ a soma dos graus das faces do grafo, temos que $W = 2|E|$. Cada
  aresta separa duas faces, com exceção das arestas prego (como as arestas $ih$
  do exemplo anterior), mas neste caso a aresta é contada duas vezes no grau da
  face

- Cada face tem grau pelo menos 3, portanto $3f \le W$, como $W = 2|E|$, então
  $3f \le 2|E|$

- Substituindo $f$ por $\frac{2|E|}{3}$ na fórmula de Euler, obtemos
    $$|V| + \frac{2|E|}{3} \le |E| + 2$$
    $$3|V| + 2|E| \le 3|E| + 6$$
    $$|E| \le 3|V| - 6$$


## Propriedades

Podemos usar o Corolário 1 para mostrar que o $K_5$ é não planar. O $K_5$ tem
5 vértices e 10 arestas, desta foma $3|V| - 6 = 9$, o que implica que
$|E| \le 3|V| - 6$ é falso. Portanto, o $K_5$ é não planar.

![](imagens/k5.pdf){width=4cm}


## Propriedades

**Corolário 2**

Seja $G = (V, E)$ um grafo planar e conexo com $|V| \ge 3$ e sem ciclos de
tamanho 3, então $|E| \le 2|V| - 4$.


## Propriedades

**Prova**

- Semelhante a do corolário 1

- Cada face tem grau pelo menos 4 (não tem ciclos de tamanho 3), portanto, $4f
  \le W$, como $W = 2|E|$, então $4f \le 2|E|$ e $2f \le |E|$

- Substituindo $f$ por $\frac{|E|}{2}$ na fórmula de Euler, obtemos
    $$|V| + \frac{|E|}{2} \le |E| + 2$$
    $$2|V| + |E| \le 2|E| + 4$$
    $$|E| \le 2|V| - 4$$


## Propriedades

O $K_{3,3}$ não tem faces (ciclos) de tamanho 3. Podemos usar o Corolário
2 para mostrar que o $K_{3,3}$ é não planar. O $K_{3,3}$ tem 6 vértices
e 9 arestas, desta foma $9 \le 2 \times 6 - 4 = 8$, o que não é verdade.
Portanto, o $K_{3, 3}$ é não planar.

![](imagens/k33.pdf){width=4cm}


## Propriedades

Uma **operação de subdivisão** de uma aresta $e = (u, v)$ é uma substituição de
$e$ por um novo vértice $w$ e duas novas arestas $(u, w)$ e $(w, v)$

\pause

Uma **subdivisão** de um grafo $G$ é um grafo $H$ que pode ser obtido a partir
de $G$ por uma sequência finita de operações de subdivisão de arestas


## Propriedades

**Teorema de Kuratowski**

Um grafo $G$ é planar se, e somente se, ele não contém uma subdivisão do $K_{3,
3}$ e do $K_5$.


## Exemplo

![](imagens/exemplo-petersen.pdf){width=8cm}

Veja [esta](https://en.wikipedia.org/wiki/File:Kuratowski.gif) animação
mostrando a subdivisão.


## Métodos de teste de planaridade

Dado um grafo $G = (V, E)$, o **problema do teste de planaridade** consiste em
determinar se $G$ é planar. \pause

Existem diversos algoritmos com tempo de execução $O(V + E)$

- Algoritmo clássico baseado em adição de caminhos (Hopcroft e Tarjan, 1974)

- Baseado em adição de vértices (Lempel, Even e Cederbaum, 1967, melhorado por
  Eve e Tarjan, 1976, e Booth e Lueker)

- Baseado em adição de arestas (Boyer e Myrvold, 2004), considerado como
  estado da arte


## Métodos de teste de planaridade

Estes algoritmos são bastante elaborados, difíceis de entender e implementar.
Para grafos pequenos, podemos testar manualmente se um grafo é planar usando
o método heurístico círculo-corda.


## Método círculo-corda para teste de planaridade

O método círculo-corda consiste em

- Passo 1: Encontrar um ciclo que contém todos os vértices do grafo
  e desenhá-lo como um círculo

- Passo 2: O restante das arestas que não estão círculo, chamadas de cordas,
  deve ser desenhadas ou do lado de dentro ou do lado de fora do círculo, de
  maneira que o desenho seja planar

\pause

Observe-se que este é um método heurístico, nem todos os grafos planares
podem ser desenhados com este método.


## Exemplo

![](imagens/exemplo-metodo-circulo-corda.pdf){width=10cm}


## Medidas de não planaridade

Quando um grafo não é planar, uma questão interessante é: o quão longe de ser
planar o grafo está?

Algumas medidas de não planaridade

- Número mínimo de cruzamento de arestas para um desenho no plano ($cr(G)$ - o *crossing number* de $G$)

- Número mínimo de arestas cuja remoção do grafo resulta em um grafo planar
  ($sk(G)$ - a *skewness* de $G$)

- Número mínimo de operações de divisões de vértices que obtêm um grafo planar
  ($sp(G)$ - o *splitting number* de $G$)


## Medidas de não planaridade

Pela definição destas medidas, podemos observar que $sp(G) \le sk(G) \le cr(G)$.

Os problemas de otimização relacionados com o número mínimo de cruzamento,
número mínimo de remoção de arestas e número mínimo de divisão de vértices são
NP-difícies.


## Referências

- [Grafos planares](http://mfleck.cs.illinois.edu/building-blocks/version-1.3/planargraphs.pdf).
    Livro Building Blocks for Theoretical Computer Science. Margaret M. Fleck.
    Capítulo 21.

- [Vídeo Planar Graphs](https://www.youtube.com/watch?v=xBkTIp6ajAg).

- Grafos planares. Wikipédia. <https://en.wikipedia.org/wiki/Planar_graph>

- Teste de planaridade. Wikipédia.
    <https://en.wikipedia.org/wiki/Planarity_testing>
