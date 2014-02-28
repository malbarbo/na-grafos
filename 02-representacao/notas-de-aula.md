---
title: Representação
template: slide.tex
---

# Introdução

### Introdução

-   Geralmente medimos o tamanho de um grafo $G = (V, E)$ em termos do número de
    vértice $|V|$ e do número de arestas $|E|$

    -   Dentro da notação assintótica, o termo $V$ representará $|V|$, e o termo
        $E$, representará $|E|$

-   Um grafo $G = (V, E)$ é

    -   **Esparso** se $|E|$ é muito menor que $|V|^2$

    -   **Denso** se $|E|$ está próximo de $|V|^2$

# Representação de grafos

### Representação de grafos

-   Existem duas maneiras padrão para representar um grafo $G = (V, E)$

    -   Lista de adjacências

    -   Matriz de adjacências

## Lista de adjacências

### Representação de grafos

-   Lista de adjacências

    -   A **representação de lista de adjacências** consiste de um arranjo $Adj$
        de $|V|$ listas, uma para cada vértice

    -   Para cada $u \in V$, a lista de adjacências $Adj[u]$ contém (ponteiros
        para) todos os vértices $v$ tal que $(u,v) \in E$

    -   No pseudo do código vamos tratar o arranjo $Adj$ como um atributo do
        grafo, assim como $V$ e $E$

        -   $G.V$ - conjunto de vértices

        -   $G.E$ - conjunto de arestas

        -   $G.Adj$ - arranjo com as listas de adjacências

### Representação de grafos

![22-1](Fig-22-1)

\pause

![22-2](Fig-22-2)

### Representação de grafos

-   Lista de adjacências

    -   Qual é a soma dos comprimentos de todas as listas de adjacências? \pause

        -   Se $G$ é um grafo orientado, a soma é $|E|$ \pause

        -   Se $G$ é um grafo não orientado, a soma é $2 |E|$ \pause

    -   Qual é a quantidade de memória requerida? \pause $\Theta(V + E)$ \pause

    -   Adequada para grafos esparsos \pause

    -   Vantagens \pause

        -   Flexível, é possível adaptar a representação para variantes de grafos

        -   A quantidade de memória é assintoticamente ótima \pause

    -   Desvantagem \pause

        -   Não existe nenhum modo rápido para determinar se uma dada aresta
            $(u, v)$ está presente no grafo

## Matriz de adjacências

### Representação de grafos

-   Matriz de adjacências

    -   Na **representação de matriz de adjacências**, supomos que os vértices
        são numerados $1, 2, \dots, |V|$

    -   A representação consiste em uma matriz $|V| \times |V| A = (a_{ij})$ tal
        que

        $$
        a_{ij} = \begin{cases}
                     1 \text{ se } (i, j) \in E\\
                     0 \text{ caso contrário}
                 \end{cases}
        $$


### Representação de grafos

![22-1](Fig-22-1)

\pause

![22-2](Fig-22-2)

### Representação de grafos

-   Matriz de adjacências

    -   Qual é quantidade de memória requerida? $\pause \Theta(V^2)$. A
        quantidade de memória independe de $E$ \pause

    -   Em um grafo não orientado, a matriz é igual a sua transposta, desta
        forma é possível usar apenas os elementos abaixo (ou acima) da diagonal
        principal \pause

    -   Adequada para grafos densos \pause

    -   Vantagens \pause

        -   Simplicidade

        -   Permite consultar se uma aresta faz parte do grafo em tempo
            constante \pause

    - Desvantagens \pause

        -   Memória


## Atributos

### Atributos

-   Muitos algoritmos que operam em grafos precisam manter atributos para
    vértices e/ou arestas \pause

-   Nos códigos, indicamos os atributos como

    -   $v.d$, atributo $d$ do vértice $v$

    -   $(u, v).f$, atributo $f$ da aresta $(u, v)$

    \pause

-   Como estes atributos podem ser implementados? \pause

    -   Depende da linguagem de programação, algoritmo, etc \pause

    -   Os atributos podem ser armazenado diretamente na lista ou matriz de
        adjacência

    -   Se os vértices são enumerados de $1..|V|$ os atributos podem ser
        representados em arranjos, tais como $d[1..|V|]$

    -   Atributos de vértices podem ficar nos registros que representam os
        vértices

    -   Atributos de arestas podem ficar nos registros que representam as
        arestas

## Exemplos de implementação

### Exemplos de implementação

Veja o arquivo 02-representacao-exemplo.zip

# Exercícios


### Exercícios

-   [22.1-1] Dada uma representação de lista de adjacências de um grafo
    orientado, qual o tempo necessário para computar o grau de saída de todo
    o vértice? Qual o tempo necessário para computar os graus de entrada?

### Resolução 22.1-1

-   Antes de fazer a análise do tempo de execução é necessário escrever
    o pseudo código do algoritmo

### Resolução 22.1-1

```
computa-graus-de-saida(G)
 1 for u in G.V
 2   u.grau-de-saida = 0
 3 for u in G.V
 4   for v in G.Adj[u]
 5       u.grau-de-saida += 1
```
    
\pause

-   Análise do tempo de execução

    -   O laço das linhas 2 a 3 demora $\Theta(V)$

    -   O laço da linha 4 (sem contar as linhas 5 e 6) demora $\Theta(V)$

    -   A cada interação do laço da linha 4, o laço das linhas
        5 a 6 é executado $|G.Adj[u]|$ vezes, como o laço da linha
        4 é executado uma vez para cada vértices, temos que o laço das linhas
        5 a 6 é executado $\sum_{u \in G.V} |G.Adj[u]| = |E|$. Ou seja, o tempo
        de execução das linha 5 e 6 é $\Theta(E)$

    -   Portanto, o tempo de execução do procedimento `computa-graus-saida`
        é $\Theta(V + E)$


### Resolução 22.1-1

```
computa-graus-de-entrada(G)
 1 for u in G.V
 2   u.grau-de-entrada = 0
 3 for u in G.V
 4   for v in G.Adj[u]
 5     v.grau-de-entrada += 1
```

-   Análise do tempo de execução

    -   Mesmo do procedimento `computa-graus-de-saida`


<!-- TODO: Adicionar exemplo de pseudo código de matriz de adjacência (exercício 22.1-3)  !-->
<!-- TODO: Falar sobre tipo abstrado de dados para Grafos  !-->

# Referências

### Referências

-   Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.1.


<!-- vim: set spell spelllang=pt_br: -->
