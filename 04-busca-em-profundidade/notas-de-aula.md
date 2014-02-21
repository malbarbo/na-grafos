---
title: Busca em profundidade
template: slide.tex
---

# Introdução

### Introdução

-   Procurar "mais fundo" no grafo sempre que possível

-   As arestas são exploradas a partir do vértices $v$ mais recentemente
    descoberto que ainda tem arestas inexploradas saindo dele

-   Quando todas as arestas de $v$ são exploradas, a busca regressa para
    explorar as arestas que deixam o vértice a partir do qual $v$ foi
    descoberto

-   Este processo continua até que todos os vértices acessíveis a partir da
    origem tenham sidos descobertos

-   Se restarem vértices não descobertos, a busca se repetirá para estes
    vértices

### Introdução

-   Durante a execução do algoritmo, diversos atributos são definidos para os
    vértices

-   Quando um vértice $v$ é descoberto a partir de um vértice $u$, o campo
    predecessor $v.\pi = u$ é definido

-   Cada vértice é inicialmente branco, o vértice é marcado de cinza quando é
    descoberto e marcado de preto quando é terminado (sua lista de adjacências
    é completamente examinada)

-   Cada vértice tem dois carimbos de tempo $v.d$ (quando o vértice é
    descoberto) e $v.f$ (quando o vértice é terminado)

<!-- Gerado com bin/split-image clrs/Chapter\ 22/Fig-22-4.pdf 699 513 4 4 height=4.0cm  !-->

# Exemplo de execução

### Exemplo de execução

![]([trim=0pt 1898pt 2709pt 0pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=903pt 1898pt 1806pt 0pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=1806pt 1898pt 903pt 0pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=2709pt 1898pt 0pt 0pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=0pt 1266pt 2709pt 632pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=903pt 1266pt 1806pt 632pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=1806pt 1266pt 903pt 632pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=2709pt 1266pt 0pt 632pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=0pt 634pt 2709pt 1264pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=903pt 634pt 1806pt 1264pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=1806pt 634pt 903pt 1264pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=2709pt 634pt 0pt 1264pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=0pt 2pt 2709pt 1896pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=903pt 2pt 1806pt 1896pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=1806pt 2pt 903pt 1896pt,clip,height=4.0cm]Fig-22-4)

### Exemplo de execução

![]([trim=2709pt 2pt 0pt 1896pt,clip,height=4.0cm]Fig-22-4)



# Procedimento `dfs`

### Procedimento `dfs`

```
dfs(G)
 1 for cada vértice u em G.V
 2   u.cor = branco
 3   u.pai = nil
 4 tempo = 0
 5 for cada vértice u em G.V
 6   if u.cor == branco
 7     dfs-visit(u)

dfs-visit(u)
 1 tempo = tempo + 1
 2 u.cor = cinza
 3 u.d = tempo
 4 for cada vértice v em u.adj
 5   if v.cor == branco
 6     v.pai = u
 7     dfs-visit(v)
 8 u.cor = preto
 9 tempo = tempo + 1
10 u.f = tempo
```

# Análise do tempo de execução do `dfs`

### Análise do tempo de execução do `dfs`

-   Os loops nas linhas 1 a 3 e nas linhas 5 a 7 de `dfs` demoram tempo
    $\Theta(V)$, sem contar o tempo das chamadas a `dfs-visit`

-   Usamos a análise agregada

-   O procedimento `dfs-visit` é chamado exatamente uma vez para cada vértice,
    isto porque `dfs-visit` é chamado para os vértices brancos, e no início de
    `dfs-visit` o vértice é pintado de cinza

-   Durante a execução de `dfs-visit(v)`, o laço nas linhas 4 a 7 é executado
    $|v.adj|$ vezes, como $\sum_{v \in V} |v.adj| = \Theta(E)$, o custo total
    da execução das linhas 4 a 7 de `dfs-visit` é $\Theta(E)$ \pause

-   Portanto, o tempo de execução do `dfs` é $\Theta(V + E)$

# Floresta primeiro na profundidade

### Floresta primeiro na profundidade

-   O procedimento \texttt{dfs} constrói uma floresta primeiro na profundidade,
    contendo diversas árvores primeiro na profundidade

-   Para um grafo $G=(V, E)$, definimos o **subgrafo predecessor** de uma busca
    primeiro na profundidade de $G$ como o grafo $G_\pi=(V, E_\pi)$ onde

    -   $E_\pi = \{(v.\pi, v):v \in V \text{ e } v.\pi \not = \text{NIL} \}$

-   As arestas em $E_\pi$ são **arestas da árvore**

# Propriedades

### Propriedades

-   Teorema 22.7 (Teorema do parênteses)

    -   Para dois vértices quaisquer $u$ e $v$, exatamente uma das três
        condições a seguir é verdadeira

        -   Os intervalos $[u.d, u.f]$ e $[v.d, v.f]$ são disjuntos e nem $u$ e
            nem $v$ são descendentes um do outro na floresta primeiro na
            profundidade

        -   O intervalo $[u.d, u.f]$ está contido inteiramente no intervalo
            $[v.d, v.f]$ e $u$ é descendente de $v$ em uma árvore primeiro na
            profundidade

        -   O intervalo $[v.d, v.f]$ está contido inteiramente no intervalo
            $[u.d, u.f]$ e $v$ é descendente de $u$ em uma árvore primeiro na
            profundidade

    -   Veja a prova no livro

### Propriedades

![22-5]([width=5cm]Fig-22-5)

### Classificação das arestas

-   Podemos definir quadro tipos de arestas em termos da floresta primeiro na
    profundidade $G_\pi$

    -   **Arestas da árvore**, são as arestas na floresta primeiro na
        profundidade chamada $G_\pi$. Uma aresta $(u, v)$ é uma aresta da árvore
        se $v$ foi descoberto primeiro pela exploração da aresta $(u, v)$

    -   **Arestas de retorno** são as arestas $(u, v)$ que conectam um vértice
        $u$ a um ancestral $v$ na árvore primeiro na profundidade

    -   **Arestas para frente** são as arestas $(u, v)$ que não são arestas da
        árvore e conectam o vértice $u$ a um descendente $v$ na árvore primeiro
        na profundidade

    -   **Arestas cruzadas** são todas as outras arestas


# Referências

### Referências

-   Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.3.


<!-- vim: set spell spelllang=pt_br: -->
