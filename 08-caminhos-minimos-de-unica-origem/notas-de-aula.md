---
# vim: set spell spelllang=pt_br:
# TODO: adicionar as provas!
# TODO: semehante as notas de aula do cormem
# TODO: procurar uma arbodagem mais simples?
# TODO: fazer uma tabela com os tempos de execução do dijkstra
title: Caminhos mínimos de única origem
---


## Problema

Como determinar a "rota" mais curta entre duas cidades do Brasil? \pause

Que informações nós temos? \pause A cidade de origem, a cidade de destino e um mapa das estradas do Brasil com a distância entre cada par de interseções adjacentes. \pause O mapa e as distâncias podem ser representadas por um grafo: \pause

- Cada interseção é representada por um vértice; \pause
- A distância entre cada par de interseções adjacentes é representada por uma aresta com peso. \pause

Se a nossa entrada é um grafo e dois vértices, qual é a saída? \pause

- Um caminho que inicia no vértice de origem e termina no vértice de destino e tem o peso (soma dos pesos das arestas) mínimo.


## Problema

\includegraphics[width=4.5cm]{imagens/fig-24-2.pdf}

Se a cidade de origem é representada por $s$ e a de destino por $x$ \pause

- O caminho $\langle s, y, t \rangle$ representa um "rota" entre as cidades de origem e destino? \pause Não. \pause
- O caminho $\langle s, y, t, x \rangle$ representa um "rota" entre as cidades de origem e destino? \pause Sim. \pause Qual o peso desse caminho? \pause 12. \pause Esta é a "rota" mais curta? \pause Não. \pause Os caminhos $\langle s, y, x \rangle$ e $\langle s, t, x \rangle$ também representam rotas entre as cidades de origem e destino e tem peso 9.


## Definições

Neste módulo vamos estudar alguns **problemas de caminho mínimo**. \pause Antes de continuarmos precisamos definir com precisão alguns termos.


## Definições

Seja $G = (V, E)$ um grafo orientado e $w : E \rightarrow \mathbb{R}$ uma função peso: \pause

- O **peso do caminho** $p = \langle v_0, v_1, \dots, v_k \rangle$ é a soma dos pesos das arestas em $p$ $$\displaystyle w(p) = \sum_{i=1}^k w(v_{i-1}, v_i)$$ \pause
- O **peso do caminho mínimo** $\delta(u, v)$ de $u$ até $v$ é

  $$\delta(u, v) = \begin{cases}
        min\{w(p) : u \stackrel{p}{\leadsto} v \} & \text{se existe um caminho de $u$ até $v$} \\
        \infty                                    & \text{caso contrário}
  \end{cases}$$ \pause
- Um **caminho mínimo** de $u$ até $v$ é qualquer caminho $p$ tal que $w(p) = \delta(u,v)$.


## Peso ou distância?

Porque usamos o termo "peso" e não "distância? \pause

Porque os pesos das arestas podem representar outras métricas além da distância, como o tempo, custo, ou outra quantidade que acumule linearmente ao longo de um caminho e que desejamos minimizar.


## Tipos de problemas de caminho mínimo

**Único par**: Encontrar o caminho mínimo de $u$ até $v$. \pause

**Única origem**: Encontrar um caminho mínimo a partir de uma dada origem $s \in V$ até todo vértice $v \in V$. \pause O algoritmo de busca em largura é um algoritmo de caminhos mínimos de única origem que funciona para grafos não valorados, isto é, as arestas tem peso unitário. \pause

**Único destino**: Encontrar um caminho mínimo até um determinado vértice de destino $t$ a partir de cada vértice $v$. \pause

**Todos os pares**: Encontrar um caminho mínimo deste $u$ até $v$ para todo par de vértices $u$ e $v$.


## Exemplo

Vamos focar no **problema do caminho mínimo de única origem**. \pause Aqui está um exemplo de caminhos mínimos de única origem

![](imagens/Fig-24-2.pdf)

\pause

Antes de pensarmos em como resolver este problema, o que podemos observar sobre caminhos mínimos? \pause

- Um caminho mínimo é formado por outros caminhos mínimos (subestrutura ótima); \pause
- Os caminhos mínimos de única origem formam uma árvore.


## Subestrutura ótima

### Lema 24.1

Qualquer subcaminho de um caminho mínimo é um caminho mínimo. \pause

### Prova

Ideia da prova: se um subcaminho não for mínimo podemos trocá-lo por um subcaminho mínimo é obter um caminho de menor peso, o que é uma contradição pois o caminho é mínimo!


## Representação da árvore

Da mesma forma que no \proc{BFS}, \proc{DFS} e \proc{Prim}: \pause

- $\attrib{v}{\pi} =$ predecessor de $v$ no caminho mínimo a partir de $s$

- Se não existe predecessor, então $\attrib{v}{\pi} = \const{nil}$


## Pensando em um algoritmo

Qual é o tipo do problema? \pause Otimização. \pause

Que estratégias podemos tentar utilizar? \pause

- Algoritmo guloso
- Programação dinâmica
- Melhoramento iterativo
- Etc

\pause

Vamos tentar utilizar estas técnicas para derivar hipóteses de algoritmos.


## Pensando em um algoritmo

\includegraphics{imagens/Fig-24-2.pdf}

Como produzir árvores de caminhos mínimos a partir da entrada? \pause

Veja os vídeos das aulas para entender como derivamos a hipóteses a seguir.


## Pensando em um algoritmo

Hipóteses \pause

- Algoritmo guloso: Começar com o vértice de origem na árvore e ir "ligando" novos vértices à árvore usando os caminhos mínimos (não pode haver arestas de peso negativo). \pause

- Programação dinâmica: Expressar os pesos dos caminhos mínimos que usam no máximo $k$ arestas, em termos dos pesos dos caminhos mínimos que usam no máximo $k - 1$ arestas. \pause

- Melhoramento iterativo: Iniciar com uma árvore de caminhos qualquer e tentar melhorar os caminhos trocando uma aresta da árvore por uma que não está na árvore.


## Algoritmo de Dijkstra

A ideia deste algoritmo guloso para caminhos mínimos de única origem foi inicialmente proposta por Dijkstra. \pause

A ideia do algoritmo de Dijkstra é semelhante a de outro algoritmo guloso: o algoritmo de Prim. \pause Vamos comparar as duas ideias.


## Dijkstra vs Prim

**Dijkstra (Caminhos mínimos de única origem)**: Começar com o vértice de origem na árvore e ir "ligando" novos vértices à árvore usando os caminhos de menor peso.

**Prim (Árvores geradoras mínimas)**: Começar com um vértice na árvore e ir "ligando" novos vértices à árvore usando as arestas de menor peso.

\pause

Quais são as semelhanças? \pause

- Começam com um vértice na árvore; \pause
- Escolhem o próximo vértice para ligar na árvore usando um critério guloso.

\pause

Qual é a diferença? \pause O critério guloso:

- Prim: escolhemos ligar o novo vértice usando **uma aresta** de menor peso.
- Dijkstra: escolhemos ligar um novo vértice usando **um caminho** de menor peso.


## Algoritmo de Dijkstra

Como podemos implementar de forma eficiente o algoritmo de Dijkstra? \pause

Considerando a semelhança entre o algoritmos de Dijkstra e o algoritmo de Prim, vamos lembrar: Qual era o "desafio" para implementar o algoritmo Prim de forma eficiente? \pause

- Escolher de forma eficiente o próximo vértice para ser ligado a árvore. \pause

Como resolvemos esse problema? \pause Usando uma fila de prioridades. \pause

Vamos revisar como isso funcionava no algoritmo de Prim.



## Revisão do algoritmo de Prim

Os elementos em uma fila de prioridade são removidos por ordem de prioridade (a \id{chave} no algoritmo de Prim). \pause

Para cada vértice $v$ fora da árvore, qual é o significado do valor $\attrib{v}{chave}$ no algoritmo de Prim? \pause O menor peso entre todas as arestas que podem ser usadas para ligar $v$ a um vértice qualquer da árvore.


## Revisão do algoritmo de Prim

Todos os vértices são inicialmente adicionados na fila. O vértice raiz $r$ começa com $\attrib{r}{chave} = 0$ e os outros vértices com $\id{chave} = \infty$. \pause

Cada vez que um vértice $u$ é removido da fila para ser ligado a árvore, o que é necessário fazer? \pause Verificar é possível ligar algum vértice $v$ adjacente de $u$ de forma "mais eficiente" a árvore, isto é, se podemos mudar o valor de $\attrib{v}{chave}$ para $w(u, v)$: \pause

\begin{codebox}
  \zi \If $\attrib{v}{chave} > w(u, v)$ \Then
  \zi       $\attrib{v}{chave} = w(u, v)$
  \zi       $\attrib{v}{\pi} = u$
  \zi \End
\end{codebox}


## Algoritmo de Dijkstra

Vamos usar a mesma ideia no algoritmo de Dijkstra. \pause

Para cada vértice $v$ do grafo mantemos o atributo $\attrib{v}{d}$, a **estimativa de caminho mínimo**, que é usada como prioridade. \pause

Todos os vértices são inicialmente adicionados na fila. O vértice de origem $s$ começa com $\attrib{s}{d} = 0$ e os vértices começam com $d = \infty$. \pause

Assim como as chaves no algoritmo de Prim são alteradas conforme o algoritmo progride, os valores das estimativas de caminhos mínimo também são alteradas. \pause

Nos exemplos a seguir as arestas destacadas que levam a vértices brancos mostram a estimativa de caminho mínimo atual.


## Algoritmo de Dijkstra

\includegraphics[width=6cm,trim=0pt 903pt 2484pt 0pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=6cm,trim=1242pt 903pt 1242pt 0pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=6cm,trim=2484pt 903pt 0pt 0pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=6cm,trim=0pt 0pt 2484pt 903pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=6cm,trim=1242pt 0pt 1242pt 903pt,clip,]{imagens/Fig-24-6.pdf}

## Algoritmo de Dijkstra

\includegraphics[width=6cm,trim=2484pt 0pt 0pt 903pt,clip,]{imagens/Fig-24-6.pdf}


## Atualização da estimativa de peso do caminho mínimo

![](imagens/Fig-24-3.pdf){width=6cm}

Como a estimativa de caminho mínimo deve ser atualizada algoritmo de Dijkstra? \pause

\begin{codebox}
    \Procname{$\proc{relax}(u, v, w)$}
    \li \If $\attrib{v}{d} > \attrib{u}{d} + w(u, v)$ \Then
    \li     $\attrib{v}{d} = \attrib{u}{d} + w(u, v)$
    \li     $\attrib{v}{\pi} = u$
        \End
\end{codebox}

Este esquema de atualização também é utilizada em outros algoritmos, por isso definimos um procedimento.


## \proc{Initialize-Single-Source}

Para manter a propriedade de que o atributo $d$ representa uma estimativa de caminho mínimo, ele deve ser inicializado de forma apropriada e só pode ser alterado utilizando o procedimento \proc{Relax}. \pause

Usamos a seguinte função de inicialização em diversos algoritmos:

\begin{codebox}
    \Procname{$\proc{Initialize-Single-Source}(G, s)$}
    \li \For $v \in \attrib{G}{V}$ \Do
    \li     $\attrib{v}{d} = \infty$
    \li     $\attrib{v}{\pi} = \const{nil}$\
        \End
    \li $\attrib{s}{d} = 0$
\end{codebox}


## Algoritmo de Dijkstra

Agora que sabemos que o algoritmo de Dijkstra pode ser implementado da mesma forma que o algoritmo de Prim, mudando apenas a forma que as prioridades são computadas, podemos escrever o pseudo código do algoritmo. \pause

Para nos ajudar na análise de corretude do algoritmo, nós vamos utilizar um conjunto $S$, que conterá os vértices cujo caminho mínimo desde a origem já foram determinados.


## Algoritmo de Dijkstra

<div class="columns">
<div class="column" width="40%">
\begin{codebox}
    \Procname{$\proc{Dijkstra}(G, w, s)$}
    \li $\proc{Initialize-Single-Source}(G, s)$
    \li $S = \emptyset$
    \li $Q = \attrib{G}{V}$
    \li \While $Q \not = \emptyset$ \Do
    \li     $u = \proc{Extract-Min}(Q)$
    \li     $S = S \cup \{ u \}$
    \li     \For $v \in \attrib{G}{adj}[u]$ \Do
    \li         $\proc{Relax}(u, v, w)$
            \End
        \End
\end{codebox}
</div>
<div class="column" width="60%">
\pause
**Análise do tempo de execução** \pause

É a mesma que a do algoritmo de Prim! \pause

- O tempo de execução abstrato é escrito em termos dos tempos das operações de fila: $O(V) \times O(\proc{Insert}) + O(V) \times O(\proc{Extract-Min)} + O(E) \times O(\proc{Decrease-Key})$. \pause

- Para determinar o tempo de execução concreto, precisamos considerar como a fila de prioridade é implementada.

</div>
</div>


## Algoritmo de Dijkstra

Operação           | Arranjo  | Heap           | Heap de Fibonacci
-------------------|----------|----------------|------------------
\proc{create}      | $O(V)$   |   $O(V)$       | $O(V)$
\proc{extract-min} | $O(V)$   | $O(\lg V)$     | $O(\lg V)$ (amortizado)
\proc{decrease-key}| $O(1)$   | $O(\lg V)$     | $O(1)$ (amortizado)

\pause

Tempo do procedimento \proc{Dijkstra}

Tempo              | Arranjo         | Heap                  | Heap de Fibonacci
-------------------|-----------------|-----------------------|------------------
Grafo qualquer     | \pause $O(V^2)$ | \pause $O(E \lg V)$   | \pause $O(E + V \lg V)$ \pause
Grafo denso        | \pause $O(V^2)$ | \pause $O(V^2 \lg V)$ | \pause $O(V^2)$


## Algoritmo de Dijkstra

<div class="columns">
<div class="column" width="40%">
\begin{codebox}
    \Procname{$\proc{Dijkstra}(G, w, s)$}
    \li $\proc{Initialize-Single-Source}(G, s)$
    \li $S = \emptyset$
    \li $Q = \attrib{G}{V}$
    \li \While $Q \not = \emptyset$ \Do
    \li     $u = \proc{Extract-Min}(Q)$
    \li     $S = S \cup \{ u \}$
    \li     \For $v \in \attrib{G}{adj}[u]$ \Do
    \li         $\proc{Relax}(u, v, w)$
            \End
        \End
\end{codebox}
</div>
<div class="column" width="60%">

\pause

\small

**Análise de corretude** \pause

O algoritmo mantém a seguinte invariante: \pause \vspace{-1em}

- No início de cada iteração do laço \While, $\attrib{v}{d} = \delta(s, v)$ para todos $v \in S$ \pause

A invariante é verdadeira antes da primeira iteração? \pause \vspace{-1em}

- Sim! \pause $S = \emptyset$, então é verdadeira por nulidade. \pause

Vamos deixar a manutenção de lado por um instante e pensar no término. Quando o laço termina, quais vértices estão em $S$? \pause \vspace{-1em}

- Todos, então, pela invariante, $\attrib{v}{d} = \delta(s, v)$, para todo $v \in V$ e o algoritmo produz a resposta correta!

\pause

Agora precisamos mostrar como a invariante é mantida quando um vértice é adicionado a $S$.

</div>
</div>


## Algoritmo de Dijkstra

<div class="columns">
<div class="column" width="35%">

\small

\begin{codebox}
    \Procname{$\proc{Dijkstra}(G, w, s)$}
    \li $\proc{Initialize-Single-Source}(G, s)$
    \li $S = \emptyset$
    \li $Q = \attrib{G}{V}$
    \li \While $Q \not = \emptyset$ \Do
    \li     $u = \proc{Extract-Min}(Q)$
    \li     $S = S \cup \{ u \}$
    \li     \For $v \in \attrib{G}{adj}[u]$ \Do
    \li         $\proc{Relax}(u, v, w)$
            \End
        \End
\end{codebox}
</div>
<div class="column" width="65%">

\small

\pause

**Análise de corretude** \pause

Invariante: no início de cada iteração do laço \While, $\attrib{v}{d} = \delta(s, v)$ para todos $v \in S$. \pause

Manutenção: Temos que mostrar que quando o vértice $u$ é extraído da fila (linha 5) e adicionado ao conjunto $S$ (linha 6) $\attrib{u}{d} = \delta(s, u)$. Vamos supor que $\attrib{u}{d} > \delta(s, u)$ e derivar uma contradição.\pause \vspace{-1em}

- $u$ pode ser o $s$? \pause Não, pois $\attrib{s}{d} = 0 = \delta(s, s)$; \pause
- Existe algum caminho entre $s$ e $u$? \pause Sim, pois se não $\delta(s, u) = \infty$ e o algoritmo não poderia ter encontrado $\attrib{u}{d} > \delta(s, u)$; \pause
- Seja $p$ um caminho de peso mínimo entre $s$ e $u$ ($w(p) = \delta(s, u)$). \pause
- Como $s \in S$ e $u \not \in S$, então no caminho $p$ existe pelo menos uma aresta que conecta um vértice de $S$ com um vértice que não está em $S$. Seja $(x, y)$ a primeira aresta em $p$ que faz isso ($x \in S$ e $y \not \in S$).

</div>
</div>


## Algoritmo de Dijkstra

<div class="columns">
<div class="column" width="35%">

\small

\begin{codebox}
    \Procname{$\proc{Dijkstra}(G, w, s)$}
    \li $\proc{Initialize-Single-Source}(G, s)$
    \li $S = \emptyset$
    \li $Q = \attrib{G}{V}$
    \li \While $Q \not = \emptyset$ \Do
    \li     $u = \proc{Extract-Min}(Q)$
    \li     $S = S \cup \{ u \}$
    \li     \For $v \in \attrib{G}{adj}[u]$ \Do
    \li         $\proc{Relax}(u, v, w)$
            \End
        \End
\end{codebox}
</div>
<div class="column" width="65%">

\small

**Análise de corretude**

Invariante: no início de cada iteração do laço \While, $\attrib{v}{d} = \delta(s, v)$ para todos $v \in S$.

Manutenção: Temos que mostrar que quando o vértice $u$ é extraído da fila (linha 5) e adicionado ao conjunto $S$ (linha 6) $\attrib{u}{d} = \delta(s, u)$. Vamos supor que $\attrib{u}{d} > \delta(s, u)$ e derivar uma contradição. \vspace{-1em}

- Se não existem arestas de peso negativo no grafo, então $\delta(s, x) + w(x, y) \le \delta(s, u)$. \pause
- Pela hipótese indutiva $\attrib{x}{d} = \delta(s, x)$ e portanto $\attrib{x}{d} + w(x, y) \le \delta(s, u)$. \pause
- A aresta $(x, y)$ foi relaxada quando $x$ foi adicionada a $S$, portanto $\attrib{y}{d} \le \attrib{x}{d} + w(x, y)$. \pause
- Qual a relação entre os valores de $d$ do vértice $u$ e $y$? \pause $\attrib{u}{d} \le \attrib{y}{d}$ porque $u$ foi escolhido primeiro que $y$. \pause
- $\attrib{u}{d} \le \attrib{y}{d} \pause \le \attrib{x}{d} + w(x,y) \pause \le \delta(s, u)$, \pause uma contradição!

</div>
</div>

## Arestas com pesos negativos

Nós vimos que a corretude do algoritmo de Dijkstra requer que o grafo não tenha arestas de peso negativo. \pause Mas e se o grafo tiver arestas de peso negativos, podemos determinar os caminhos de peso mínimo? \pause Vamos fazer um exemplo e pensar nessa questão.


## Arestas com pesos negativos

![](imagens/Fig-24-1.pdf){width=7cm}

\pause
O que podemos observar em relação as arestas de peso negativo e os caminhos de peso mínimo? \pause

- Arestas de peso negativo podem gerar ciclos de peso negativo; \pause
- Os caminhos de peso mínimo que não envolvem ciclos de peso negativo continuam bem definidos; \pause
- Os ciclos de peso negativo que são acessíveis a partir da origem tornam "impossível" enumerar alguns caminhos de peso mínimo (ex: $\langle s, e, f, e, f, \dots \rangle$).


## Arestas com pesos negativos

Como lidar com caminhos entre $s$ e $v$ que envolvam ciclos de peso negativos? \pause

- Vamos ajustar a definição de peso de caminho mínimo para estes casos para $\delta(s, v) = - \infty$; \pause
- Não podemos enumerar os vértices do caminho, mas será que podemos identificar que ele contém um ciclo de peso negativo? \pause

Vamos voltar para as hipóteses de algoritmos baseadas em programação dinâmica e melhoramento iterativo e verificar se podemos empregá-las para encontrar caminhos mínimos em grafos com arestas de peso negativo.


## Relembrando as hipóteses

Programação dinâmica: Expressar os pesos dos caminhos mínimos que usam no máximo $k$ arestas, em termos dos pesos dos caminhos mínimos que usam no máximo $k - 1$ arestas. \pause

Melhoramento iterativo: Iniciar com uma árvore de caminhos qualquer e tentar melhorar os caminhos trocando uma aresta da árvore por uma que não está na árvore.


## Limitações

Existe alguma limitação aparente nessas abordagens que impedem que elas sejam usadas em grafos com arestas de peso negativo (e sem ciclos de peso negativo)? \pause

- Programação dinâmica: \pause encontra todos os caminhos mínimos com até $|V| - 1$ arestas, como os caminhos mínimos, mesmo com arestas de peso negativos (sem ciclos de peso negativo), não podem ter mais que $|V| - 1$ arestas, então as arestas de peso negativo parecem não mudar a hipótese \pause

- Melhoramento iterativo: \pause como o algoritmo só vai parar quando não for possível melhorar mais nenhum caminho, então as arestas de peso negativo parecem não mudar a hipótese \pause

Sabendo que as duas hipóteses ainda são viáveis, agora temos que partir para descrição dos algoritmos e verificação de corretude.


## Melhoramento iterativo

Qual questão ficou em aberto na ideia baseada em melhoramento iterativo? \pause

- Como e em que ordem verificar se as arestas que não estão na árvore podem ser inseridas na árvore e melhorar os caminhos. \pause

Por exemplo, se em um determinado momento tivéssemos os caminhos $s \leadsto a \leadsto b$ e de $b$ pra todos os demais vértices (não necessariamente direto), como verificar se podemos "colocar" a aresta $(a, b)$ na árvore? \pause

Verificando se o peso do caminho $s \leadsto a \rightarrow b$ é menor do que o peso do caminho atual $s \leadsto b$, \pause ou seja, relaxando a aresta $(a, b)$! \pause Como o peso do caminho $s \leadsto b$ mudou, temos que mudar o peso de todos os caminhos que começam com $b$... \pause e como fazer isso? \pause Relaxando as arestas dos caminhos. \pause Então, de fato, não precisamos apenas relaxar as arestas que não estão na árvore, pode ser necessário relaxar as próprias arestas da árvore. A questão continua, em que ordem?


## Programação dinâmica

E a ideia baseada em programação dinâmica? \pause

- Nós escrevemos a função recursiva mas não discutimos como implementá-la.


## Programação dinâmica

\small

$\delta^k(s, v)$ -- peso do caminho mínimo de $s$ para $v$ que utiliza até $k$ arestas
$$\delta^k(s, v) =
\begin{cases}
  0 & \text{se $s = v$ e $k = 0$} \\
  \infty & \text{se $s \not = v$ e $k = 0$} \\
  \min \begin{cases}
    \delta^{k-1}(s, v) \\
    \min\limits_{(u, v) \in E}(\delta^{k-1}(s, u) + w(u, v))
  \end{cases} & \text{caso contrário}
\end{cases}$$

\pause

O que o "caso contrário" nos diz? \pause

- O caminho mínimo de $s$ para $v$ com até $k$ arestas é o mesmo que o caminho mínimo com até $k - 1$ arestas; ou \pause
- O caminho mínimo de $s$ para $v$ com até $k$ arestas tem exatamente $k$ arestas e então pode ser obtido a partir de um caminho mínimo com $k-1$ arestas. \pause Por que isso é verdade? \pause Porque caminhos mínimos tem subestrutura ótima!


## Programação dinâmica

Como seria uma implementação _bottom-up_?\pause

- Começamos, de forma trivial, com uma árvore de caminhos mínimos com até 0 aresta; \pause
- Depois, a partir da árvore de caminhos mínimos com até 0 aresta, encontramos a árvore de caminhos mínimos com até 1 aresta; \pause
- Depois, a partir da árvore de caminhos mínimos com até 1 aresta, encontramos a árvore de caminhos mínimos com até 2 aresta; \pause
- E assim por diante até caminhos mínimos com até $|V| - 1$ arestas.


## Programação dinâmica

Note de que certa forma esse é um algoritmo de melhoramento iterativo \pause

* Os caminhos mínimos com até $k - 1$ arestas são uma estimativa para os caminhos mínimos com até $|V| - 1$ arestas; \pause
* Na iteração $k$, buscamos melhorar as estimativas obtidas na iteração $k - 1$. \pause

Esta "visão" de uma abordagem de melhoramento iterativo é mais interessante que a outra, isto porque ela define claramente uma forma de progresso para o algoritmo e o momento de parada. \pause

Vamos seguir com a ideia de programação dinâmica e escrever o algoritmo!


## Programação dinâmica

O algoritmo precisa fazer $|V| - 1$ iterações. Em uma iteração $k > 0$ precisamos construir uma nova árvore a partir da árvore da iteração $k - 1$, como fazemos isso? \pause "Aplicando" a equação para cada vértice. \pause

<div class="columns">
<div class="column" width="50%">
\small
\begin{codebox}
    \zi \Comment Computar $\attrib{v}{d}^0$ e $\attrib{v}{\pi}^0$ para todo $v \in V$
    \zi \For $k \gets 1$ \To $|V| - 1$ \Do
    \zi   \For each vertex $v \in V$ \Do
    \zi     $\attrib{v}{d}^k = \attrib{v}{d}^{k-1}$
    \zi     $\attrib{v}{\pi}^k = \attrib{v}{\pi}^{k-1}$
    \zi     \For each edge $(u, v) \in E$ \Do
    \zi       \If $\attrib{v}{d}^k > \attrib{u}{d}^{k-1} + w(u, v)$ \Then
    \zi         $\attrib{v}{d}^k = \attrib{u}{d}^{k-1} + w(u, v)$
    \zi         $\attrib{v}{\pi}^k = u$
              \End
            \End
          \End
        \End
\end{codebox}
</div>
<div class="column" width="50%">
\pause

\small

O que poderia ser difícil de implementar nesse código? \pause

Fazer a repetição usando as arestas que entram em $v$. \pause A dificuldade existe porque em uma lista de adjacências temos as arestas que saem de um vértice e não as que entram. \pause

Como resolver esse problema? \pause Criando uma lista de adjacências com as arestas que entram nos vértices! \pause

Tem outra maneira? \pause Sim!

</div>
</div>

## Programação dinâmica

<div class="columns">
<div class="column" width="50%">
\small
\begin{codebox}
    \zi \Comment Computar $\attrib{v}{d}^0$ e $\attrib{v}{\pi}^0$ para todo $v \in V$
    \zi \For $k \gets 1$ \To $|V| - 1$ \Do
    \zi   \For each vertex $v \in V$ \Do
    \zi     $\attrib{v}{d}^k = \attrib{v}{d}^{k-1}$
    \zi     $\attrib{v}{\pi}^k = \attrib{v}{\pi}^{k-1}$
    \zi     \For each edge $(u, v) \in E$ \Do
    \zi       \If $\attrib{v}{d}^k > \attrib{u}{d}^{k-1} + w(u, v)$ \Then
    \zi         $\attrib{v}{d}^k = \attrib{u}{d}^{k-1} + w(u, v)$
    \zi         $\attrib{v}{\pi}^k = u$
              \End
            \End
          \End
        \End
\end{codebox}
</div>
<div class="column" width="50%">
Você consegue identificar algo familiar no código? \pause O relaxamento da aresta $(u, v)$. \pause

Qual é o propósito do relaxamento? \pause Tentar melhorar a estimativa de caminho mínimo para $v$. \pause

Da forma que o código está escrito, as tentativas de melhora para $v$ são feitas uma após a outro. \pause Isto é necessário ou poderíamos intercalar tentativas? Tentar uma melhora para um vértice, depois tentar para outro e assim por diante até tentar todas as melhoras para todos os vértices? \pause

Podemos tentar as melhoras em qualquer ordem!

</div>
</div>


## Programação dinâmica

<div class="columns">
<div class="column" width="50%">
\small
\begin{codebox}
    \zi \Comment Computar $\attrib{v}{d}^0$ e $\attrib{v}{\pi}^0$ para todo $v \in V$
    \zi \For $k \gets 1$ \To $|V| - 1$ \Do
    \zi   \For each vertex $v \in V$ \Do
    \zi     $\attrib{v}{d}^k = \attrib{v}{d}^{k-1}$
    \zi     $\attrib{v}{\pi}^k = \attrib{v}{\pi}^{k-1}$
          \End
    \zi   \For each edge $(u, v) \in E$ \Do
    \zi     \If $\attrib{v}{d}^k > \attrib{u}{d}^{k-1} + w(u, v)$ \Then
    \zi       $\attrib{v}{d}^k = \attrib{u}{d}^{k-1} + w(u, v)$
    \zi       $\attrib{v}{\pi}^k = u$
            \End
          \End
        \End
\end{codebox}
</div>
<div class="column" width="50%">
\small

Para facilitar a programação verificamos as arestas na ordem que elas aparecem nas listas de adjacências. \pause

Tem mais alguma coisa que podemos modificar no código para deixar a implementação mais fácil? \pause Ao invés de cada vértice ter atributos $d$ e $\pi$ para cada valor de $k$, cada vértice pode ter apenas um atributo $d$ e $\pi$ (vamos ver a seguir porque isso é possível). \pause Isso permite três simplificações: \pause

- O uso de \proc{Initialize-Single-Source} para computar os valores iniciais de $d$ e $\pi$ \pause
- A remoção da repetição que inicializa os atributos $d$ e $\pi$ da iteração $k$ a partir dos valores da iteração $k - 1$ \pause
- O uso de \proc{Relax}

</div>
</div>


## \proc{Bellman-Ford}

O algoritmo que obtemos é chamado de \proc{Bellman-Ford}.

<div class="columns">
<div class="column" width="50%">
\begin{codebox}
    \Procname{$\proc{Bellman-Ford}(G, w, s)$}
    \li $\proc{Initialize-Single-Source}(G, s)$
    \li \For $i \gets 1$ \To $|\attrib{G}{V}| - 1$ \Do
    \li     \For each edge $(u, v) \in \attrib{G}{E}$ \Do
    \li         $\proc{Relax}(u, v, w)$
            \End
        \End
    \li \For each edge $(u, v) \in \attrib{G}{E}$ \Do
    \li     \If $\attrib{v}{d} > \attrib{u}{d} + w(u, v)$ \Then
    \li         \Return \const{false}
            \End
        \End
    \li \Return \const{true}
\end{codebox}
</div>
<div class="column" width="50%">
\pause

**Análise do tempo de execução**

\pause

- A inicialização na linha 1 demora $\Theta(V)$

- Cada uma das $|V| - 1$ passagens das linha 2 a 4 demora o tempo $\Theta(E)$, totalizando $\Theta(V \cdot E)$

- O laço das linha 5 a 7 demora $O(E)$

- Tempo de execução do algoritmo $\Theta(V \cdot E)$
</div>
</div/>

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=5cm,trim=0pt 1016pt 2484pt 0pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=5cm,trim=1242pt 1016pt 1242pt 0pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=5cm,trim=2484pt 1016pt 0pt 0pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=5cm,trim=0pt 0pt 2484pt 1016pt,clip,]{imagens/Fig-24-4.pdf}

## Algoritmo de Bellman-Ford

Relaxação das arestas na ordem $(t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s), (s,t), (s,y)$

\includegraphics[width=5cm,trim=1242pt 0pt 1242pt 1016pt,clip,]{imagens/Fig-24-4.pdf}


## Correture de Bellman-Ford

Nos derivamos o algoritmo a partir do modelo de programação dinâmica. Na iteração $k$ o algoritmo fazia: \pause

- Na primeira versão, selecionava um vértice, inicializa $d^k$ e $\pi^k$ e relaxava as arestas que "entravam" no vértice; \pause

- Na segunda versão, inicializa $d^k$ e $\pi^k$ para todos os vértices e depois relaxava todas as arestas; \pause

- Na terceira versão (Bellman-Ford), usava apenas uma "versão" de $d$ e $\pi$ e relaxada todas as arestas; \pause

Porque o algoritmo de Bellman-Ford funciona?


## Correture de Bellman-Ford

Após \proc{Initialize-Single-Source}, qual é a única forma utilizada pelo algoritmo para mudar as estimativas de caminhos mínimos (atributo $d$)? \pause A função de relaxamento. \pause


Vamos pensar em caminhos mínimos que estão sendo (ou já foram) construídos pelo algoritmo e o uso da função de relaxamento.

## Correture de Bellman-Ford

Se $s \leadsto v$ é um caminho mínimo e o algoritmo já encontrou esse caminho mínimo, o que acontece se a função de relaxamento for chamada para qualquer aresta desse caminho? \pause Nada. O caminho continua do jeito que está, ele já é mínimo! \pause

Se $s \leadsto u \rightarrow v$ é um caminho mínimo e o algoritmo já encontrou o caminho mínimo $s \leadsto u$, isto é $\attrib{u}{d} = \delta(s, u)$, o que podemos afirmar após o relaxamento da aresta $(u, v)$? \pause Que $\attrib{v}{d} = \delta(s, v)$. \pause O relaxamento pode ou não mudar a estimativa para $v$: \pause

- Se $\attrib{v}{d}$ já fosse $\delta(s, v)$, então o algoritmo já tinha encontrado um caminho mínimo para $v$ e o relaxamento não faz nada. \pause

- Por outro lado, se $\attrib{v}{d} > \delta(s, v)$, então o relaxamento mudaria $\attrib{v}{d}$ para $\attrib{u}{d} + w(u, v) = \delta(s, u) + w(u, v) = \delta(s, v)$. \pause

Este é o Lema 24.14, propriedade de convergência, apresentado no livro.


## Correture de Bellman-Ford


Se $\langle v_0, v_1, \dots, v_k \rangle$ é uma caminho mínimo de $s = v_0$ até $v_k$ e: \pause

- Em um momento qualquer, mesmo que após relaxamentos diversos, a aresta $(v_0, v_1)$ é relaxada; e \pause
- Em um momento posterior, mesmo que após relaxamentos diversos, a a aresta $(v_1, v_2)$ é relaxada; e \pause
- $\dots$ \pause
- Em um momento posterior, mesmo que após relaxamentos diversos, a aresta $(v_{k-1}, v_k)$ é relaxada. \pause

O que podemos afirmar sobre $\attrib{v_k}{d}$ no final desse processo? \pause Que $\attrib{v_k}{d} = \delta(s, v_k)$! \pause

Este o Lema 24.15, propriedade de relaxamento de caminho, apresentado no livro.


## Correture de Bellman-Ford

<div class="columns">
<div class="column" width="38%">
\begin{codebox}
    \Procname{$\proc{Bellman-Ford}(G, w, s)$}
    \li $\proc{Initialize-Single-Source}(G, s)$
    \li \For $i \gets 1$ \To $|\attrib{G}{V}| - 1$ \Do
    \li     \For each edge $(u, v) \in \attrib{G}{E}$ \Do
    \li         $\proc{Relax}(u, v, w)$
            \End
        \End
    \li \For each edge $(u, v) \in \attrib{G}{E}$ \Do
    \li     \If $\attrib{v}{d} > \attrib{u}{d} + w(u, v)$ \Then
    \li         \Return \const{false}
            \End
        \End
    \li \Return \const{true}
\end{codebox}
</div>
<div class="column" width="62%">

\small

**Análise de corretude** \pause

Cada iteração do laço da linha 2 todas as arestas são relaxadas: \pause \vspace{-1em}

- A primeira iteração relaxa todas as primeiras arestas de todos os caminhos mínimos que têm pelo menos uma aresta \pause
- A segunda iteração relaxa todas as segundas arestas de todos os caminhos mínimos que têm pelo menos duas arestas \pause
- ...
- A $|V| - 1$-ésima iteração relaxa todas as $|V| - 1$-ésima arestas de todos os caminhos que têm $|V| - 1$ arestas \pause

Mesmo sem saber os caminhos mínimos, o algoritmo relaxa todas as arestas de todos os caminhos mínimos em sequência, garantindo, pela propriedade de relaxamento de caminho, que os caminhos mínimos serão calculados corretamente.

<!-- TODO: e o valor true/false? !-->
</div>
</div>


## Revisão

Tanto o algoritmo de Dijkstra quanto o algoritmo de Bellman-Ford são baseados na mesma ideia

- Inicializar os atributos $d$ e $\pi$

- Relaxar as arestas em uma ordem específica \pause

O algoritmo de Dijkstra relaxa cada aresta apenas uma vez e só funciona para grafos sem arestas de peso negativo.

O algoritmo relaxa todas as arestas $|V| - 1$ vezes e funciona para grafos com arestas de peso negativo e identifica grafos com ciclos de peso negativo.


## Exercício

Projete um algoritmo que encontre os caminhos mínimos de única origem em um grafo acíclico orientado. \pause

Solução

- Relaxar as arestas em uma ordem topológica dos vértices


## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 2032pt 1920pt 0pt,clip,width=7cm]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=1920pt 2032pt 0pt 0pt,clip,width=7cm]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 1355pt 1920pt 677pt,clip,width=7cm]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=1920pt 1355pt 0pt 677pt,clip,width=7cm]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 678pt 1920pt 1354pt,clip,width=7cm]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=1920pt 678pt 0pt 1354pt,clip,width=7cm]{imagens/Fig-24-5.pdf}

## Caminhos mínimos de única origem em gaos

\includegraphics[trim=0pt 1pt 1920pt 2031pt,clip,width=7cm]{imagens/Fig-24-5.pdf}


## Caminhos mínimos de única origem em gaos

Por que este algoritmo funciona? \pause

- Como os vértices são processados em ordem topológica, as arestas de qualquer caminho são relaxadas na ordem que aparecem no caminho; \pause

- Pela propriedade de relaxamento de caminho, o algoritmo funciona corretamente.


## Caminhos mínimos de única origem em gaos

<div class="columns">
<div class="column" width="50%">
\begin{codebox}
    \Procname{$\proc{Dag-Shortest-Paths}(G, w, s)$}
    \li ordenar topologicamente $\attrib{G}{V}$
    \li $\proc{Initialize-Single-Source}(G, s)$
    \li \For vértice $u$ em ordem topológica \Do
    \li     \For each vertex $v \in \attrib{G}{adj}[u]$ \Do
    \li         $\proc{Relax}(u, v, w)$
            \End
        \End
\end{codebox}
</div>
<div class="column" width="50%">
\pause
**Análise do tempo de execução**
\pause

- A ordenação topológica da linha 1 tem tempo $\Theta(V + E)$

- \proc{Initialize-Single-Source} na linha 2 tem tempo $\Theta(V)$

- Nos laços das linhas 2 e 3 a lista de adjacências de cada vértices é visitada apenas uma vez, totalizando $V + E$ (análise agregada), como o relaxamento de cada aresta custa $O(1)$, o tempo total é $\Theta(E)$

- Portanto, o tempo de execução do algoritmo é $\Theta(V + E)$
</div>
</div>


<!--
## Aplicação

Caminhos críticos na análise de diagramas PERT (*program evaluation and review technique*)

As arestas representam serviços a serem executados

Os pesos de arestas representam os tempos necessários para execução de determinados serviços

- $(u, v)$, $v$, $(v, x)$: serviço $(u, v)$ deve ser executado antes do serviço $(v, x)$


## Aplicação

Um caminho através desse gao: sequência de serviços

Caminho crítico: é um caminho mais longo pelo gao

- Tempo mais longo para execução de uma sequência ordenada

O peso de um caminho crítico é um limite inferior sobre o tempo total para execução de todos os serviços


## Aplicação

Podemos encontrar um caminho crítico de duas maneiras: \pause

- Tornando negativos os pesos das arestas e executando \proc{dag-shortest-paths}; ou \pause

- Executando \proc{dag-shortest-paths}, substituindo “$\infty$” por “$-\infty$” na linha 2 de \proc{initialize-single-source} e “$>$” por “$<$” no procedimento \proc{relax}

-->

## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 24.
