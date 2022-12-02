---
# vim: set spell spelllang=pt_br:
title: Ordenação topológica
---


## Contextualização

Vamos considerar a execução de algum as atividades: \pause

- Montagem de um computador \pause

- Criação de um arquivo para distribuição de um programa a partir do código fonte \pause

- Vestimento da roupa pela manhã



## Montagem de um produto

Quais são as etapas necessárias na montagem de um computador? \pause

- Colocação do processador na placa mãe \pause

- Colocação do dissipador \pause

- Colocação dos fans \pause

- Fixação da placa mãe no gabinete

- Colocação da memória na placa mãe

- Fixação do disco no gabinete

- $\dots$

Estas tarefas podem ser executadas em qualquer ordem? \pause Não!


## Distribuição de programas


Quais ações (execução de comandos) são necessárias para criar um arquivo para distribuição de um programa a partir do código fonte? \pause

- Compilação de cada arquivo de código fonte (possivelmente em linguagens diferentes) para gerar os códigos objeto \pause

- Ligação dos códigos objetos em arquivos executáveis ou bibliotecas dinâmicas \pause

- Remoção dos símbolos de arquivos executáveis \pause

- Criação dos diretórios onde serão armazenados os arquivos produzidos \pause

- Execução dos testes automatizados \pause

- $\dots$ \pause

Estas tarefas podem ser executadas em qualquer ordem? \pause Não!



## Colocar a roupa pela manhã

Quais são as etapas necessárias para colocar a roupa pela manhã? \pause

- Colocação das meias

- Colocação da calça

- Colocação das roupas íntimas

- Colocação da blusa

- Colocação do cinto

- $\dots$

Estas tarefas podem ser executadas em qualquer ordem? \pause Não!


## Problema

Muitos tarefas requerem a realização de diversas etapas para serem executas. Em geral, existem algumas precedências entre as etapas (algumas precisam ser executas antes do que outras). \pause

Nesse contexto, queremos determinar uma ordem de execução das tarefas que seja válida (nenhum tarefa pode ser executada antes das tarefas que a precedem)


## Problema

Como podemos modelar este problema usando grafos? \pause

- Representando cada etapa por um vértice \pause

- E cada precedência do tipo "a etapa 1 deve ser realizada antes da etapa 2" com uma aresta direcionada que saí do vértice que representa a etapa 1 e entra no vértice que representa a etapa 2.


## Exemplo

<div class="columns">
<div class="column" width="48%">

Por exemplo, considere a colocação de cada peça de roupa como uma etapa: \pause

- Camisa
- Meia
- Calça
- Roupa íntima
- $\dots$ \pause

</div>
<div class="column" width="48%">
Nós podemos representar estas etapas e suas precedências com o seguinte grafo:

\vspace{0.5cm}

\includegraphics[trim=100pt 600pt 800pt 0pt,clip,width=6.5cm]{imagens/Fig-22-7.pdf}

</div>
</div>

\pause

Em que ordem podemos vestir as roupas para que elas "fiquem certas"? \pause

\includegraphics[trim=100pt 75pt 0pt 1200pt,clip,width=9cm]{imagens/Fig-22-7.pdf}


## Solução

Qualquer sequência para colocar as roupas de "forma certa" terá a seguinte característica: para cada aresta $(u, v)$ do grafo o vértice $u$ aparece antes que o vértice $v$ na sequência. \pause

Uma sequência de vértices com essas características é chamada de ordenação topológica. \pause

Encontrar uma ordenação topológica dos vértices de um grafo orientado acíclico é um problema clássico da computação. Vamos ver como resolver este problema.


## Formalização

Uma **ordenação topológica** de um grafo acíclico orientado $G = (V, E)$ é uma ordenação linear de todos os vértices, tal que para toda aresta $(u, v) \in E$, $u$ aparece antes de $v$ na ordenação. \pause

- Se os vértices forem dispostos em uma linha horizontal, todas as arestas devem ter a orientação da esquerda para direita


## Problema

Projete um algoritmo que receba como entrada um grafo acíclico orientado e encontre uma ordenação topológica dos seus vértices. \pause

Observe que formulamos o problema em termos abstratos, de certa forma a ideia de tarefas e precedência não é mais necessária.


## Algoritmo

<div class="columns">
<div class="column" width="60%">

Baseado no exemplo das roupas, podemos criar uma "hipótese" de como resolver o problema? (Ignore por enquanto os carimbos de tempo)

\vspace{1cm}

\includegraphics[clip,width=8cm]{imagens/Fig-22-7.pdf}
</div>
<div class="column" width="40%">

\pause

Método incremental

- Selecione um vértice com grau de entrada 0 e adicione no final da sequência
- Remova este vértice do grafo e repita o processo até que o grafo fique vazio

\pause

Este método funciona e foi descrito pela primeira vez por Kahn.

</div>
</div>


## Exercício

Implemente o algoritmo de Kahn mas sem remover de fato os vértices do grafo.


## Algoritmo

Uma ordenação topológica também pode ser encontrada usando a busca em profundidade. \pause

\includegraphics[trim=0pt 600pt 800pt 0pt,clip,width=7cm]{imagens/Fig-22-7.pdf} \pause

Considerando os eventos de descoberta e termino dos vértices na ordem que eles acontecem, podemos determinar uma ordenação topológica para os vértices? \pause

\includegraphics[trim=100pt 75pt 0pt 1200pt,clip,width=9cm]{imagens/Fig-22-7.pdf}


## Procedimento \proc{topological-sort}

<div class="columns">
<div class="column" width="50%">

\begin{codebox}
  \Procname{$\proc{topological-sort}(G)$}
  \li chamar $\proc{DFS}(G)$ para calcular o
  \zi     tempo de término $\attrib{v}{f}$ para cada vértice
  \li à medida que cada vértice é finalizado,
  \zi     inserir o vértice à frente de uma lista ligada
  \li \Return a lista ligada de vértices
\end{codebox}

</div>

<div class="column" width="50%">

\small

\pause

**Tempo de execução** \pause

- O tempo de execução da busca em profundidade é $\Theta(V + E)$

- O tempo para inserir cada vértice na lista de saída é $O(1)$, cada vértice é inserido apenas uma vez e portanto o tempo total gasto em operações de inserções é de $\Theta(V)$ \pause

- Portanto, o tempo de execução do algoritmo é $\Theta(V + E)$

</div>
</div>


## Corretude

### Lema 22.11

Um grafo orientado $G$ é acíclico se e somente se uma busca em profundidade de $G$ não encontra arestas de retorno.

\pause

### Prova

Veja o livro.


## Corretude

### Teorema 22.12

$\proc{topological-sort}(G)$ produz uma ordenação topológica do grafo acíclico orientado $G$.

\pause

Precisamos mostrar que se $(u, v) \in E$, então $\attrib{v}{f} < \attrib{u}{f}$.


## Corretude

Quando a aresta $(u, v)$ é explorada, quais são as cores de $u$ e $v$? \pause

- $u$ é cinza \pause

- $v$ é cinza também? \pause Não, porque isto implicaria que $v$ é ancestral de $u$, e portando a aresta $(u, v)$ seria uma aresta de retorno. Gaos não contém arestas de retorno. \pause

- $v$ é branco? \pause Então $v$ torna-se um descendente de $u$. Pelo teorema do parênteses  $\attrib{u}{d} < \attrib{v}{d} < \mathbf{\attrib{v}{f} < \attrib{u}{f}}$. \pause

- $v$ é preto? \pause Então $v$ já foi finalizado. Como a aresta $(u, v)$ está sendo explorada, $u$ não foi finalizado, logo $\attrib{v}{f} < \attrib{u}{f}$. \pause

$\qed$


## Exercícios


22.4-1 Mostre a ordem do vértices produzido por \proc{topological-sort} quando executado no gao da Figura 22.8 (assuma que o for das linhas 5-7 do \proc{DFS} considera os vertices em ordem alfabética e que os vértices nas listas de adjacência estão em ordem alfabética)

\includegraphics[trim=0pt 0pt 0pt 0pt,clip,width=7cm]{imagens/Fig-22-8.pdf}


## Exercícios

22.4-2 Dê um algoritmo de tempo linear que receba com entrada um grafo acíclico orientado $G = (V, E)$ e dois vértices $s$ e $t$ e retorne o número de caminhos simples de $s$ para $t$ em $G$. Por exemplo, o gao da Figura 22.8 contém exatamente quatro caminhos simples do vértice $p$ para o vértice $v$: $pov$, $poryv$, $posryv$ e $psryv$.

\includegraphics[trim=0pt 0pt 0pt 0pt,clip,width=7cm]{imagens/Fig-22-8.pdf}


## Exercícios

Veja a lista de exercícios e algumas soluções na página da disciplina.


## Referências

Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.4.
