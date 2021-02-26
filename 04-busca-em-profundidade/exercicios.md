---
# vim: set spell spelllang=pt_br:
title: 04 - Busca em profundiade
---

1. Exercício 22.3-1 do CLRS3 ou CLRS2. (Observe que você deve considerar se pode ou não existir arestas (e o tipo) durante **qualquer** momento da execução do algoritmo)

2. Exercício 22.3-2 do CLRS3 ou CLRS2.

3. Exercício 22.3-3 do CLRS3 ou CLRS2.

4. Exercício 22.3-4 do CLRS3. (De acordo com a errata, considere a remoção da  linha 8 e não da linha 3)

5. Exercício 22.3-7 do CLRS3 ou 22.3-6 CLRS2.

6. Exercício 22.3-8 do CLRS3 ou 22.3-7 CLRS2.

7. Exercício 22.3-9 do CLRS3 ou 22.3-8 CLRS2.

8. Exercício 22.3-10 do CLRS3 ou 22.3-9 CLRS2.

9. Exercício 22.3-11 do CLRS3 ou 22.3-10 CLRS2.

10. Exercício 22.3-12 do CLRS3 ou 22.3-11 CLRS2.

11. Exercício 22.3-13 do CLRS3.


# Referências

-   [CLRS2] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{2} edition. Capítulo 22.3.

-   [CLRS3] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.3.

\newpage


# Soluções

**Exercício 8**

Apenas o procedimento \proc{DFS-Visit} precisa ser alterado. O código a seguir mostra as modificações para grafos orientados.

\begin{codebox}
  \Procname{$\proc{DFS-Visit}(G, u)$}
  \li $\id{tempo} \gets \id{tempo} + 1$
  \li $\attrib{u}{d} \gets \id{tempo}$
  \li $\attrib{u}{cor} \gets \const{cinza}$
  \li \For $v \in \attrib{G}{Adj}[u]$ \Do
  \li   \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li     \proc{print} $(u, v)$ ``= aresta de árvore''
  \li     $\attrib{v}{\pi} \gets u$
  \li     $\proc{DFS-Visit}(G, v)$
  \li   \ElseIf $\attrib{v}{cor} \isequal \const{cinza}$ \Then
  \li     \proc{print} $(u, v)$ ``= aresta de retorno''
  \li   \Else
  \li     \If $\attrib{u}{d} < \attrib{v}{d}$ \Then
  \li       \proc{print} $(u, v)$ ``= aresta para frente''
  \li     \Else
  \li       \proc{print} $(u, v)$ ``= aresta cruzada''
          \End
        \End
      \End
  \li $\attrib{u}{cor} \gets \const{preto}$
  \li $\id{tempo} \gets \id{tempo} + 1$
  \li $\attrib{u}{f} \gets \id{tempo}$
\end{codebox}

Para grafos não orientados temos que evitar classificar uma aresta mais de uma vez, especificamente, as arestas que conectam um vértice ao seu pai são arestas da árvore, então temos que evitar classificá-las como de retorno. O código a seguir mostra as modificação do \proc{DFS-Visit} para grafos não orientados.

\begin{codebox}
  \Procname{$\proc{DFS-Visit}(G, u)$}
  \li $\id{tempo} \gets \id{tempo} + 1$
  \li $\attrib{u}{d} \gets \id{tempo}$
  \li $\attrib{u}{cor} \gets \const{cinza}$
  \li \For $v \in \attrib{G}{Adj}[u]$ \Do
  \li   \If $\attrib{v}{cor} \isequal \const{branco}$ \Then
  \li     \proc{print} $(u, v)$ ``= aresta de árvore''
  \li     $\attrib{v}{\pi} \gets u$
  \li     $\proc{DFS-Visit}(G, v)$
  \li   \ElseIf $\attrib{u}{\pi} \not = v$ e $\attrib{v}{cor} \isequal \const{cinza}$ \Then
  \li     \proc{print} $(u, v)$ ``= aresta de retorno''
        \End
      \End
  \li $\attrib{u}{cor} \gets \const{preto}$
  \li $\id{tempo} \gets \id{tempo} + 1$
  \li $\attrib{u}{f} \gets \id{tempo}$
\end{codebox}

\newpage

**Exercício 10**

Utilizamos uma variável $\id{cc}$ no procedimento \proc{DFS} que armazena o número de componentes. Quando um vértice $u$ com cor \const{branco} é identificado incrementamos \id{cc}, para indicar mais um componente conexo, e fazemos $\attrib{u}{cc} \gets \id{cc}$. Em \proc{DFS-Visit} todos os vértices recebem o mesmo número do componente do seu pai (linha 6). Desta forma, todos vértices de um mesmo componente têm o mesmo valor do atributo \id{cc}.

\begin{codebox}
  \Procname{$\proc{DFS}(G)$}
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   $\attrib{u}{cor} \gets \const{branco}$
  \li   $\attrib{u}{\pi} \gets \const{nil}$
      \End
  \li $\id{tempo} \gets 0$
  \li $\id{cc} \gets 0$
  \li \For $u \in \attrib{G}{V}$ \Do
  \li   \If $\attrib{u}{cor} \isequal \const{branco}$ \Then
  \li     $\id{cc} \gets \id{cc} + 1$
  \li     $\attrib{u}{cc} \gets \id{cc}$
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
  \li     $\attrib{v}{cc} \gets \attrib{u}{cc}$
  \li     $\attrib{v}{\pi} \gets u$
  \li     $\proc{DFS-Visit}(G, v)$
        \End
      \End
  \li $\attrib{u}{cor} \gets \const{preto}$
  \li $\id{tempo} \gets \id{tempo} + 1$
  \li $\attrib{u}{f} \gets \id{tempo}$
\end{codebox}
