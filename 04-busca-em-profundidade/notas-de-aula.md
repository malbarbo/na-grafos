---
# vim: set spell spelllang=pt_br:
title: Busca em profundidade
---

## Introdução

- Procurar "mais fundo" no grafo sempre que possível (_Depth-first search_ -
  DFS em inglês)

- As arestas são exploradas a partir do vértices $v$ mais recentemente
  descoberto que ainda tem arestas inexploradas saindo dele

- Quando todas as arestas de $v$ são exploradas, a busca regressa para explorar
  as arestas que deixam o vértice a partir do qual $v$ foi descoberto

- Este processo continua até que todos os vértices acessíveis a partir da
  origem tenham sidos descobertos

- Se restarem vértices não descobertos, a busca se repetirá para estes vértices


## Introdução

- Durante a execução do algoritmo, diversos atributos são definidos para os
  vértices

- Quando um vértice $v$ é descoberto a partir de um vértice $u$, o campo
  predecessor $\attrib{v}{\pi} = u$ é definido

- Cada vértice é inicialmente branco, o vértice é marcado de cinza quando é
  descoberto e marcado de preto quando é terminado (sua lista de adjacências é
  completamente examinada)

- Cada vértice tem dois carimbos de tempo $\attrib{v}{d}$ (quando o vértice é
  descoberto) e $\attrib{v}{f}$ (quando o vértice é terminado)


<!-- Gerado com bin/split-image clrs/Chapter\ 22/Fig-22-4.pdf 699 513 4 4 height=4.0cm  !-->

## Exemplo de execução

\includegraphics[trim=0pt 1898pt 2709pt 0pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=903pt 1898pt 1806pt 0pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=1806pt 1898pt 903pt 0pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=2709pt 1898pt 0pt 0pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=0pt 1266pt 2709pt 632pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=903pt 1266pt 1806pt 632pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=1806pt 1266pt 903pt 632pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=2709pt 1266pt 0pt 632pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=0pt 634pt 2709pt 1264pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=903pt 634pt 1806pt 1264pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=1806pt 634pt 903pt 1264pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=2709pt 634pt 0pt 1264pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=0pt 2pt 2709pt 1896pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=903pt 2pt 1806pt 1896pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=1806pt 2pt 903pt 1896pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exemplo de execução

\includegraphics[trim=2709pt 2pt 0pt 1896pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}



## Procedimento \proc{DFS}

<div class="columns">
<div class="column" width="30%">
\scriptsize

\begin{codebox}
  \Procname{$\proc{DFS}(G)$}
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   $\attrib{u}{cor} \gets \const{branco}$
  \li   $\attrib{u}{\pi} \gets \const{nil}$
      \End
  \li $\id{tempo} \gets 0$
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   \If $\attrib{u}{cor} \isequal \const{branco}$ \Then
  \li     $\proc{dfs-visit}(G, u)$
        \End
      \End
\end{codebox}

\begin{codebox}
  \Procname{$\proc{DFS-Visit}(G, u)$}
  \li $\id{tempo} \gets \id{tempo} + 1$
  \li $\attrib{u}{d} \gets \id{tempo}$
  \li $\attrib{u}{cor} \gets \const{cinza}$
  \li \For $v \in \attrib{G}{Adj}[u]$ \Do
  \li   \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li     $\attrib{v}{\pi} \gets u$
  \li     $\proc{DFS-Visit}(G, v)$
        \End
      \End
  \li $\attrib{u}{cor} \gets \const{preto}$
  \li $\id{tempo} \gets \id{tempo} + 1$
  \li $\attrib{u}{f} \gets \id{tempo}$
\end{codebox}

</div>

<div class="column" width="70%">

\footnotesize

\pause

Tempo de execução \pause

- Os laços nas linhas 1 a 3 e nas linhas 5 a 7 de \proc{DFS} demoram tempo
  $\Theta(V)$, sem contar o tempo das chamadas a \proc{DFS-Visit}

- O procedimento \proc{DFS-Visit} é chamado exatamente uma vez para cada
  vértice, isto porque \proc{DFS-Visit} é chamado para os vértices brancos, e
  no início de \proc{DFS-Visit} o vértice é pintado de cinza

- Durante a execução de $\proc{DFS-Visit}(v)$, o laço nas linhas 4 a 7 é
  executado $\attrib{G}{Adj}[v]$ vezes, como $\sum_{v \in V}
  |\attrib{G}{Adj}[v]| = \Theta(E)$, o custo total da execução das linhas 4 a 7
  de \proc{DFS-Visit} é $\Theta(E)$

- Portanto, o tempo de execução do \proc{DFS} é $\Theta(V + E)$

</div>
</div>


## Floresta da busca em profundidade

- O procedimento \proc{DFS} constrói uma floresta da busca em profundidade
  (floresta DFS), contendo diversas árvores da busca em profundidade

- Para um grafo $G = (V, E)$, definimos o **subgrafo predecessor** de uma busca
  em profundidade de $G$ como o grafo $G_\pi=(V, E_\pi)$ onde

    - $E_\pi = \{(\attrib{v}{\pi}, v):v \in V \text{ e } \attrib{v}{\pi} \not = \const{nil} \}$

- As arestas em $E_\pi$ são **arestas da floresta**


## Propriedades

### Teorema 22.7 (Teorema do parênteses)

Para dois vértices quaisquer $u$ e $v$, exatamente uma das três condições a
seguir é verdadeira

- Os intervalos $[\attrib{u}{d}, \attrib{u}{f}]$ e $[\attrib{v}{d},
  \attrib{v}{f}]$ são disjuntos e nem $u$ e nem $v$ são descendentes um do
  outro na floresta DFS

- O intervalo $[\attrib{u}{d}, \attrib{u}{f}]$ está contido inteiramente no
  intervalo $[\attrib{v}{d}, \attrib{v}{f}]$ e $u$ é descendente de $v$ em uma
  árvore DFS

- O intervalo $[\attrib{v}{d}, \attrib{v}{f}]$ está contido inteiramente no
  intervalo $[\attrib{u}{d}, \attrib{u}{f}]$ e $v$ é descendente de $u$ em uma
  árvore DFS

\pause

Prova feita em sala. Veja o livro para detalhes.


## Propriedades

![22-5](imagens/Fig-22-5.pdf){width=5cm}


## Classificação das arestas

Podemos definir quadro tipos de arestas em termos da floresta $G_\pi$

- **Arestas de árvore**, são as arestas em $G_\pi$. Uma aresta $(u,
  v)$ é uma aresta de árvore se $v$ foi descoberto primeiro pela exploração da
  aresta $(u, v)$

- **Arestas de retorno** são as arestas $(u, v)$ que conectam um vértice $u$
  a um ancestral $v$ em uma árvore DFS (consideramos laços como arestas de
  retorno)

- **Arestas diretas** são as arestas $(u, v)$ que não são arestas da árvore
  e conectam o vértice $u$ a um descendente $v$ em uma árvore DFS

- **Arestas cruzadas** são todas as outras arestas


## Classificação das arestas

Quando uma aresta $(u, v)$ é explorada, a cor do vértice $v$ nos indica o tipo
de aresta: \pause

- \const{branco} \pause - aresta da árvore,

- \const{cinza} \pause - aresta de retorno, e

- \const{preto} \pause - aresta direta ou cruzada


## Classificação das arestas para grafos não orientados

### Teorema 22.10

Na busca em profundidade de um grafo não orientado $G$, cada aresta de $G$ ou
é uma aresta de árvore ou uma aresta de retorno.

\pause

Prova feita em sala. Veja o livro para detalhes.


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.3.
