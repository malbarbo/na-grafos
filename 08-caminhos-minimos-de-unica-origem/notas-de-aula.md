---
# vim: set spell spelllang=pt_br:
# TODO: adicionar as provas!
# TODO: semehante as notas de aula do cormem
# TODO: procurar uma arbodagem mais simples?
# TODO: fazer uma tabela com os tempos de execução do dijkstra
title: Caminhos mínimos de única origem
---


# Introdução


## Introdução

- Como encontrar o caminho mínimo entre duas cidades? \pause

- Vamos estudar este tipo de problema, que é conhecido como **problema de
  caminho mínimo**

- Entrada

    - Um grafo orientado $G = (V, E)$

    - Uma função peso $w : E \rightarrow \mathbb{R}$


## Introdução

- O **peso do caminho** $p = \langle v_0, v_1, \dots, v_k \rangle$ é a soma dos
  pesos das arestas no caminho

    - $\displaystyle w(p) = \sum_{i=1}^k w(v_{i-1}, v_i)$


## Introdução

- O **peso do caminho mínimo** $\delta(u, v)$ deste $u$ até $v$ é

    $$\delta(u, v) = \begin{cases}
        min\{w(p) : u \stackrel{p}{\leadsto} v \} & \text{se existe um caminho de $u$ até $v$} \\
        \infty                                    & \text{caso contrário}
    \end{cases}$$


## Introdução

- Um **caminho mínimo** do vértice $u$ até o vértice $v$ é qualquer caminho $p$
  com peso $w(p) = \delta(u,v)$


## Introdução

- Os pesos das arestas podem representar outras métricas além da distância,
  como o tempo, custo, ou outra quantidade que acumule linearmente ao longo de
  um caminho e que se deseja minimizar

- O algoritmo de busca em largura é um algoritmo de caminhos mínimos que
  funciona para grafos não valorados, isto é, as arestas tem peso unitário


## Tipos de problemas de caminho mínimo

- **Origem única**: Encontrar um caminho mínimo a partir de uma dada origem $s
  \in V$ até todo vértice $v \in V$ \pause

- **Destino único**: Encontrar um caminho mínimo até um determinado vértice de
  destino $t$ a partir de cada vértice $v$ \pause

- **Par único**: Encontrar o caminho mínimo de $u$ até $v$ \pause

- **Todos os pares**: Encontrar um caminho mínimo deste $u$ até $v$ para todo
  par de vértices $u$ e $v$


## Exemplo

- Exemplo de caminhos mínimos de única origem

    ![](imagens/Fig-24-2.pdf)

- Observe que

    - O caminho mínimo pode não ser único

    - Os caminhos mínimos de uma origem para todos os outros vértices formam
      uma árvore


## Caminhos mínimos

- Veremos algumas características dos caminho mínimos


## Subestrutura ótima

Em geral os algoritmos de caminhos mínimos se baseiam na seguinte propriedade

### Lema 24.1

Qualquer subcaminho de um caminho mínimo é um caminho mínimo \pause

### Prova

Ideia da prova: se um subcaminho não for mínimo podemos trocá-lo por um
subcaminho mínimo é obter um caminho menor, o que é uma contradição pois o
caminho é mínimo!


## Arestas com pesos negativos

- Não apresentam problemas se nenhum ciclo com peso negativo é alcançável a
  partir da origem

- Nenhum caminho da origem até um vértice em um ciclo negativo pode ser mínimo

- Se existe um ciclo de peso negativo em algum caminho de $s$ até $v$,
  definimos $\delta(s, v) = -\infty$

    ![](imagens/Fig-24-1.pdf){width=7cm}


## Ciclos

- Caminhos mínimos podem conter ciclos? \pause Não \pause

    - Peso negativo, acabamos de descartar

    - Peso positivo, podemos obter um caminho mínimo eliminando o ciclo

    - Peso nulo, não existe razão para usar tal ciclo

    \pause

- Qualquer caminho acíclico em um grafo $G = (V, E)$ contém no máximo $|V|$
  vértices distintos e no máximo $|V| - 1$ arestas

    - Desta forma, vamos restringir a nossa atenção para ciclos com no máximo
      $|V| - 1$ arestas


## Representação

- Representamos os caminhos mínimos de forma semelhante as árvores produzidas
  pelo \proc{BFS}


## Representação

- Para cada vértice $v \in V$, a saída dos algoritmos consiste em

    - $\attrib{v}{d} = \delta(s, v)$

        - Inicialmente $\attrib{v}{d} = \infty$

        - Diminui conforme o algoritmo progride, mas sempre mantém a
          propriedade $\attrib{v}{d} \ge \delta(s, v)$

        - Vamos chamar $v.d$ de **estimativa do caminho mínimo**

    - $\attrib{v}{\pi} =$ predecessor de $v$ no caminho mínimo a partir de $s$

        - Se não existe predecessor, então $\attrib{v}{\pi} = \const{nil}$

        - $\pi$ induz uma árvore, a árvore de caminhos mínimos



## Relaxamento

\begin{codebox}
    \Procname{$\proc{initialize-single-source}(G, s)$}
    \li \For $v \in \attrib{G}{V}$ \Do
    \li     $v.d = \infty$
    \li     $\attrib{v}{\pi} = \const{nil}$\
        \End
    \li $s.d = 0$
\end{codebox}


## Relaxamento

Sendo os vértices inicializados com \proc{initialize-single-source}, podemos
melhorar a estimativa do caminho mínimo para $v$, indo através de $u$ e
seguindo $(u, v)$?

![](imagens/Fig-24-3.pdf){width=6cm}

\pause

\begin{codebox}
    \Procname{$\proc{relax}(u, v, w)$}
    \li \If $\attrib{v}{d} > \attrib{u}{d} + w(u, v)$ \Then
    \li     $\attrib{v.d} = \attrib{u}{d} + w(u, v)$
    \li     $\attrib{v}{\pi} = u$
        \End
\end{codebox}


## Propriedades

- Desigualdade de triângulos (Lema 24.10)

    - Para toda $(u, v) \in E$, temos que
      $\delta(s, v) \le \delta(s, u) + w(u, v)$ \pause

- Para as próximas propriedades supomos que

    - O grafo é inicializado com uma chamada a \proc{initialize-single-source}

    - O único modo de modificar $v.d$ e $v.\pi$ (para qualquer vértice) e pela
      chamada de \proc{relax}


## Propriedades

- Propriedade do limite superior (Lema 24.11)

    - Sempre temos $v.d \ge \delta(s, v)$ para todo $v$. Uma vez que
      $v.d = \delta(s, v)$, ele nunca muda

    \pause

- Propriedade de nenhum caminho (Corolário 24.12)

    - Se $\delta(s, v) = \infty$, então sempre $v.d = \infty$


## Propriedades

- Propriedade de convergência (Lema 24.14)

    - Se $s \leadsto u \rightarrow v$ é um caminho mínimo,
      $\attrib{u}{d} = \delta(s, u)$ e \proc{relax}$(u, v, w)$ é chamado,
      então, em todos os momentos após a chamada, temos $\attrib{v}{d} =
      \delta(s, v)$

    \pause

- Propriedade de relaxamento de caminho (Lema 24.15)

    - Seja $p = \langle v_0, v_1, \dots, v_k \rangle$ o caminho mínimo de $s =
      v_0$ até $v_k$, se a função \proc{relax} for chamada na ordem $(v_0, v_1),
      (v_1, v_2), \dots, (v_{k-1}, v_k)$, mesmo que intercalada com outros
      relaxamentos, então $\attrib{v_k}{d} = \delta(s, v_k)$

## Propriedades

- Propriedade do subgrafo-predecessor

    - Uma vez que $\attrib{v}{d} = \delta(s, v)$ for todo $v \in V$, o subgrafo
      predecessor é uma árvore de caminhos mínimos enraizada em $s$


## Ideia dos algoritmos

- Os algoritmos que veremos usam a mesma ideia

    - inicializar os atributos $\attrib{v}{d}$ e $\attrib{v}{\pi}$

    - relaxar as arestas

- Eles diferem na ordem e na quantidade de vezes que cada aresta é relaxada



# Algoritmo de Bellman-Ford


## Algoritmo de Bellman-Ford

- Resolve o problema para o caso geral, as arestas podem ter pesos negativos

    - Se ciclos negativos acessíveis a partir da origem forem encontrados
      o algoritmo devolve \const{false}, caso contrário, devolve \const{true}

    - Calcula $\attrib{v}{d}$ e $\attrib{v}{\pi}$ para todo $v \in V$

\pause

- Ideia

    - Relaxar todas as arestas, $|V| - 1$ vezes


## Algoritmo de Bellman-Ford

<div class="columns">
<div class="column" width="50%">
\begin{codebox}
    \Procname{$\proc{bellman-ford}(G, w, s)$}
    \li $\proc{initialize-single-source}(G, s)$
    \li \For $i \gets 1$ \To $|G.V| - 1$ \Do
    \li     \For $(u, v) \in \attrib{G}{E}$ \Do
    \li         $\proc{relax}(u, v, w)$
            \End
        \End
    \li \For $(u, v) \in \attrib{G}{E}$ \Do
    \li     \If $\attrib{v}{d} > \attrib{u}{d} + w(u, v)$ \Then
    \li         \Return \const{false}
            \End
        \End
    \li \Return \const{true}
\end{codebox}
</div>
<div class="column" width="50%">
\pause

Análise do tempo de execução

\pause

- A inicialização na linha 1 demora $\Theta(V)$

- Cada uma das $|V| - 1$ passagens das linha 2 a 4 demora o tempo $\Theta(E)$,
  totalizando $O(V \cdot E)$

- O laço das linha 5 a 7 demora $O(E)$

- Tempo de execução do algoritmo $\Theta(V \cdot E)$
</div>
</div/>


## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=7cm,trim=0pt 1016pt 2484pt 0pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=7cm,trim=1242pt 1016pt 1242pt 0pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=7cm,trim=2484pt 1016pt 0pt 0pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=7cm,trim=0pt 0pt 2484pt 1016pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=7cm,trim=1242pt 0pt 1242pt 1016pt,clip,]{imagens/Fig-24-4.pdf}



## Algoritmo de Bellman-Ford

\small

- Por que este algoritmo funciona? \pause

    - Propriedade de relaxamento de caminho

    - Seja $p = \langle v_0, v_1, \dots, v_k \rangle$ um caminho mínimo
      acíclico entre $s = v_0$ e $v = v_k$. O caminho $p$ tem no máximo $|V| -
      1$ arestas, e portanto $k \le |V| - 1$

    - Cada iteração do laço da linha 2 relaxa todas as arestas

        - A primeira iteração relaxa $(v_0, v_1)$

        - A segunda iteração relaxa $(v_1, v_2)$

        - ...

        - A $k$-ésima iteração relaxa $(v_{k-1}, v_k)$

    - Pela propriedade de relaxamento de caminho
        $v.d = v_k.d = \delta(s, v_k) = \delta(s, v)$

<!-- TODO: e o valor true/false? !-->



# Grafo orientado acíclico


## Algoritmo para gaos

- Em grafo acíclico orientado (gao), os caminhos mínimos são sempre bem
  definidos (não existem ciclos de peso negativo) \pause

- Ideia

    - Relaxar as arestas em uma ordem topológica dos vértices


## Caminhos mínimos de única origem em gaos

<div class="columns">
<div class="column" width="50%">
\begin{codebox}
    \Procname{$\proc{dag-shortest-paths}(G, w, s)$}
    \li ordenar topologicamente $\attrib{G}{V}$
    \li $\proc{initialize-single-source}(G, s)$
    \li \For vértice $u$ em ordem topológica \Do
    \li     \For $v \in \attrib{G}{adj}[u]$ \Do
    \li         $\proc{relax}(u, v, w)$
            \End
        \End
\end{codebox}
</div>
<div class="column" width="50%">
\pause
Análise do tempo de execução
\pause

- A ordenação topológica da linha 1 tem tempo $\Theta(V + E)$

- \proc{initialize-single-source} na linha 2 tem tempo $\Theta(V)$

- Nos laços das linhas 2 e 3 a lista de adjacências de cada vértices é visitada
  apenas uma vez, totalizando $V + E$ (análise agregada), como o relaxamento de
  cada aresta custa $O(1)$, o tempo total é $\Theta(E)$

- Portanto, o tempo de execução do algoritmo é $\Theta(V + E)$
</div>
</div>


## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 2032pt 1920pt 0pt,clip,]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=1920pt 2032pt 0pt 0pt,clip,]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 1355pt 1920pt 677pt,clip,]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=1920pt 1355pt 0pt 677pt,clip,]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 678pt 1920pt 1354pt,clip,]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=1920pt 678pt 0pt 1354pt,clip,]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 1pt 1920pt 2031pt,clip,]{imagens/Fig-24-5.pdf}


## Caminhos mínimos de única origem em gaos

- Por que este algoritmo funciona?

    - Como os vértices são processados em ordem topológica, as arestas de
      qualquer caminho são relaxadas na ordem que aparecem no caminho

    - Pela propriedade de relaxamento de caminho, o algoritmo funciona
      corretamente


## Aplicação

- Caminhos críticos na análise de diagramas PERT (*program evaluation and
  review technique*)

- As arestas representam serviços a serem executados

- Os pesos de arestas representam os tempos necessários para execução de
  determinados serviços

- $(u, v)$, $v$, $(v, x)$: serviço $(u, v)$ deve ser executado antes do serviço
  $(v, x)$


## Aplicação

- Um caminho através desse gao: sequência de serviços

- Caminho crítico: é um caminho mais longo pelo gao

    - Tempo mais longo para execução de uma sequência ordenada

- O peso de um caminho crítico é um limite inferior sobre o tempo total para
  execução de todos os serviços


## Aplicação

- Podemos encontrar um caminho crítico de duas maneiras: \pause

    - Tornando negativos os pesos das arestas e executando
      \proc{dag-shortest-paths}; ou \pause

    - Executando \proc{dag-shortest-paths}, substituindo “$\infty$” por
      “$-\infty$” na linha 2 de \proc{initialize-single-source} e “$>$” por
      “$<$” no procedimento \proc{relax}



# Algoritmo de Dijkstra


## Algoritmo de Dijkstra

- Caminho mínimo de única origem em um grafo orientado ponderado

- Todos os pesos de arestas são não negativos, ou seja $w(u,v) \geq 0$ para
  cada aresta $(u,v) \in E$


## Algoritmo de Dijkstra

- Ideia

    - Essencialmente uma versão ponderada da busca em largura

        - Ao invés de uma fila FIFO, usa uma fila de prioridades

        - As chaves são os valores $v.d$

    - Mantém dois conjuntos de vértices

        - $S$: vértices cujo caminho mínimo desde a origem já foram
          determinados

        - $Q = V - S$: fila de prioridades

    - O algoritmo seleciona repetidamente o vértice $u \in Q$ com a mínima
      estimativa de peso do caminho mínimo, adiciona $u$ a $S$ e relaxa todas
      as arestas que saem de $u$


## Algoritmo de Dijkstra

\begin{codebox}
    \Procname{$\proc{dijkstra}(G, w, s)$}
    \li $\proc{initialize-single-source}(G, s)$
    \li $S = \emptyset$
    \li $Q = \attrib{G}{V}$
    \li \While $Q \not = \emptyset$ \Do
    \li     $u = \proc{extract-min}(Q)$
    \li     $S = S \cup \{ u \}$
    \li     \For $v \in \attrib{G}{adj}[u]$ \Do
    \li         $\proc{relax}(u, v, w)$
            \End
        \End
\end{codebox}


## Algoritmo de Dijkstra

\includegraphics[width=7cm,trim=0pt 903pt 2484pt 0pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=7cm,trim=1242pt 903pt 1242pt 0pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=7cm,trim=2484pt 903pt 0pt 0pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=7cm,trim=0pt 0pt 2484pt 903pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=7cm,trim=1242pt 0pt 1242pt 903pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=7cm,trim=2484pt 0pt 0pt 903pt,clip,]{imagens/Fig-24-6.pdf}


## Algoritmo de Dijkstra

- Análise do tempo de execução

    - Linha 1 $\Theta(V)$

    - Linhas 3 a 8 $O(V + E)$ (sem contar as operações com fila)

    - Operações de fila

        - \proc{insert} implícita na linha 3 (executado uma vez para cada vértice)

        - \proc{extract-min} na linha 5 (executado uma vez para cada vértice)

        - \proc{decrease-key} implícita em \proc{relax} (executado no máximo de
          $|E|$ vezes, uma vez para cada aresta relaxada)

    - Depende da implementação da fila de prioridade


## Algoritmo de Dijkstra

- Análise do tempo de execução

    - Arranjos simples

        - Como os vértices são enumerados de $1$ a $|V|$, armazenamos o valor
          $\attrib{v}{d}$ na $v$-ésima entrada de um arranjo

        - Cada operação \proc{insert} e \proc{decrease-key} demora $O(1)$

        - Cada operação \proc{extract-min} demora $O(V)$ (pesquisa linear)

        - Tempo total de $O(V^2 + E) = O(V^2)$


## Algoritmo de Dijkstra

- Análise do tempo de execução

    - Heap

        - Se o grafo é esparso, em particular, $E = o(V^2 / \lg V)$ é prático
          utilizar um heap binário

        - O tempo para construir um heap é $O(V)$

        - Cada operação de \proc{extract-min} e \proc{decrease-key} demora $O(\lg V)$

        - Tempo total de $O((V + E)\lg V + V)$, que é $O(E\lg V)$ se todos os
          vértices são acessíveis a partir da origem


## Algoritmo de Dijkstra

- Análise do tempo de execução

    - Heap de Fibonacci

        - Cada operação \proc{extract-min} demora $O(\lg V)$

        - Cada operação \proc{decrease-key} demora o tempo amortizado de $O(1)$

        - Tempo total de $O(V\lg V + E)$


## Algoritmo de Dijkstra

- Porque este algoritmo funciona?

    - Invariante de laço: no início de cada iteração do laço while,
    $v.d = \delta(s, v)$ para todos $v \in S$

    - Inicialização: $S = \emptyset$, então é verdadeiro

    - Término: No final,
    $Q = \emptyset \Rightarrow S = V \Rightarrow v.d = \delta(s, v)$, para todo $v \in V$

    - Manutenção: precisamos mostrar que $u.d = \delta(s, u)$ quando $u$ é
      adicionado a $S$ em cada iteração (Comentado em sala, veja o livro para a
      prova completa)

    - Feito em sala


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 24.
