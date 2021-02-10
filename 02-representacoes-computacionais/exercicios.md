---
# vim: set spell spelllang=pt_br:
title: 02 - Representações computacionais
---

1.  Exercício 22.1-2 de CLRS3 ou CLRS2.

2.  Exercício 22.1-3 de CLRS3 ou CLRS2.

3.  Exercício 22.1-4 de CLRS3 ou CLRS2.

4.  Exercício 22.1-5 de CLRS3 ou CLRS2.

5.  Exercício 22.1-6 de CLRS3 ou CLRS2.

6.  Exercício 22.1-7 de CLRS3 ou CLRS2.

7.  Exercício 22.1-8 de CLRS3 ou CLRS2.


# Referências

-   [CLRS2] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{2} edition. Capítulo 22.1.

-   [CLRS3] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.1.

\newpage


# Soluções

**Exercício 3**

Criamos uma lista de adjacência $\attrib{G'}{Adj}$ de tamanho $|V|$. Para cada vértice $u$ de $G$, examinamos $\attrib{G}{Adj}[u]$ e adicionamos os vértices encontrados em $\attrib{G'}{Adj}[u]$. Temos que achar uma maneira de evitar adicionar o vértice $u$ (laço) e vértices repetidos (arestas múltiplas) em $\attrib{G'}{Adj}[u]$. Vamos primeiro analisar uma opção menos eficiente.

Criamos um matriz $A = (a_{ij})$ de tamanho $|V| \times |V|$, e inicializamos cada valor $a_{ij}$ com $\const{true}$ se $i \not = j$, e $\const{false}$ caso contrário ($A_{ij} \isequal \const{true}$ significa que a aresta $(i, j)$ é permitida em $G'$). Quando examinamos uma aresta $(u, v)$, apenas adicionamos $v$ em $\attrib{G'}{Adj}[u]$ se $A_{uv} \isequal \const{true}$. Após a adição, fazemos $A_{uv} \gets \const{false}$, evitando desta forma que $v$ seja adicionado novamente em $\attrib{G'}{Adj}[u]$.

O tempo para analisar todos as arestas de $G$ é $O(V + E)$. Inicializar a lista de adjacência de $G'$ tem tempo $O(V)$. Adicionar um vértice na lista de adjacência de $G'$ é constante (verificar e mudar um elemento de $A$ também), portanto "preencher" as listas de adjacência de $G'$ tem tempo $O(E)$. Poderíamos concluir então, de forma precipitada, que o tempo de execução para criar $G'$ é $O(V + E)$. No entanto, não consideramos o tempo de inicialização de $V$, que é $O(V^2)$! Ou seja, o tempo para criar $G'$ é $O(V^2)$, o que não
atende o que foi pedido no exercício.

Podemos observar que cada linha $i$ da matriz $V$ é utilizada para evitar que laços e arestas múltiplas sejam adicionadas na lista de adjacência do vértice $i$ em $G'$. Mas, uma vez que a lista de adjacência de $i$ é explorada, a linha $i$ da matriz não é mais utilizada. Desta forma, poderíamos ter apenas uma linha na matriz e reutilizar esta linha para todos os vértices. Precisamos apenas der o cuidado de deixar esta linha em um estado consistente antes de explorar a lista de adjacência de cada vértice.

Usamos então um atributo $\id{permitido}$ nos vértices (equivalente a uma linha da matriz $A$), inicializado com $\const{true}$. Antes de selecionar cada vértice $u$, assumimos que $\attrib{v}{permitido} \isequal \const{true}$ para todo $v \in \attrib{G}{V} - \{ u \}$, e $\attrib{u}{permitido} \isequal \const{false}$, indicando que as arestas $(u, v)$ são permitidas em $G'$ e $(u, u)$ não é. Quando examinamos uma aresta $(u, v)$, apenas adicionamos $v$ em $\attrib{G'}{Adj}[u]$ se $\attrib{v}{permitido} \isequal \const{true}$. Após a adição, fazemos $\attrib{v}{permitido} \gets \const{false}$, evitando desta forma que $v$ seja adicionado novamente em $\attrib{G'}{Adj}[u]$. O código a seguir mostra este processo


\begin{codebox}
  \Procname{$\proc{multigrafo-para-grafo(G)}$}
  \li Seja $\attrib{G'}{Adj}$ uma nova lista de adjacências de tamanho $|V|$
  \li \For each vertex $v \in \attrib{G}{V}$ \Do
  \li   $\attrib{v}{permitido} \gets \const{true}$
      \End
  \li \For each vertex $u \in \attrib{G}{V}$ \Do
  \li   $\attrib{u}{permitido} \gets \const{false}$
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li     \If $\attrib{v}{permitido} \isequal \const{true}$ \Then
  \li       Adiciona $v$ em $\attrib{G'}{adj[u]}$
  \li       $\attrib{v}{permitido} \gets \const{false}$
          \End
        \End
  \zi   \Comment Precisamos restaurar o atributo $\id{permitido}$ para a próxima iteração.
  \zi   \Comment Ao invés de mudar o valor do atributo para todos os vértices (o que faria o tempo ser $O(V^2)$),
  \zi   \Comment apenas mudamos para aqueles que o atributo foi alterado nas linha anteriores.
  \li   $\attrib{u}{permitido} \gets \const{true}$
  \li   \For each vertex $v \in \attrib{G}{Adj}[u]$ \Do
  \li       $\attrib{v}{permitido} \gets \const{true}$
        \End
      \End
  \li \Return $G'$
\end{codebox}

A linha 1 e o laço das linhas 2 e 3 têm tempo $O(V)$ e o laço das linhas 4 a 12 tem tempo $O(V + E)$, portanto, o tempo de execução de \proc{multigrafo-para-grafo} é $O(V + E)$, conforme o solicitado no exercício.

<!--

**Exercício 5**

Considerando a definição de sumidouro universal, podemos fazer a seguintes
observações

- Existe no máximo 1 sumidouro universal em um grafo

- Se o vértice $u$ é sumidouro universal de um grafo representado pela matriz
  de adjacências $A$ então

    - todos os valores na linha $u$ de $A$ são 0; e

    - todos os valores da coluna $u$, exceto $A_{uu}$ são 1;

Baseado nestas observações podemos

-->
