---
# vim: set spell spelllang=pt_br:
title: Busca em profundidade
---

## Introdução

Procurar "mais fundo" no grafo sempre que possível (_Depth-first search_ - DFS em inglês) \pause

- As arestas são exploradas a partir do vértice $v$ mais recentemente descoberto que ainda tem arestas inexploradas saindo dele \pause

- Quando todas as arestas de $v$ são exploradas, a busca regressa para explorar as arestas que deixam o vértice a partir do qual $v$ foi descoberto \pause

- Este processo continua até que todos os vértices acessíveis a partir da origem tenham sidos descobertos \pause

- Se restarem vértices não descobertos, a busca se repetirá para estes vértices


## Introdução

Durante a execução do algoritmo, diversos atributos são definidos para os vértices

- Cor ($\id{cor}$): cada vértice inicialmente é branco. Quando um vértice é descoberto ele é colorido de cinza. Quando a lista de adjacências de um vértice é totalmente explorada, o vértice é colorido de preto.

- Pai ($\pi$): quando um vértice $v$ é descoberto a partir de um vértice $u$, o campo  predecessor $\attrib{v}{\pi} = u$ é definido

- Carimbo de tempo (\id{d} e \id{f}): cada vértice tem dois carimbos de tempo $\attrib{v}{d}$ (quando o vértice é descoberto) e $\attrib{v}{f}$ (quando o vértice é terminado)


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
\vspace{-1mm}

\begin{codebox}
  \Procname{$\proc{DFS}(G)$}
  \li \For each vertex $u \in \attrib{G}{V}$ \Do
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
  \li \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
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

**Tempo de execução** \pause

- Os laços nas linhas 1 a 3 e nas linhas 5 a 7 de \proc{DFS} demoram tempo $\Theta(V)$, sem contar o tempo das chamadas a \proc{DFS-Visit}

- O procedimento \proc{DFS-Visit} é chamado exatamente uma vez para cada vértice, isto porque \proc{DFS-Visit} é chamado para os vértices brancos, e no início de \proc{DFS-Visit} o vértice é pintado de cinza

- Durante a execução de $\proc{DFS-Visit}(v)$, o laço nas linhas 4 a 7 é executado $\attrib{G}{Adj}[v]$ vezes, como $\sum_{v \in V}  |\attrib{G}{Adj}[v]| = \Theta(E)$, o custo total da execução das linhas 4 a 7 de \proc{DFS-Visit} é $\Theta(E)$

- Portanto, o tempo de execução do \proc{DFS} é $\Theta(V + E)$

</div>
</div>


## Propriedades

A busca em profundidade produz informações interessantes sobre a estrutura do grafo. \pause

Estas informações podem ser usadas diretamente ou na construção de outros algoritmos. \pause

Vamos ver algumas dessas informações.


## Floresta da busca em profundidade

O procedimento \proc{DFS} constrói uma floresta da busca em profundidade (floresta DFS), contendo diversas árvores da busca em profundidade. \pause

Para um grafo $G = (V, E)$, definimos o **subgrafo predecessor** de uma busca em profundidade de $G$ como o grafo $G_\pi=(V, E_\pi)$ onde $E_\pi = \{(\attrib{v}{\pi}, v):v \in V \text{ e } \attrib{v}{\pi} \not = \const{nil} \}$. \pause

As arestas em $E_\pi$ são **arestas da floresta**.


## Estrutura de parênteses

O tempo de descoberta e término dos vértices têm estrutura de parênteses. \pause

Quando representamos a descoberta de um vértice $v$ por "$(v$" e o término por "$v)$", então a sequência de descobertas e términos gera uma expressão bem formada (os parênteses estão certos).


## Estrutura de parênteses

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1000pt 0pt 0pt,clip,width=6.0cm]{imagens/Fig-22-5.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=0pt 0pt 0pt 2000pt,clip,width=6.0cm]{imagens/Fig-22-5.pdf}
</div>
</div>


## Estrutura de parênteses

<div class="columns">
<div class="column" width="40%">
\small

### Teorema 22.7 (Teorema do parênteses)

Para dois vértices quaisquer $u$ e $v$, exatamente uma das três condições a seguir é verdadeira \pause \vspace{-1em}

- Os intervalos $[\attrib{u}{d}, \attrib{u}{f}]$ e $[\attrib{v}{d}, \attrib{v}{f}]$ são disjuntos e nem $u$ e nem $v$ são descendentes um do outro \pause
- O intervalo $[\attrib{u}{d}, \attrib{u}{f}]$ está contido inteiramente no intervalo $[\attrib{v}{d}, \attrib{v}{f}]$ e $u$ é descendente de $v$ em uma árvore DFS \pause
- O intervalo $[\attrib{v}{d}, \attrib{v}{f}]$ está contido inteiramente no intervalo $[\attrib{u}{d}, \attrib{u}{f}]$ e $v$ é descendente de $u$ em uma árvore DFS \pause
</div>

<div class="column" width="57%">
\small

### Prova

Primeiro observamos que $\attrib{u}{d} < \attrib{u}{f}$ para todo vértice $u$ (22.2). \pause

É verdade que $\attrib{u}{d} < \attrib{v}{d}$? \pause Se sim\pause, é verdade que $\attrib{v}{d} < \attrib{u}{f}$? \pause \vspace{-1em}

- Se sim, \pause qual era a cor de $u$ quando $v$ foi descoberto? \pause \proc{cinza}. \pause $v$ é descente de $u$? \pause Sim. \pause Então todas as arestas que saem de $v$ são exploradas e $v$ é finalizado antes que a busca retorne para finaliza $u$. \pause Logo $\attrib{v}{f} < \attrib{u}{f}$ e o intervalo $[\attrib{v}{d}, \attrib{v}{f}]$ está inteiramente contido no intervalo $[\attrib{u}{d}, \attrib{u}{f}]$. \pause
- Se não, $\attrib{u}{f} < \attrib{v}{d}$ e pela equação 22.2 $\attrib{u}{d} < \attrib{u}{f} < \attrib{v}{d} < \attrib{v}{f}$. \pause Portanto os intervalos $[\attrib{u}{d}, \attrib{u}{f}]$ e $[\attrib{v}{d}, \attrib{v}{f}]$ são disjuntos. \pause

Se não ($\attrib{v}{d} < \attrib{u}{d}$), \pause temos a mesma situação anterior, mas o $u$ faz o papel de $v$ e $v$ faz o papel do $u$.

</div>
</div>


## Aninhamento dos intervalos de descendentes

### Corolário 22.8 (Aninhamento dos intervalos de descendentes)

Um vértice $v$ é um descendente próprio de $u$ na floresta DFS de um grafo $G$ se e somente se $\attrib{u}{d} < \attrib{v}{d} < \attrib{v}{f} < \attrib{u}{f}$.

\pause

### Prova

Direta do Teorema 22.7.



## Caminho de vértices brancos

### Teorema 22.9 (Teorema do caminho de vértices brancos)

Na floresta DFS de um grafo $G = (V, E)$, um vértice $v$ é descende de um vértice $u$ se e somente se no momento $\attrib{u}{d}$, que a busca descobre $u$, existe um caminho de $u$ para $v$ que consiste apenas de vértices brancos.

\pause

### Prova

Exercício: leia e compreenda a prova no livro.


## Classificação das arestas

Podemos definir quadro tipos de arestas em termos da floresta $G_\pi$

- **Arestas de árvore**, são as arestas em $G_\pi$. Uma aresta $(u, v)$ é uma aresta de árvore se $v$ foi descoberto primeiro pela exploração da aresta $(u, v)$

- **Arestas de retorno** são as arestas $(u, v)$ que conectam um vértice $u$ a um ancestral $v$ em uma árvore DFS (consideramos laços como arestas de retorno)

- **Arestas diretas** são as arestas $(u, v)$ que não são arestas da árvore e conectam o vértice $u$ a um descendente $v$ em uma árvore DFS

- **Arestas cruzadas** são todas as outras arestas


## Classificação das arestas

Quando uma aresta $(u, v)$ é explorada, a cor do vértice $v$ nos indica o tipo de aresta: \pause

- \const{branco} \pause - aresta da árvore, \pause

- \const{cinza} \pause - aresta de retorno, e \pause

- \const{preto} \pause - aresta direta ou cruzada \pause (como diferenciar as duas?)


## Classificação das arestas para grafos não orientados

### Teorema 22.10

Na busca em profundidade de um grafo não orientado $G$, cada aresta de $G$ ou é uma aresta de árvore ou uma aresta de retorno. \pause

Exercício

- Faça exemplos de grafos não orientados;
- Execute o DFS e classifique as arestas;
- Leia e compreenda a prova no livro.


## Exercícios

22.3-3 Mostre a estrutura de parênteses da busca em profundidade da Figura 22.4.

\includegraphics[trim=2709pt 2pt 0pt 1896pt,clip,height=4.0cm]{imagens/Fig-22-4.pdf}


## Exercícios

22.3-9 Dê um contraexemplo para a seguinte conjectura: se um grafo direcionado $G$ contém um caminho de $u$ para $v$, então qualquer busca em profundidade resulta em $\attrib{v}{d} \le \attrib{u}{f}$.


## Exercícios

22.3-11 Explique como um vértice $u$ de um grafo direcionado pode acabar em uma árvore do DFS contendo apenas $u$, mesmo $u$ tendo arestas de entrada e saída.


## Exercícios

22.3-13 Um grafo direcionado $G$ é **singularmente conexo** se $u \leadsto v$ implica que $G$ contém no máximo um caminho simples de $u$ para $v$ para todos os vértices $u, v \in V$. Projete um algoritmo eficiente para determinar se um grafo é singularmente conectado ou não.

\pause

Como resolver este problema? \pause

O primeiro passo é termos certeza que entendemos o problema. \pause

E Depois? \pause Fazer exemplos de grafos que são e não são singularmente conexos. Note que os exemplos também ajudam na compreensão do problema. \pause

E depois? \pause Como estamos no capítulo do DFS, podemos executar o DFS em cada exemplo e tentar identificar características nos resultados do DFS que possam ser usados para classificar o grafo e então criar uma hipótese (algoritmo).

## Exercícios

E depois? \pause Antes de tentar provar que a hipótese é verdadeira, tentamos encontrar contra exemplos que mostre que ela não é verdadeira. \pause Se encontrarmos contraexemplos, ajustamos a hipótese (algoritmo) e repetimos o processo. \pause

Apos isso temos uma hipótese que não conseguimos mostrar que é falsa encontrado contraexemplos. \pause Então a nossa solução está correta e resolvemos o problema? \pause Não! \pause Agora precisamos provar (argumentar) que o nosso algoritmo está correto. Como fizemos diversos exemplos e possíveis contraexemplos, ganhamos intuição do porque o algoritmo funciona e estamos mais preparados para fazer uma argumentação formal.


## Exercícios

Veja a lista completa de exercícios e algumas soluções na página da disciplina.


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.3.
