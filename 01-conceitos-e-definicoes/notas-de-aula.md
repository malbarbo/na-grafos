---
# vim: set spell spelllang=pt_br:
title: Conceitos e definições
---

## Grafos

Um **grafo orientado** $G$ é um par $(V, E)$, onde

- $V$ é um conjunto finito, chamado de **conjunto de vértices**

- $E$ é um conjunto de pares ordenados de $V$, chamado de **conjunto de arestas** \pause

Em um **grafo não orientado** $G = (V, E)$, $E$ é um conjunto de pares de vértices não ordenados.


## Representação gráfica

Os grafos podem ser representados graficamente

- Os vértices são desenhados como círculos

- As arestas são desenhadas como curvas ligando dois círculos, no caso de grafos orientados, as curvas tem um seta em uma das extremidades


## Exemplos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Na figura B-2-a, qual é o conjunto de vértices e o conjunto de arestas?

\pause
$V = \{1, 2, 3, 4, 5, 6\}$, \newline
$E = \{(1,2), (2,2), (2,4), (2,5), (4,1), (4,5), (5,4), (6,3)\}$

\pause

Na figura B-2-b, qual é o conjunto de vértices e o conjunto de arestas?

\pause
$V = \{1, 2, 3, 4, 5, 6\}$, \newline
$E = \{(1,2), (1,5), (2,5), (3,6)\}$
</div>
</div>


## Exemplos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">

Em grafos orientados são permitidos **laços** (arestas de um vértice para ele mesmo -- _autoloop_ em inglês). Exemplo: aresta $(2, 2)$ da figura B-2-a. \pause

Um grafo orientado sem laços é chamado de **grafo simples**.

</div>
</div>


## Exemplos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Em grafos não orientados os laços não são permitidos. \pause

Para grafos não orientados, utilizamos a notação $(u,v)$ para denotar uma aresta, ao invés da notação de conjunto $\{u, v\}$. Dessa forma, $(u, v)$ e $(v, u)$ são consideradas a mesma aresta.
</div>
</div>


## Incidência

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Para uma aresta $(u, v)$ em um grafo orientado, dizemos que $(u, v)$ é **incidente do** ou **sai do** vértice $u$ e é **incidente no** ou **entra no** vértice $v$. \pause

Quais as arestas que saem do vértice 2 na figura B-2-a? \pause \newline $(2,2),
(2,4)$ e $(2,5)$. \pause

Quais as arestas que entram no vértice 2 na figura B-2-a? \pause \newline
$(1,2)$ e $(2,2)$.
</div>
</div>


## Incidência

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Para uma aresta $(u, v)$ em um grafo não orientado, dizemos que $(u, v)$ é **incidente** nos vértices $u$ e $v$. \pause

Quais são as arestas incidentes no vértice 2 da figura B-2-b? \pause \newline
$(1,2)$ e $(2,5)$.
</div>
</div>


## Adjacência

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Para uma aresta $(u, v)$, dizemos que o vértice $v$ é **adjacente** ao vértice $u$. \pause

Para grafos não orientados, a relação de adjacência é simétrica. \pause

Se $v$ é adjacente a $u$ em um grafo orientado, escrevemos $u \rightarrow v$. \pause

O vértice 1 é adjacente ao vértice 2 na figura B-2-b? \pause Sim. \pause E na figura B-2-a? \pause Não, pois não existe a aresta $(2, 1)$.
</div>
</div>


## Grau

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Em um grafo orientado

- O **grau de saída** de um vértice é o número de arestas que saem dele

- O **grau de entrada** de um vértice é o número de arestas que entram nele

- O **grau** de um vértice é soma do grau de saída e do grau de entrada \pause

- Na figura B-2-a, qual é o grau de entrada, o grau de saída e o grau do vértice 2? \pause \newline
2, 3 e 5.
</div>
</div>


## Grau

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Em um grafo não orientado

- O **grau** de um vértice é o número de arestas incidentes nele \pause

- Na figura B-2-b, qual é o grau do vértice 2? \pause \newline
2
</div>
</div>


## Grau

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Um vértice **isolado** tem grau 0. \pause

- Existe algum vértice isolado nos grafos da figura B-2? \pause
Sim, o vértice 4 da figura B-2-b.
</div>
</div>


## Caminhos e ciclos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Um **caminho** de **comprimento** $k$ de um vértice $u$ até um vértice $u'$ em um grafo $G = (V, E)$ é uma sequência $\langle v_0, v_1, v_2, \dots, v_k \rangle$ de vértices tal que $u = v_0$, $u' = v_k$ e $(v_{i-1}, v_i) \in E$ para $i = 1, 2, \dots, k$.

O comprimento do caminho ($k$) é a quantidade de aresta no caminho. \pause

O caminho **contém** os vértice $v_0, v_1, \dots, v_k$ e as arestas $(v_0, v_1), (v_1, v_2), \dots, (v_{k-1}, v_k)$.
</div>
</div>


## Caminhos e ciclos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Se existe um caminho $p$ de $u$ até $u'$, dizemos que $u'$ é **acessível** a partir de $u$ via $p$, ou $u \stackrel{p}{\leadsto} u'$ se o grafo é orientado. \pause

Sempre existe um caminho de comprimento 0 de $u$ para $u$. \pause

Exemplos da figura B-2-a: $\langle 1, 2, 5, 4 \rangle$, $\langle 2, 5, 4, 5 \rangle$ e $\langle 3 \rangle$.
</div>
</div>


## Caminhos e ciclos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Um caminho é **simples** se todos os vértices no caminho são distintos.

Existe um caminho de tamanho 5 no grafo da figura B-2-a? \pause \newline
Sim. Por exemplo, $\langle 1, 2, 5, 4, 1, 2 \rangle$ \pause

Existe um caminho simples de tamanho 5 no grafo da figura B-2-a? \pause \newline
Não. \pause

Um **subcaminho** do caminho $p = \langle v_0, v_1, \dots, v_k \rangle$ é uma subsequência contígua de seus vértices. \pause Por exemplo, o caminho $\langle 2, 5, 4 \rangle$ é um subcaminho de $\langle 1, 2, 5, 4, 1, 2 \rangle$.

</div>
</div>


## Caminhos e ciclos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Em um grafo orientado

- Um caminho $\langle v_0, v_1, \dots, v_k \rangle$ forma um **ciclo** se $v_0 = v_k$ e o caminho contém pelo menos uma aresta. \pause

- O ciclo é **simples** se além disso $v_1, v_2, \dots, v_k$ são distintos. \pause

Dois caminhos $\langle v_0, v_1, \dots, v_{k-1}, v_0 \rangle$ e $\langle v_0', v_1', \dots, v_{k-1}', v_0' \rangle$ formam o mesmo ciclo se existe um inteiro $j$ tal que $v_i' = v_{(i + j) \mod k}$ para $i = 0, 1, \dots, k - 1$.

- Considerando a figura B-2-a, dê dois caminhos que formam o mesmo ciclo que o caminho $\langle 1, 2, 4, 1 \rangle$. \pause \newline $\langle 2, 4, 1, 2 \rangle$ e $\langle 4, 1, 2, 4 \rangle$.
</div>
</div>


## Caminhos e ciclos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Em um grafo não orientado

- Um caminho $\langle v_0, v_1, \dots, v_k \rangle$ forma um **ciclo** se $k > 0$, $v_0 = v_k$ e todas as arestas do caminho são distintas. (Esta definição é diferente em algumas versões do Cormen. Vamos considerar correta a definição que estamos apresentando aqui) \pause

- O ciclo é **simples** se $v_1, v_2, \dots, v_k$ são distintos. \pause

Um grafo sem ciclos é **acíclico**.
</div>
</div>


## Conectividade

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Um grafo não orientado é **conexo** (conectado) se cada vértice é acessível a partir de todos os outros. \pause

Os **componentes conexos** de um grafo são as classes de equivalência de vértices sob a relação “é acessível a partir de”. \pause

Na figura B-2-b quais são os componentes conexos? \pause \newline $\{1, 2, 5\}, \{3, 6\}$ e $\{4\}$ \pause

Um grafo não orientado é conexo se tem exatamente um componente conexo.
</div>
</div>


## Conectividade

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Um grafo orientado é **fortemente conexo** se para cada par de vértices $(u, v)$, $v$ é acessível a partir de $u$. \pause

Os **componentes fortemente conexos** de um grafo orientado são as classes de equivalência de vértices sob a relação “são mutuamente acessíveis”.
</div>
</div>


## Conectividade

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Quais os componentes fortemente conexos da figura B-2-a? \pause \newline $\{1, 2, 4, 5\}$ \pause , $\{3\}$ e $\{6\}$. \pause

- Todos os pares de vértices em $\{1, 2, 4, 5\}$ são mutuamente acessíveis. \pause
- Os vértices $\{3, 6\}$ não formam um componente fortemente conexo por quê? \pause O vértice 6 não é acessível a partir do 3; \pause

Um grafo orientado é fortemente conexo se ele só tem um componente fortemente conexo.
</div>
</div>


## Isomorfismo

Dois grafos $G=(V, E)$ e $G'=(V', E')$ são **isomorfos** se existe uma bijeção $f: V \rightarrow V'$ tal que $(u, v) \in E$ se e somente se $(f(u), f(v)) \in E'$

Ideia: podemos identificar os vértices de $G$ como vértices de $G'$, mantendo as arestas correspondentes em $G$ e $G'$.


## Isomorfismo

<div class="columns">
<div class="column" width="40%">
\includegraphics[trim=0cm 0cm 43cm 0cm,clip,width=5.5cm]{imagens/Fig-B-3.pdf}
</div>
<div class="column" width="60%">

Os grafos da figura B-3-a são isomorfos entre si? \pause

- $V=\{1, 2, 3, 4, 5, 6\}$ e $V'=\{u, v, w, x, y, z\}$ \pause

- $|V|=6$ e $|V'|=6$ ; $|E|= 9$ e $|E'|=9$ \pause

- Mapeamento de $V$ para $V'$ dado pela função bijetora \newline $f(1)= u$,
  $f(2)=v$, $f(3)=w$, $f(4)=x$, $f(5)=y$, $f(6)=z$ \pause

- Sim, são isomorfos
</div>
</div>


## Isomorfismo

<div class="columns">
<div class="column" width="40%">
\includegraphics[trim=56cm 0cm 0cm 0cm,clip,width=4.5cm]{imagens/Fig-B-3.pdf}
</div>
<div class="column" width="60%">
Os grafos da figura B-3-b, são isomorfos? \pause

- $V=\{1, 2, 3, 4, 5\}$ e $V'=\{u, v, w, x, y\}$ \pause

- $|V|=5$ e $|V'|=5$; $|E|=7$ e $|E'|=7$ \pause

- $G$ tem um vértice de grau 4, mas $G'$ não tem \pause

- Não são isomorfos
</div>
</div>


## Subgrafos

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
$G'=(V', E')$ é um **subgrafo** de $G=(V, E)$ se $V' \subseteq V$ e $E' \subseteq E$. \pause

Dado um conjunto $V'$ de modo que $V' \subseteq V$, o subgrafo de $G$ **induzido** por $V'$ é o grafo $G'=(V', E')$, onde $E'=\{(u, v) \in E: u, v \in V'\}$. \pause

Qual é o subgrafo induzido pelo conjunto de vértices $\{1, 2, 3, 6\}$ na figura B-2-a? \pause \newline $G = (\{1, 2, 3, 6\}, \{(1, 2), (2, 2), (6, 3)\}$.
</div>
</div>


## Versões orientada e não orientada

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Dado um grafo não orientado $G=(V, E)$, a **versão orientada** de $G$ é o grafo orientado $G'=(V, E')$, onde $(u, v) \in E'$ se e somente se $(u, v) \in E$

- Cada aresta não orientada $(u, v)$ em $G$ é substituída na versão orientada pelas duas arestas orientadas $(u, v)$ e $(v, u)$ \pause

- Qual é a versão orientada do grafo da figura B-2-b? \pause \newline
  $V = \{1, 2, 3, 4, 5, 6\}$ \newline
  $E = \{(1, 2), (2, 1), (1, 5), (5, 1), (2, 5), (5, 2), (3, 6), (6, 3)\}$
</div>
</div>


## Versões orientada e não orientada

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Dado um grafo orientado $G=(V, E)$, a **versão não orientada** de $G$ é o grafo não orientado $G'=(V, E')$, onde $(u, v) \in E'$ se e somente se $u \neq v$ e $(u, v) \in E$

- A versão não orientada contém as arestas de $G$ “com suas orientações removidas” e laços eliminados \pause

- Mesmo que o grafo orientado contenha as arestas $(u, v)$ e $(v, u)$, o grafo não orientado conterá $(u, v)$ somente uma vez \pause

- Qual é a versão não orientada do grafo da figura B-2-a? \pause \newline
  $V = \{1, 2, 3, 4, 5, 6\}$ \newline
  $E = \{(1, 2), (1, 4), (2, 4), (2, 5), (3, 6), (4, 5)\}$
</div>
</div>


## Vizinho

<div class="columns">
<div class="column" width="30%">
\includegraphics[trim=0cm 0cm 91cm 0cm,clip,width=3cm]{imagens/Fig-B-2.pdf}
\includegraphics[trim=45.5cm 0cm 45.5cm 0cm,clip,width=3.0cm]{imagens/Fig-B-2.pdf}
</div>
<div class="column" width="70%">
Em um grafo orientado, um vizinho de um vértice $u$ é qualquer vértice que seja adjacente a $u$ na versão não orientada

- $v$ é **vizinho** de $u$ se $(u, v) \in E$ ou $(v, u) \in E$ \pause

- Na figura B-2-a, quais os vizinhos do vértice 2? \pause \newline $1, 4, 5$ \pause

Em um grafo não orientado, $u$ e $v$ são vizinhos se são adjacentes.
</div>
</div>


## Grafo completo

**Grafo completo** é um grafo não orientado no qual todo par de vértices é adjacente. \pause

Um grafo completo com $n$ vértices é chamado de $K_n$. \pause

Desenhe os grafos $K_1, K_2, K_3, K_4, K_5$.


## Grafo bipartido

**Grafo bipartido** é um grafo não orientado $G = (V, E)$ em que $V$ pode ser particionado em dois conjuntos $V_1$ e $V_2$ tais que $(u, v) \in E$ implica que $u \in V_1$ e $v \in V_2$ ou\ $u \in V_2$ e $v \in V_1$. \pause

- Todas as arestas ficam entre os dois conjuntos $V_1$ e $V_2$. \pause

Dê um exemplo de um grafo bipartido.


## Árvores e florestas

Um grafo conexo acíclico não orientado é uma **árvore** \pause

- Dê um exemplo de uma árvore. \pause

Um grafo acíclico não orientado é uma **floresta** \pause

- Dê um exemplo de uma floresta. \pause

Um grafo acíclico orientado é chamado de **GAO** \pause

- Dê um exemplo de um GAO.


## Variantes

Semelhantes a grafos não orientados

- **Multigrafo**: pode ter várias arestas entre vértices e também laços \pause

- **Hipergrafo**: cada **hiperaresta**, em lugar de conectar dois vértices, conecta um subconjunto arbitrário de vértices


## Referências

Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo B.4.
