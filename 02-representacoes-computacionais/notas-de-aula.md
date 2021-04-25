---
# vim: set spell spelllang=pt_br:
# TODO: Adicionar exemplo de pseudo código de matriz de adjacência (exercício 22.1-3)
# TODO: Falar sobre tipo abstrado de dados para Grafos
title: Representações computacionais
---

## Introdução

Geralmente medimos o tamanho de um grafo $G = (V, E)$ em termos do número de vértices $|V|$ e do número de arestas $|E|$.

Dentro da notação assintótica, e apenas neste caso, o termo $V$ representará $|V|$, e o termo $E$, representará $|E|$.

Por exemplo, quando dizermos que o tempo de execução de um algoritmo é $O(VE)$, significa que o tempo de execução é $O(|V| \cdot |E|)$


## Introdução

Um grafo $G = (V, E)$ é

- **Esparso** se $|E|$ é muito menor que $|V|^2$

- **Denso** se $|E|$ está próximo de $|V|^2$


## Representação de grafos

No exemplo do número de Erdős representamos um grafo por uma lista de arestas. Na prática esta representação não é muito utilizada (Por quê?). \pause

As maneiras mais comuns para representar um grafo $G = (V, E)$ são

- Lista de adjacências

- Matriz de adjacências


## Exemplos

![22-1](imagens/Fig-22-1.pdf){width=11cm}

\pause

![22-2](imagens/Fig-22-2.pdf){width=11cm}


## Lista de adjacências

A **representação de lista de adjacências** consiste de um arranjo $Adj$ de $|V|$ listas, uma para cada vértice. \pause

Para cada $u \in V$, a lista de adjacências $Adj[u]$ contém todos os vértices (ou referências para os vértices) $v$, tal que $v$ é adjacente a $u$, isto é $(u, v) \in E$.


## Lista de adjacências

<div class="columns">
<div class="column" width="60%">
\includegraphics[trim=0cm 0cm 35cm 0cm,clip,width=8cm]{imagens/Fig-22-1.pdf}
\includegraphics[trim=0cm 0cm 35cm 0cm,clip,width=8cm]{imagens/Fig-22-2.pdf}
</div>
<div class="column" width="40%">
Qual é a soma dos comprimentos de todas as listas de adjacências?

- Se $G$ é um grafo orientado? \pause \newline $|E|$ \pause

- Se $G$ é um grafo não orientado? \pause \newline $2 |E|$ \pause

Qual é a quantidade de memória requerida? \pause \newline $\Theta(V + E)$
</div>
</div>


## Lista de adjacências

Vantagens \pause

- Flexível, é possível estender a representação para multigrafos

- A quantidade de memória é assintoticamente ótima (adequada para grafos esparsos) \pause

Desvantagem \pause

- Não existe nenhum modo rápido para determinar se uma dada aresta $(u, v)$ está presente no grafo.


## Matriz de adjacências

Na **representação de matriz de adjacências**, usamos uma matriz $A = (a_{ij})$, de tamanho $|V| \times |V|$, tal que

$$
a_{ij} = \begin{cases}
             1 \text{ se } (i, j) \in E\\
             0 \text{ caso contrário}
      \end{cases}
$$

Neste caso, supomos que os vértices são numerados $1, 2, \dots, |V|$


## Matriz de adjacências

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 84cm 0cm,clip,width=3.5cm]{imagens/Fig-22-1.pdf}
\includegraphics[trim=0cm 0cm 84cm 0cm,clip,width=3.5cm]{imagens/Fig-22-2.pdf}
</div>
<div class="column" width="30%">
\includegraphics[trim=84cm 0cm 0cm 0cm,clip,width=3.5cm]{imagens/Fig-22-1.pdf}
\includegraphics[trim=84cm 0cm 0cm 0cm,clip,width=3.5cm]{imagens/Fig-22-2.pdf}
</div>
<div class="column" width="40%">
Qual é quantidade de memória requerida? \pause

$\Theta(V^2)$ (independe de $|E|$). \pause

Adequada para grafos densos. \pause

Em um grafo não orientado, a matriz é igual a sua transposta, desta forma é possível usar apenas os elementos abaixo (ou acima) da diagonal principal.
</div>
</div>


## Matriz de adjacências

Vantagens \pause

- Simplicidade \pause

- Permite consultar se uma aresta faz parte do grafo em tempo constante \pause


Desvantagem \pause

- Uso excessivo da memória para grafos esparsos \newline


## Pseudo código

Nos pseudo códigos vamos tratar o conjunto de vértices, o conjunto de arestas e a lista de adjacências um atributos do grafo:

- $\attrib{G}{V}$ - conjunto de vértices

- $\attrib{G}{E}$ - conjunto de arestas

- $\attrib{G}{Adj}$ - arranjo com as listas de adjacências


## Pseudo código

Para fazer uma repetição passado por cada vértice vamos escrever:

\begin{codebox}
  \li \For each vertex $v \in \attrib{G}{V}$ \Do
  \li \dots
      \End
\end{codebox}

\pause

Para fazer uma repetição passando por cada vértice adjacente a um vértice $u$ vamos escrever:

\begin{codebox}
  \li \For each vertex $v \in \attrib{G}{Adj[u]}$ \Do
  \li \dots
      \End
\end{codebox}


## Implementação

Como podemos implementar a representação de matriz de adjacências? \pause

- Diretamente usando matriz na linguagem de programação \pause

- Criar uma abstração para matriz transposta e economizar memória na representação de grafos não orientados


## Implementação

Como podemos implementar a representação de lista de adjacências? \pause

- De muitas formas, depende da linguagem, do algoritmo, etc \pause

- Uma forma simples é representar os vértices com inteiros no intervalo de $0$ a $V - 1$ é a lista de adjacências com lista de listas (arranjo de arranjos), sem criar nenhum abstração \pause

- Ou criar uma abstração simples para deixar o código mais legível e evitar que o grafo seja alterado de forma inconsistente \pause

- Ou ainda usar orientação objeto e criar classes para grafo, vértice, aresta, etc.


## Implementação simples

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0cm 0cm 35cm 0cm,clip,width=6.5cm]{imagens/Fig-22-1.pdf}
\scriptsize
\pause
Como representar esse grafo em Python? \pause

```python
g = [
    [1, 4],
    [0, 4, 2, 3],
    [1, 3],
    [1, 4, 2],
    [3, 0, 1],
]
```

</div>
<div class="column" width="50%">
\scriptsize
\pause
Como fazer uma repetição passando por cada vértice? \pause

```python
for v in range(len(g)): # v = 0, 1, 2, ..., len(g) - 1
    ...
```

\pause
Como fazer uma repetição passando por cada vértice adjacente de um vértice $u$? \pause

```python
u = 2
for v in g[u]: # v = 1, 3
    ...
```

\pause
Como calcular o número de arestas? \pause

```python
m = sum(len(adjacentes) for adjacentes in g) / 2
```
</div>
</div>


## Implementação simples

<div class="columns">
<div class="column" width="55%">
\includegraphics[trim=0cm 0cm 35cm 0cm,clip,width=6.5cm]{imagens/Fig-22-2.pdf}
\scriptsize

\pause
Como representar esse grafo em C? \pause

```c
// Usamos -1 para denotar o fim de uma lista de adj
// Usamos NULL para denotat o fim da lista de adjs
int* g[7] = {
    (int[]) { 1, 3, -1 },
    (int[]) { 4, -1 },
    (int[]) { 5, 4, -1 },
    (int[]) { 1, -1 },
    (int[]) { 3, -1 },
    (int[]) { 5, -1 },
    NULL,
};
```
</div>
<div class="column" width="45%">
\scriptsize
\pause
Como fazer uma repetição passando por cada vértice? \pause

```c
for (int v = 0; g[v] != NULL; v++) {
    // v = 0, 1, 2, ..., n - 1
    ...
}
```

\pause
E uma repetição por cada vértice adjacente de um vértice $u$? \pause

```c
int u = 2;
for (int i = 0; g[u][i] != -1; i++) {
    int v = g[u][i]; // 5, 4
    ...
}
```

\pause ou

```c
int u = 2;
for (int* v = g[u]; *v != -1; v++) {
    ... *v // 5, 4
}
```

\pause
Como calcular o número de arestas? \pause Fica como exercício.

</div>
</div>


## Atributos

Muitos algoritmos que operam em grafos precisam manter atributos para vértices e/ou arestas (como o número de Erdős para cada vértice).  \pause

Em pseudo código indicamos os atributos da seguinte maneira:

- $v.d$, atributo $d$ do vértice $v$

- $(u, v).f$, atributo $f$ da aresta $(u, v)$


## Atributos

Como estes atributos podem ser implementados? \pause

- Depende da linguagem de programação, algoritmo, etc \pause

- Os atributos da arestas podem ser armazenados diretamente na lista ou matriz de adjacência \pause

- Se os vértices são enumerados de $1..|V|$ os atributos podem ser representados em arranjos, tais como $d[1..|V|]$ \pause

- Atributos de vértices podem ficar nos registros que representam os vértices \pause

- Atributos de arestas podem ficar nos registros que representam as arestas


## Exemplos de implementação

Veja na página da disciplina.


## Exercício

22.1-1) Dada uma representação de lista de adjacências de um grafo orientado, qual o tempo necessário para computar o grau de saída de todo o vértice? Qual o tempo necessário para computar os graus de entrada?

## Resolução 22.1-1

Antes de fazer a análise do tempo de execução é necessário escrever o pseudo código do algoritmo.

## Resolução 22.1-1

\begin{codebox}
  \Procname{$\proc{graus-de-saida(G)}$}
  \li \For each vertex $v \in \attrib{G}{V}$ \Do
  \li   $\attrib{v}{grau-de-saida} \gets 0$
      \End
  \li \For each vertex $u \in G.V$ \Do
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     $\attrib{u}{grau-de-saida} \gets \attrib{u}{grau-de-saida} + 1$
        \End
      \End
\end{codebox}

\pause

\small

**Análise do tempo de execução**

- O laço das linhas 1 a 2 tem tempo de execução $\Theta(V)$
- A cada interação do laço da linha 3, o laço das linha 4 a 5 é executado
  $|\attrib{G}{Adj}[u]|$ vezes, como o laço das linha 4 a 5 é executado uma vez
  para cada vértice, temos que seu tempo de execução é $\sum_{u \in
  \attrib{G}{V}} |\attrib{G}{Adj}[u]| = |E|$. Ou seja, o tempo de execução das
  linhas 3 a 5 é $\Theta(V + E)$
- Portanto, o tempo de execução do procedimento $\proc{graus-de-saida}$ é
  $\Theta(V + E)$


## Resolução 22.1-1

\begin{codebox}
  \Procname{$\proc{graus-de-entrada(G)}$}
  \li \For each vertex $u \in \attrib{G}{V}$ \Do
  \li   $\attrib{u}{grau-de-entrada} \gets 0$
      \End
  \li \For each vertex $u \in G.V$ \Do
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     $\attrib{v}{grau-de-entrada} \gets \attrib{v}{grau-de-entrada} + 1$
        \End
      \End
\end{codebox}

\pause

**Análise do tempo de execução**

- Mesmo do procedimento $\proc{graus-de-saida}$


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.1.
