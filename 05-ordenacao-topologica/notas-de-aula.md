---
# vim: set spell spelllang=pt_br:
title: Ordenação topológica
---

## Introdução

- Uma **ordenação topológica** de um grafo acíclico orientado $G = (V, E)$
  é uma ordenação linear de todos os vértices, tal que para toda aresta $(u, v)
  \in E$, $u$ aparece antes de $v$ na ordenação

- Se os vértices forem dispostos em uma linha horizontal, todas as arestas
  devem ter a orientação da esquerda para direita

- Aplicações

    - Definição da ordem de execução de tarefas dependentes

    - Por exemplo, `Makefile`


## Introdução

\includegraphics[trim=0pt 600pt 800pt 0pt,clip,width=10cm]{imagens/Fig-22-7.pdf}


## Procedimento \proc{topological-sort}

<div class="columns">
<div class="column" width="45%">
\scriptsize

\begin{codebox}
  \Procname{$\proc{topological-sort}(G)$}
  \li chamar $\proc{DFS}(G)$ para calcular o
  \zi     tempo de término $\attrib{v}{f}$ para cada vértice
  \li à medida que cada vértice é finalizado,
  \zi     inserir o vértice à frente de uma lista ligada
  \li \Return a lista ligada de vértices
\end{codebox}

</div>

<div class="column" width="55%">

\footnotesize

\pause

Tempo de execução \pause

- O tempo de execução da busca em profundidade é $\Theta(V + E)$

- O tempo para inserir cada vértice na lista de saída é $O(1)$, cada vértice
  é inserido apenas uma vez e portanto o tempo total gasto em operações de
  inserções é de $\Theta(V)$ \pause

- Portanto, o tempo de execução do algoritmo é $\Theta(V + E)$

</div>
</div>


## Exemplo de execução

![](imagens/Fig-22-7.pdf)


## Corretude

### Lema 22.11

Um grafo direcionado $G$ é acíclico se e somente se uma busca em profundidade
de $G$ não encontra arestas de retorno.

\pause

Prova feita em sala. Veja o livro para detalhes.


## Corretude

### Teorema 22.12

$\proc{topological-sort}(G)$ produz uma ordenação topológica do grafo acíclico
orientado $G$.

\pause

Precisamos mostrar que se $(u, v) \in E$, então $\attrib{v}{f} < \attrib{u}{f}$.


## Corretude

- Quando a aresta $(u, v)$ é explorada, quais são as cores de $u$ e $v$? \pause

    - $u$ é cinza \pause

    - $v$ é cinza também? \pause

        - Não, porque isto implicaria que $v$ é ancestral de $u$, e portando a
          aresta $(u, v)$ seria uma aresta de retorno. Gaos não contém arestas
          de retorno

    \pause

    - $v$ é branco? \pause

        - Então $v$ torna-se um descendente de $u$. Pelo teorema do parênteses
          $\attrib{u}{d} < \attrib{v}{d} < \mathbf{\attrib{v}{f} < \attrib{u}{f}}$

    \pause

    - $v$ é preto? \pause

        - Então $v$ já foi finalizado. Como a aresta $(u, v)$ está sendo
          explorada, $u$ não foi finalizado, logo $\attrib{v}{f} < \attrib{u}{f}$


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 22.4.
